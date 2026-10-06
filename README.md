# rem / T本智能软件V1.0

以完整 REM 工作法处理 Mission、开展协同工作：依据 Mission 对 Agent 输出做 EVAL，支持 Human 岗位责任对齐；通过内生 HTML 影页呈现目标、输出、证据与责任关系，回查原件并进入受治理行动。
客户端为 VSC + 有效 GitHub Copilot 订阅 / 席位。Mission 推演 / 执行目标为 Sol；rem 自身维护 / 演进目标为 Luna。由 Human 核验 picker 与选择模型，不模拟自动切换，不从订阅声明推导实际运行通过。

## 工作入口

- [Ego](Ego/Ego-rem.md)：责任主体、工作方式与通用能力。
- [RWS](Ego/Rws.md)：rem Work System，已接受的 canonical Work-System source，整合工作台底座、Tools 与工作闭环。
- [Mission](Mission/Story-rem.md) -> [EVAL](Mission/EVAL/eval-rem-v1.md)：产品承诺与验收。
- [INTENT](Repo/INTENT.md) -> [today](Repo/today.md) / [now](Repo/now.md) -> [DONE](Repo/DONE.md)：当前执行与交接。
- [岗位责任](Mission/roles.md)、[Agent 输出](Mission/outputs.md)、[行动证据](Mission/evidence/README.md)。
- [技能登记](Ego/TeamSkill/TeamSkill.md)、[RWS Tools 与 CLI 登记](Ego/Rws.md)、[来源与适配](Ego/TeamSkill/deployment.md)。

## 内生影页与 MPS

影页（Narrative Page）：以 HTML 承载的 Mission 工作评审视图，呈现目标、输出、证据与岗位责任关系，支持 EVAL 和工作对齐；不替代原件与 Human 裁决。确定性 MPS artifact 由 `scripts/mirror.py` 生成，与影页 authoring / review 分开。

按 [RWS](Ego/Rws.md) 的 Python 3.14 / uv 基线、Git 与获准的 source custody review 后，在目标目录运行：

```
uv run python scripts/verify.py
uv run python scripts/mirror.py --request Mission/Requests/bootstrap.toml --approved-by bitguts --approval-evidence Mission/Audit/2026-09-30-bootstrap.md --content-reviewed
```

`--content-reviewed` 只能在 Human / Agent 已按授权完成 no-secret 审查后使用，不赋予权限。文件组显式声明，保留原始非空行与所有 frozen source bytes；数字、状态和句子均可回查。影页与 MPS artifact 的 custody 见 [TeamsPage](Repo/TeamsPage/README.md)。打开 HTML 可离线评审，链接返回原件；内容修改与 Tools 执行回到 VSC / owning workflow。

## 完成边界

这是从 EGO-T189 固定提交派生的独立 Private 产品仓，不携带 T189 服务实例、CRAFTS 或旧历史，不是源仓改名。影页是软件评审输出，不限制任务的真实交付类型。Human acceptance、岗位对齐、Sol/Luna 实际运行分别留证；无证据不宣称完成。当前验收缺口见 [EVAL](Mission/EVAL/eval-rem-v1.md)。
