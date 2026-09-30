# Motion: teamsbook.org 对外交付与 Cloudflare 自动化

> **Date**: 2026-09-30
> **Owner**: yangjun / bitguts
> **Status**: Blocked
> **Owner Approval**: [M1-M3 approval audit](../../../Mission/Audit/2026-09-30-cloudflare-motion-approval.md)
> **Type**: External delivery implementation
> **Service Object**: teamsbook.org 上的首个 rem 对外交付
> **Primary Route**: [Story-rem](../../../Mission/Story-rem.md) -> [EVAL](../../../Mission/EVAL/eval-rem-v1.md)；保留唯一 Primary，不创建 Secondary
> **Source Request**: 当前会话，2026-09-30
> **Round**: R1

本文件是三阶段序列的第 3 阶段，Owner 已批准其书面范围，并选择私有门户/文件、目标 hostname `rem.teamsbook.org`、Microsoft Entra SSO、共享只读文件、Free-only 与 staging 后 production。Owner 接受 M2 的 Worker Static Assets + hostname-based Access 候选，并选择允许所有已验证 `@TeraTeams.com` 邮箱。该规则覆盖整个邮箱域；域名归属和 Entra claim 尚未核验。REM 方法介绍草稿见 [Mission/teamsbook.org/index.md](../../../Mission/teamsbook.org/index.md)，Owner 已接受其用于 staging-preview 准备；内容仍是 non-authority，尚未转成 HTML/build 或发布。Owner 报告 full Zone/control 与 Free entitlement 已确认但尚无独立证据，因此 M2/M3 仍为 Blocked。不创建 policy、不登录、不改 DNS、不部署。

## 请求与事实边界

- Owner 指定 `teamsbook.org` 为 rem **目标交付根域**，并选择 `rem.teamsbook.org` 为首个目标 hostname。其 EGO canonical root-domain record 由 M1 建立；本 Motion 仅消费该根域记录和当前 hostname 输入，不改 EGO/DNS。域名注册人、控制权、Cloudflare Zone 与 DNS 委派尚未独立核验；目标 hostname 不证明所有权或可用性。
- Owner 确认首个交付为共享只读静态门户/文件，不需要上传或 per-user ACL；具体文件集/root path 与允许 Entra 组尚未给出。
- The authorized local content draft now exists at `Mission/teamsbook.org/index.md`. It is a non-authority introduction to the REM work method based on current Repo/EGO/Mission sources; it is not yet approved for publication and does not create new method authority.
- Owner 选择 Free-only；若 Access/Workers/域名方案要求任何付费计划或付费附加项，停止而不升级/购买。此选择不证明账户 entitlement 或静态资产/Access 功能在目标账号可用。
- Requester 提供 Cloudflare 登录标识 `bigits@gmail.com`。它仅是未核验的账号定位信息，不是凭据或授权；本 Motion 不允许 Agent 登录、检查账号、读取凭据或索取认证因子。
- “采用 Cloudflare 最新 CLI、自动化部署 Cloudflare 全部能力”尚未定义交付物、服务清单、hostname、成本上限及权限边界。“全部能力”不可直接作为一次性生产部署范围。
- 当前 rem 仓库尚无已绑定的 Cloudflare Worker / Pages 配置或获批的对外 hostname。产品输出和 EVAL 仍由 Story-rem / EVAL 持有。

Cloudflare 于 2026-09-28 发布的官方公告介绍了 `cf`：面向 Agent 的 Cloudflare CLI，公告称它扩展到 3,000+ API operations、默认提供 JSON，并提供 `cf cli search` 命令发现；发布时为 open beta。公告同时把 `cloudflare.config.ts` 描述为 Cloudflare 整体的类型化配置方向，但当时从 Workers 起步，Policies、Zones、DNS 等完整配置支持仍属后续计划。CLI API operation 覆盖不能推导为所有产品已有成熟、幂等、可回滚的声明式配置。

公告还说明 `cf` 默认采用 Vite / Cloudflare Vite Plugin；需继续使用 esbuild 的部分 JavaScript Worker 与 Rust / Python Worker 的开发、部署仍会委托 Wrangler。因此本 Motion 采用 `cf` 为 Cloudflare API 自动化主路径，Wrangler 仅保留为 `cf` 明确委托或迁移兼容路径；Terraform 等 IaC 只在经评估确有状态管理需要且 provider 覆盖适配时补充，不与 `cf` 双重管理同一资源。

## 问题与拟议裁决

rem 需要以可审阅、可复现、可回滚的方式交付一个私有门户/文件产物。根域与 hostname、Microsoft Entra SSO、共享只读文件、Free-only 及 staging->production 顺序已选；M1/M2 acceptance、域名控制权的独立证据、Cloudflare Zone/account 绑定、允许 Entra 组、具体文件路径、Free entitlement、最小权限和回滚仍是前置条件。

**Owner 已批准的 M3 边界；执行仍受下述 gate 限制：**

1. 以 M1 完成的 EGO/DNS canonical record 为唯一根域来源；Owner 当前选择的 `rem.teamsbook.org` 作为本 Motion hostname input，不新增或修改 EGO 文件。只有 Owner 提供可回查的域名控制与对应 Zone 证据后，才允许实施绑定。
2. 以 M2 已接受的 Worker Static Assets + hostname-based Access 候选及能力矩阵为实现边界；不重新解释或扩大工具覆盖，不加入任何额外产品或付费能力。
3. 只使用 M2 锁定并经 Owner 接受的 `cf` / 兼容工具版本与资源所有权设计；同一资源只设一个写入权威。任何超出已批准矩阵的资源都先另行裁定。
4. 自动化采用本地验证 -> 非生产验证 -> 经批准的生产发布分段。生产 DNS、hostname、证书、Worker route、资源创建、费用及外部发布各自遵守针对具体变更的 Owner permission gate。

## EGO、Stack 与 CLI 的边界

- **EGO/DNS record** 是“rem 的对外交付目标根域是什么”的权威登记，由 M1 建立。本 Motion 消费 `teamsbook.org` 对应记录，不重复维护域名值，也不据此推导控制权。
- **Cloudflare stack** 是实现交付的服务 / 资源组合及其关系，例如按需要选择 DNS、Workers / 静态资产、Access、WAF、数据服务与观察性。它回答“实际由哪些组件组成”，不是命令行工具，也不表示必须启用全部产品。`CDS` 在本 Motion 中只是对该 Cloudflare 实现栈的描述，不新增治理 token。
- **`cf` CLI** 是操作 Cloudflare API 的 Agent-oriented 工具入口，不是 EGO 或 Cloudflare stack 本身。按前述官方公告，`cf` 是 API 自动化主路径；当前 open beta、API 操作覆盖、类型化配置覆盖和生产治理是不同判据。`cloudflare.config.ts`、Wrangler 委托和必要 IaC 按实际发布能力分别验证。
- 因此建议关系为：EGO 指定目标域 -> 获批的 Cloudflare stack 定义组件 -> `cf`（及明示的兼容 / IaC 工具）执行有界操作。配置字段、工具可调用性和用户授权互不替代。

## 范围

**拟纳入，批准后实施：**

- 由 Owner 提供非凭据证据，核验 `teamsbook.org` 的控制权、Cloudflare account / Zone 归属、现有 DNS 与受影响服务；记录未知，不读取或复制认证材料。
- Microsoft Entra ID 与全域 verified-email 规则 `@TeraTeams.com` 已选；核验该邮箱域属于目标组织且 Entra claim 匹配。给出待发布的具体文件/root path。共享只读、no-upload、no-per-user-ACL 已确认；若实际文件集要求偏离此模型，停止并另行设计。
- 消费 M2 已审核的 Cloudflare 能力矩阵及工具边界；本 Motion 不承担全平台盘点，也不因 API 可调用就扩展部署范围。
- 先选定一种有明确产物与消费者的 rem 交付路径，再建立版本锁定、测试、preview / staging、发布记录和回滚流程。具体应用形态与 hostname 留待 Owner 裁定。
- 只有在后续批准的范围中才配置 CI/CD；凭据由获批的 secret store 管理，采用满足该工作流的最小权限，不写入仓库、命令行参数或本 Motion。

**本 Motion 明确排除的操作：**

- 登录或检查 `bigits@gmail.com` 对应的账号，访问 Cloudflare tenant、读取凭据或代表 Owner 接受条款。
- 注册 / 转移域名，修改 nameserver、DNS、Zone、TLS、Access、路由或生产流量。
- 创建、启用、试用或部署任何会产生费用、处理真实数据或改变外部状态的服务；包括 Workers AI 等可能在开发时也计费的能力。
- 一次性自动部署所有 Cloudflare 产品；依据账号可见性、登录邮箱或已有资源推断权限、付款方式、域名所有权或可用性。
- 修改 EGO/DNS、EGO-rem、Story-rem 或 EVAL authority；上述 EGO 域名登记只由 M1 持有。

## 执行阶段与停止条件

1. **R1 / Entry gate**：Owner 接受 M1 的 EGO/DNS record 与 M2 的 Stack 决策。若 M1/M2 尚未接受，或 Zone/control 仍无可回查证据、`@TeraTeams.com` 归属/Entra claim、内容路径、Free entitlement、权限及回滚未确认，保持 `Blocked`，不登录、不探测租户。
2. **R2 / Bounded design**：Owner 指定一个交付切片与消费者；按 M2 锁定版本和资源写入权威产出本地计划、测试、权限/费用清单与回滚方案。本阶段不得写入远端资源。
3. **R3 / Non-production**：只有在单独明确批准非生产 account / Zone、权限、预算和测试数据后，才可建立或更新 staging。记录 CI 身份、实际变更、费用观察、验证及回滚结果。
4. **R4 / Production**：生产资源、域名记录、DNS / route、证书与流量切换必须有针对该具体变更的 Owner 批准及已验证回滚方案；未获批步骤保持 `not_run`。新增服务需更新 capability matrix 并另行批准。

任一阶段若域名 / Zone 控制权、权限、产品支持、费用、数据处理、回滚或实际命令结果不明，即停止受影响动作并报告 `unknown` / `Blocked`；不得以 `cf` 安装成功、命令搜索结果、API 覆盖宣称、配置类型检查、dry-run、CI 绿色或静态测试代替真实部署证据。

## EVAL / 交付判据

| Gate | 判据 | 必需证据 | 当前状态 |
| --- | --- | --- | --- |
| D1 | M1 已登记唯一 EGO/DNS target record；另行确认域名控制权、Cloudflare account / Zone 及既有 DNS 风险 | M1 canonical record 与 Owner 提供的可回查非凭据控制权证据；账号标识不等于验证 | not_run |
| D2 | 明确交付物、消费者、hostname、环境、数据分类、预算与 decision-rights | 私有门户/文件、`rem.teamsbook.org`、Entra SSO、全域 `@TeraTeams.com` allow、共享只读、Free-only 与 staging->production 已选；内容已接受用于 staging-preview 准备；域/claim/Free entitlement pending | partial |
| D3 | M2 的 Cloudflare 能力矩阵界定本次交付的产品、操作及排除项 | Owner 已接受 Static Assets + Access 候选；资源实现仍不得超出 M2 矩阵 | partial |
| D4 | 实际交付使用 M2 接受的 `cf` 版本 / 发布渠道、配置与 IaC 资源边界 | 固定版本、package integrity、配置/构建检查及单一写入权威记录 | not_run |
| D5 | 本地实现具备可重复测试、dry-run 与 secret hygiene | 命令 / exit code / bounded output、扫描范围与限制 | not_run |
| D6 | staging 在显式权限和预算下成功，并有可执行回滚 | 授权、部署 / 验证记录、实际费用状态、回滚演练结果 | not_run |
| D7 | production 交付符合指定 hostname / 安全 / 可用性要求并由 Owner 接受 | 具体生产变更批准、端到端证据、Owner acceptance、回滚与运维交接 | not_run |
| D8 | 每项纳入自动化的 Cloudflare 能力都有独立 owner、scope、permission、cost、test 和停止条件 | 已批准 capability register；未选功能明确标为 out-of-scope | not_run |

D1-D8 全部按证据逐项判定；本 Motion 不承诺任意账户中“所有 Cloudflare 产品均已部署”。Cloudflare capability matrix 是本次 Motion 的审计输出，不授予资源使用权。

## Landing、Consumer Audit 与回滚

获批执行后，交付物、命令结果、权限 / 成本、变更 diff、测试、失败与回滚证据归 `Mission/evidence/`；Owner 决定和结果归 `Mission/Audit/`。EGO/DNS landing 由 M1 管理；本 Motion 只更新经批准的 Repo 实现与交付证据，不改 EGO。完成后对照 M1 的 EGO/DNS 决定做 consumer audit，记录 History Triage Result，Owner 决定 source retirement。

在生产切换前保存经审阅的 DNS / 路由与 IaC 状态快照，逐 hostname / 产品定义前滚、回滚和健康判据。Owner 批准本 Motion 不等于授权任何具体前滚或回滚命令；回滚不得依赖未验证的 Cloudflare CLI 命令，可能删除数据、影响第三方或产生额外费用的动作仍须针对具体操作另行批准。

## Owner 待裁定

- `teamsbook.org` 的 registrar / nameserver、控制主体与 Cloudflare Zone 所属账号；hostname `rem.teamsbook.org` 已选，但控制权和可实施性仍待核验。
- Owner 选择全域 `@TeraTeams.com` verified-email allow；需核验该域属于目标组织且 Entra claim 匹配。REM 方法介绍草稿已接受用于 staging-preview 准备，但尚未 HTML/build；如需扩写或改动源于现有 EGO/Mission 之外的规则，另行授权并经 owning Mission 审阅。
- Owner reports Zone/control 与 Free entitlement confirmed，但尚无独立 account observation；补充可回查、非凭据证据。若 Free-only 不能满足即 Blocked，不切 Pro。
- CI 是否纳入、staging hostname/route、日志与数据保留要求、生产验收责任人及回滚方案。
- Cloudflare account 登录标识仍为 requester 声明，未由 Owner 在 Cloudflare 控制台验证。

## 技术依据

- [Introducing cf: the agentic CLI for the entire Cloudflare API](https://blog.cloudflare.com/cloudflare-cf-cli-launch/)：2026-09-28 公告称 `cf` 在 open beta、面向 3,000+ API operations、JSON 默认输出并提供 Agent 命令发现；同文说明类型化配置路线的当前范围及 Wrangler 委托边界。
- [Wrangler](https://developers.cloudflare.com/workers/wrangler/)：只作为 `cf` 对特定 JavaScript / Rust / Python Worker 路径委托时的兼容工具，不再作为本 Motion 的 Cloudflare API 主 CLI。
- [Cloudflare Terraform provider](https://developers.cloudflare.com/terraform/)：仅在选定资源确需 Terraform state / plan 管理且 provider 适用时评估。

资料查阅日期：2026-09-30。实施前须重新核实官方文档、产品可用性、当前稳定版本、权限与定价。Motion 保持 Draft，须经 Owner 明确批准后方可执行。
