# Motion: Cloudflare `cf` CLI 与 Stack 决策

> **Date**: 2026-09-30
> **Owner**: yangjun / bitguts
> **Status**: Blocked
> **Owner Approval**: [M1-M3 approval audit](../../../Mission/Audit/2026-09-30-cloudflare-motion-approval.md)
> **Type**: Platform/toolchain selection
> **Service Object**: rem Cloudflare management toolchain and stack boundary
> **Primary Route**: [Story-rem](../../../Mission/Story-rem.md) -> [EVAL](../../../Mission/EVAL/eval-rem-v1.md)
> **Source Request**: Owner 当前会话选择采用 Cloudflare `cf` 方案
> **Round**: R1

本 Motion 是三阶段序列的第 2 阶段，依赖 [EGO DNS 目标域登记](motion-ego-dns-registry-2026-09-30.md) 完成。Owner 已接受候选 Stack，选择 Microsoft Entra SSO、共享只读文件、Free-only 与 staging->production。Owner 报告 full Zone/control 已确认，但尚无独立证据；允许 Entra 组、文件路径、Free entitlement 和 rollback 未闭合，所以状态仍为 Blocked。无认证 smoke 见 [M2 Audit](../../../Mission/Audit/2026-09-30-cf-cli-stack-m2.md)。批准不包括 Cloudflare login、租户 API、资源创建、DNS 变更或部署。

## 问题与拟议裁决

Cloudflare 于 2026-09-28 发布 Agent-oriented CLI `cf`，公告称其处于 open beta，并覆盖 3,000+ API operations；2026-09-29 官方 CLI 文档称提供 2,900+ commands，二者统计口径不同。类型化配置 `cloudflare.config.ts` 目前用于 Workers projects；CLI 操作覆盖、配置覆盖、Stack 资源覆盖与生产安全治理是不同问题。

**Owner 已批准的 M2 范围：**

1. 将 `cf` 作为 rem Cloudflare API 操作的首选 CLI；在实施前复核 open beta 状态、版本、安装来源、包完整性、认证行为和实际命令覆盖，不在生产路径浮动安装 `latest`。
2. 将 Cloudflare stack 定义为按 rem 交付目标挑选的服务/资源组合；不把“全部 Cloudflare API 可调用”解释为所有产品均要部署或已有统一声明式配置。
3. 以 `cloudflare.config.ts` / Vite 作为当前受支持 Worker 项目的首选配置路径；对未覆盖的资源逐项评估 `cf` API、Wrangler 委托、Terraform/provider 或人工管理。每类资源指定一个写入权威，避免双重控制。
4. 生成一份带日期的能力矩阵，记录产品/资源、rem 用途、API 操作、声明式配置、权限、费用、数据影响、环境、验证、回滚与未覆盖项。

第一版条件候选矩阵已生成：[Cloudflare capability matrix](../cloudflare-capability-matrix-2026-09-30.md)。Owner 已接受 Worker Static Assets + hostname-based Access 候选，选择私有门户/文件、`rem.teamsbook.org`、Microsoft Entra SSO、共享只读静态文件、Free-only 与 staging 后 production，并选择 domain-wide `@TeraTeams.com` verified-email allow。邮箱域归属、Entra claim、具体内容路径、Zone 独立证据与 Free entitlement 仍待核实；未核实前不配置 Access policy 或部署。

## 范围

**拟纳入，获批后执行：**

- 依据 Cloudflare 官方文档与 `cf` 发布资料完成无账号访问的高层候选能力矩阵与工具边界审查，详见上方文件；不是 2,900+ command 的逐项完整清单。
- 已在临时目录完成固定版 `cf@1.0.0-beta.5` 的帮助/匿名命令发现与通用 Worker sample 类型生成、本地 build、直接 `cf deploy --dry-run`；结果和 npm 漏洞告警见 M2 Audit。此 generic sample 不替代 rem 交付项目验证，且其 dependency lockfile 不准直接复用。
- 形成适合 rem 的最小首期 stack 建议，以及后续每种资源必须取得的授权、预算、环境和回滚证据。

**不纳入本 Motion 的授权：**

- 全局安装/升级 `cf`，使用 `cf login` / `cf whoami`，读取账号会话、credentials 或 secrets。
- 调用真实 Cloudflare account / Zone API、访问账号资料或探测租户。
- 创建/更新/删除任何远端资源、DNS、Zone、route、Access policy，或执行 `cf deploy`。
- 采购、启用付费服务、设置预算、配置 CI secrets 或发布生产变更。
- 将 Wrangler 或 Terraform 与 `cf` 配置成对同一资源同时写入。

## 执行顺序与停止条件

本地 smoke、generic typed-config/build/dry-run、候选 Stack 和写入工具已确定。M2 仍需核实 Access audience/IdP、文件授权模型、Zone 权限与 Free entitlement；Cloudflare account 登录、远端 API 或资源变更仍须另有具体授权。

官方支持、费用、认证行为、state ownership 或回滚未知时标记 `unknown` / `Blocked`；`cf cli search` 结果仅用于命令发现，不证明调用适用、授权充分或操作安全。

## EVAL

| Gate | 判据 | 必需证据 | 当前状态 |
| --- | --- | --- | --- |
| C1 | 官方 `cf` 状态、版本、范围和安装模型得到当期核验 | 官方资料、npm registry 版本/integrity、固定版 help smoke，见 M2 Audit | pass |
| C2 | 明确区分 API operation、类型化配置与完整生命周期管理 | 日期化候选矩阵、generic sample typed config/build/dry-run 已记录；rem 资源级核验待 Zone/SSO/文件模型 gate | partial |
| C3 | rem 首期 stack 与各工具的唯一写入权威明确 | Owner 接受 Worker Static Assets + hostname-based Access；Worker config 与 Access API 均由 project-pinned `cf` 管理，不引入第二写入工具 | pass |
| C4 | 权限、费用、数据影响、环境、测试和回滚逐项列明 | Entra + domain-wide `@TeraTeams.com` allow、shared-read-only、Free-only/staging->production 已选；domain/claim、内容接受、Zone 证据、Free entitlement、权限和 rollback 尚待确认 | blocked |
| C5 | 未执行未经批准的认证账号操作或资源变更 | M2 Audit 的命令/结果；无登录、资源命令、部署或 DNS 写入 | pass |

## Landing 与回滚

获批产物进入 Repo 中对应的软件配置/运维文档，不把凭据写进 EGO、Motion 或 Git。平台选择若改变，保留 capability matrix 与版本证据，由 Owner 决定切换与迁移；本 Motion 不执行远端回滚或资源清理。

本 Motion 当前 `Blocked`。Owner 已接受候选 Stack 和 domain-wide `@TeraTeams.com` allow；Zone/control 只有 Owner self-attestation，邮箱域/Entra claim、内容路径、Free entitlement 与 rollback 未核验。取得可回查非凭据证据并确认行为前，不登录、不创建 Access policy、不部署。
