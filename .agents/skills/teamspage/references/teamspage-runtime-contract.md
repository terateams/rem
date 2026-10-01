evidence  可复算命令，或可定位的记录 ID 清单
# TeamPage MPS Runtime Contract

> **Type**: AgentSkill runtime contract（How）
> **Status**: active · R1 implementation
> **Version**: 3.3.0
> **Date**: 2026-09-27
> **Owner**: yangjun (Code Name: bitguts)
> **Authority**: 本文件持 TeamPage MPS runtime How；产品边界与原则见 [concept-rem-teamspage.md](../../../../EGO/TeamSkill/rem/references/concept-rem-teamspage.md)。
> **Consumers**: [TeamPage AgentSkill](../SKILL.md) · [rem-ready T189 adapter](../../../rem-ready/scripts/today_mps_adapter.py) · NP0 handoff

## 1. Typed Request

MPS 接受 caller 组装的 JSON request。通用 renderer 不读取 `today.md`、`INTENT.md`、`now.md`，不包含 Mission、EGO instance、workpoint 或当前任务默认值。

| Field | Contract |
|---|---|
| `snapshot` | NP0 runtime snapshot schema 1.0：binding、四文件 observations、source hashes、permission 与日期基线 |
| `snapshot.permission.teamspage_write` | 必须为 `true`；这是 caller 的 permission declaration，不是权限本身 |
| `as_of` | 可选 ISO date；缺省使用 snapshot 的 `baseline_date`，作为页面的业务观察日期 |
| `mp:sample` | 可选 boolean；仅 eval baseline 可设为 `true`，固定 `as_of` 且不分配 `mp:id`；生产 `generate()` 拒绝 sample request |
| `rem_id` / `repo_locator` / `mission_context` | REM identity、无凭据 owner/repo locator、当前 Mission locator |
| `target` / `viewpoint` | `namespace`、`target_kind`、`target_ref`、`scope` 与 viewpoint 必须明确 |
| `narrative` | 可见文字与决定权、下一步、验证路线；标题是标签，其余句子须有 voice provenance |
| `voice_sources` | 覆盖 `narrative` 中标题以外的每个文本 slot；kind 为 `source_claim`、`signed_quote` 或 `rule_marker` |
| `distortion_declarations` | 显式 list；每项包含 `surface`、正整数 `omitted_count` 与 `reason`；无已声明变换时传空 list |
| `gate_evidence` | 可选 `g_tier` 与 `g_orphan` 的原始证据；缺项呈现为 `not_run` |
| `projection_sources` / `reference_sources` | 每条路径必须位于 `allowed_sources` 并按字节冻结；CRAFTS adapter 另按其 contract 提供来源 |

`source_claim` 与 `signed_quote` 的文本须逐字出现在被授权 frozen source 中；signed quote 还须声明 signer。`rule_marker` 须列出稳定 `rule_id` 与已冻结证据路径。验证证明的是声明可追溯，不证明其现实或业务含义为真。

## 2. G-Distort And G-Voice

`g_distort` 校验失真声明的字段、范围与正整数数量，并把每条声明嵌入页面。它不具备推断任意上游未提供记录的能力；若输入范围或遗漏完整性未知，Human review 仍须保持 `not_run` / `unknown`。

`g_voice` 要求所有可见 narrative 文本 slot 都有来源或 rule-marker provenance。缺项、越权 source、source text 不匹配或无 signer 的 signed quote 均阻断生成。标题视为标识标签，不按句子检查。

Renderer 将来源字段差异与 `g_tier` / `g_orphan` fail evidence 汇总为五字段 failure records，并置于 Name / Event / Trace / Order overview 之前。没有失败记录时显示一条空态声明；未运行检查仍保留 `not_run`，不转成 green pass。

## 3. G-Tier And G-Orphan

- `g_tier` 消费 `verify-tier-a.sh <repo> T189` 的 command、exit code 与 bounded output evidence；exit code 0 为 `pass`，其它为 `fail`。脚本未执行时须给 reason 并记 `not_run`，不得推断通过。
- `g_orphan` 消费 `extract_shape.py` 的 target、`source_revision` 与 `orphans` / `dangling_edges` / `cycles` counts；revision 必须匹配 snapshot HEAD，三个计数全为 0 才是 `pass`。无节点-关系图的 target 可带 reason 声明 `not_applicable`。
- 两类 gate 只报告其实际 target 和 source revision，不外推到全仓；失败显示在页面，不自动改写 Repo。

## 4. G-ID And Output Identity

MPS 页面 ID 为 `YYMMDD S W NNN`：`YYMMDD` 是 `generated_at` 的 UTC 日期，`W` 是该 UTC 日期的 ISO weekday，`NNN` 为每日 001–999 序号。文件名为：

```text
MPS-{YYMMDD}S{W}{NNN}-{target-key}.html
```

Allocator 扫描 live `Repo/shape/TeamsPage/` 与 Git `--all --diff-filter=A` additions；为保持历史编号唯一，Git history 同时扫描旧路径 `Repo/shape/teamspage/`。已用序号不复用，日期/weekday 不一致、重复历史 ID、live 冲突或序号溢出均阻断生成。完整 `snapshot_id` 另存于 envelope；同一 snapshot ID 不得重复写入 live custody。`mp:id` 写入 `#mp-data`，不展示为正文叙事。

生成只写单个 HTML。`mp:sample=true` 的 eval baseline 不分配编号、不写入 review custody，`g_id` 为 `not_applicable`；应由 `build_model()` + `render_html()` 构造到 `MPS/evals/baseline/golden_*/expected.html`，不得经生产 `generate()` 输出。`Repo/shape/TeamsPage/` 是阶段性 custody；删除与保留遵循 REM Concept / owning review 的收口规则，不由 renderer 扫描后自动删除已有 artifact。

## 5. Embedded Envelope And Validation

MPS 输出单个离线 HTML，内嵌且只内嵌一个 `<script id="mp-data" type="application/json">` envelope。Envelope 保存 schema / renderer / contract versions、`mp:sample`、`as_of`、（非 sample 的）`mp:id`、`snapshot_id`、typed target、REM binding、source revisions / hashes / bytes、voice and distortion declarations、external gate evidence、semantic payload 与 checks。

`payload_sha256` 对去掉自身 digest 字段后的 canonical JSON 计算。不得嵌入自引用的完整 HTML hash，也不得生成 companion `.manifest.json`。Validator 检查 payload digest、frozen source 与投影 rows、DOM binding、外部依赖、ID/date/weekday，然后确定性重建并逐字节比较 HTML；提供 `repo` 时额外复核 G-ID 历史和当前 frozen-source freshness。

`observed_at`、`generated_at`、`reviewed_at` 分开并带时区。机器通过不代表 Human review、Mission EVAL、现实真值或 Owner Adopt。

## 6. Checks And CLI

Check values use `pass` / `fail` / `not_run` / `not_applicable` / `unknown` where applicable. Projection、source consistency、human review、runtime、freshness、G-ID、G-Distort、G-Voice、G-Tier、G-Orphan 分开记录；没有运行不得写 pass。

```text
python .agents/skills/teamspage/MPS/scripts/mps.py --repo <repo> --input <typed-request.json> --capture
python .agents/skills/teamspage/MPS/scripts/mps.py --repo <repo> --artifact <artifact.html>
python .agents/skills/teamspage/MPS/scripts/mps.py --repo <repo> --index
python .agents/skills/rem-ready/scripts/today_mps_adapter.py --repo <repo> --target-dir Repo/shape/TeamsPage
```

`--artifact` 只接受带当前 `#mp-data` envelope 的 MPS HTML；`.manifest.json` sidecar 与无 envelope 的旧 HTML 均不是 MPS input，不提供 legacy compatibility parser。新输出始终只有 HTML。`--export` 只接受合法 HTML 并写入 `Mission/` destination。MPS 不提供清理既有过程文件的 CLI。
