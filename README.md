# rem / T本智能软件V1.0

以完整 REM 工作法处理 Mission、开展协同工作：依据 Mission 对 Agent 输出做 EVAL，支持 Human 岗位责任对齐；通过内生 HTML 镜页呈现目标、输出、证据与责任关系，回查原件并进入受治理行动。

客户端为 VSC + 有效 GitHub Copilot 订阅 / 席位。Mission 推演 / 执行目标为 Sol；rem 自身维护 / 演进目标为 Luna。由 Human 核验 picker 与选择模型，不模拟自动切换，不从订阅声明推导实际运行通过。

## 工作入口

- [EGO](EGO/EGO-rem.md)：责任主体、工作方式与通用能力。
- [Mission](Mission/Story-rem.md) -> [EVAL](Mission/EVAL/eval-rem-v1.md)：产品承诺与验收。
- [INTENT](Repo/INTENT.md) -> [today](Repo/today.md) / [now](Repo/now.md) -> [DONE](Repo/DONE.md)：当前执行与交接。
- [岗位责任](Mission/roles.md)、[Agent 输出](Mission/outputs.md)、[行动证据](Mission/evidence/README.md)。
- [技能登记](EGO/TeamSkill/TeamSkill.md)、[工具](EGO/Tools.md)、[来源与适配](EGO/TeamSkill/deployment.md)。

## 内生镜页

镜页（Mirror Page）：以 HTML 承载的 Mission 工作评审视图，呈现目标、输出、证据与岗位责任关系，支持 EVAL 和工作对齐；不替代原件与 Human 裁决。

Python 3.11+、Git 与获准的 source custody review 后，在目标目录运行：

```powershell
python scripts/verify.py
python scripts/mirror.py --request Mission/Requests/bootstrap.toml --approved-by bitguts --approval-evidence Mission/Audit/2026-09-30-bootstrap.md --content-reviewed
```

`--content-reviewed` 只能在 Human / Agent 已按授权完成 no-secret 审查后使用，不赋予权限。文件组显式声明，保留原始非空行与所有 frozen source bytes；数字、状态和句子均可回查。镜页目录为 [review custody](Repo/shape/TeamsPage/README.md)。打开 HTML 可离线评审，链接返回原件；内容修改与 Tools 执行回到 VSC / owning workflow。

## 完成边界

这是从 EGO-T189 固定提交派生的独立 Private 产品仓，不携带 T189 服务实例、CRAFTS 或旧历史，不是源仓改名。镜页是软件评审输出，不限制任务的真实交付类型。Human acceptance、岗位对齐、Sol/Luna 实际运行分别留证；无证据不宣称完成。当前验收缺口见 [EVAL](Mission/EVAL/eval-rem-v1.md)。
