from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from html.parser import HTMLParser
from typing import Any


class EmbeddedManifestParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.count = 0
        self.active = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "script":
            return
        attributes = dict(attrs)
        if attributes.get("id") != "mp-data":
            return
        if attributes.get("type") != "application/json" or self.active:
            raise ValueError("Invalid embedded manifest script")
        self.count += 1
        self.active = True

    def handle_data(self, data: str) -> None:
        if self.active:
            self.parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self.active:
            self.active = False


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def payload_digest(value: dict[str, Any]) -> str:
    unsigned = deepcopy(value)
    unsigned.pop("payload_sha256", None)
    unsigned.pop("html_sha256", None)
    return hashlib.sha256(canonical_json(unsigned).encode("utf-8")).hexdigest()


def build_embedded_payload(model: dict[str, Any]) -> dict[str, Any]:
    payload = deepcopy(model)
    payload.pop("html_sha256", None)
    payload.pop("payload_sha256", None)
    payload.setdefault("artifact_type", "mirror-page")
    payload["payload_sha256"] = payload_digest(payload)
    return payload


def encode_embedded_payload(model: dict[str, Any]) -> str:
    payload = build_embedded_payload(model)
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


def extract_embedded_payload(document: str) -> dict[str, Any]:
    parser = EmbeddedManifestParser()
    parser.feed(document)
    if parser.active or parser.count != 1:
        raise ValueError("Expected exactly one closed #mp-data JSON envelope")
    try:
        payload = json.loads("".join(parser.parts))
    except json.JSONDecodeError as error:
        raise ValueError("Invalid #mp-data JSON envelope") from error
    if not isinstance(payload, dict):
        raise ValueError("#mp-data envelope must be a JSON object")
    declared_digest = payload.get("payload_sha256")
    if not isinstance(declared_digest, str) or declared_digest != payload_digest(payload):
        raise ValueError("Embedded payload digest mismatch")
    if "html_sha256" in payload:
        raise ValueError("Embedded envelope must not claim a self-contained HTML hash")
    return payload
