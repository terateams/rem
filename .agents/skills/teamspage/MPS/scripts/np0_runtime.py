from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any


def load_runtime_snapshot() -> ModuleType:
    np0_scripts = Path(__file__).resolve().parents[3] / "np0" / "scripts"
    source = np0_scripts / "runtime_snapshot.py"
    if not source.is_file():
        raise ImportError(f"Missing NP0 runtime snapshot dependency: {source}")
    if str(np0_scripts) not in sys.path:
        sys.path.insert(0, str(np0_scripts))

    existing = sys.modules.get("runtime_snapshot")
    if existing is not None:
        existing_path = Path(getattr(existing, "__file__", "")).resolve()
        if existing_path != source.resolve():
            raise ImportError("Conflicting runtime_snapshot module is already loaded")
        return existing

    spec = importlib.util.spec_from_file_location("runtime_snapshot", source)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load NP0 runtime snapshot dependency: {source}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


runtime_snapshot = load_runtime_snapshot()
SnapshotBlocked: type[ValueError] = runtime_snapshot.SnapshotBlocked

generate_observations: Any = runtime_snapshot.generate
git: Any = runtime_snapshot.git
prepare: Any = runtime_snapshot.prepare
require: Any = runtime_snapshot.require
source_file: Any = runtime_snapshot.source_file
