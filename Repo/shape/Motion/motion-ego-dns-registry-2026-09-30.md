# Motion: EGO DNS 目标域登记

> **Date**: 2026-09-30
> **Owner**: yangjun / bitguts
> **Status**: Executed
> **Owner Approval**: [M1-M3 approval audit](../../../Mission/Audit/2026-09-30-cloudflare-motion-approval.md)
> **Type**: EGO authority / DNS identity
> **Service Object**: rem EGO DNS register
> **Primary Route**: [Story-rem](../../../Mission/Story-rem.md) -> [EVAL](../../../Mission/EVAL/eval-rem-v1.md)
> **Source Request**: Owner 当前会话，指定 `teamsbook.org` 为 rem 目标交付域
> **Round**: R1

本 Motion 是三阶段交付序列的第 1 阶段。Owner 已批准三份 Motion；M1 只覆盖本地 EGO/DNS 登记，不授权修改线上 DNS 或 Cloudflare 账号。M1 已执行但尚无单独 Owner acceptance，详见 [M1 Audit](../../../Mission/Audit/2026-09-30-ego-dns-registry.md) 与[审批 Audit](../../../Mission/Audit/2026-09-30-cloudflare-motion-approval.md)。

## 问题与拟议裁决

Owner 已指定 rem 的目标交付根域为 `teamsbook.org`，但 EGO 当前没有 DNS 身份登记边界。若把该值只写在 `EGO-rem.md`，未来增加其他用途或域名时，身份、域名生命周期与对外 delivery binding 会继续混在实例叙述中。

**Owner 已批准的 M1 范围：**

1. 建立 `EGO/DNS/` 作为 EGO 所拥有的 DNS 身份登记边界；它定义目标域的名称、用途、来源、责任与验证状态，不承载实时 DNS 配置或 Cloudflare 凭据。
2. 在 `EGO/DNS/teamsbook.org.md` 建立唯一 canonical record，字段至少包括：域名、EGO / service binding、用途 `External Delivery Root Domain`、Owner 决定来源、status `target / unverified`、registrar / Zone / DNS control verification=`unknown`、具体 hostname target 与独立的验证状态。Owner 后续已选择 `rem.teamsbook.org` 作为 target hostname；记录更新与未执行事项见 [M1 Audit](../../../Mission/Audit/2026-09-30-ego-dns-registry.md)。
3. 在 `EGO/DNS/README.md` 说明词义、字段规则、验证边界和单一事实来源；`EGO/EGO-rem.md` 只链接到 canonical record，不重复维护域名值。
4. Business Domain、DNS root domain、具体 hostname/URL、Cloudflare stack 与 CLI 是不同语义，不在此 Motion 中互相推导。

## 范围

**拟纳入，获批后执行：**

- 只新增上述 `EGO/DNS/` 两个 Markdown 文件，并在 `EGO/EGO-rem.md` 加入指向 canonical record 的链接。
- 将 `teamsbook.org` 记录为 Owner 指定的目标值，但明确其 control、registrar、Zone、delegation 和可用 hostname 尚未核验。
- 运行本地链接 / 结构检查，并留下真实结果。

**不纳入本 Motion 的授权：**

- 不查 Cloudflare 账号，不登录，不读取凭据或 secrets。
- 不检查或修改 nameserver、DNS records、Zone、Registrar、TLS、route 或生产流量。
- 不将 Cloudflare provider bet、`cf` CLI 版本或服务选型写成已验证事实。
- 不修改 Mission/EVAL，不发布站点，不安装工具，不创建资源。

## 执行顺序与权限

canonical record 作为第 2 阶段 Motion 的输入。M1 批准只覆盖本地 EGO/DNS 登记；M2/M3 各自的审批不消除其记录的前置条件或具体操作权限门槛。

若 Owner 更改域名，或域名控制状态有新证据，先更新本 Motion 的来源/裁决并由 Owner 确认，再改 canonical record。`target / unverified` 不自动转为 `verified`。

## EVAL

| Gate | 判据 | 必需证据 | 当前状态 |
| --- | --- | --- | --- |
| D1 | EGO/DNS 边界说明目标域登记语义与控制权边界 | README 定义 | pass |
| D2 | `teamsbook.org` 唯一记录且绑定 rem 对外交付根域 | canonical record、Owner request provenance | pass |
| D3 | 域名、hostname、Zone 与可实施性未被误写成已验证 | explicit `target / unverified` 与 unknown 状态 | pass |
| D4 | EGO-rem 只引用 canonical record，无第二份域名 SSOT | EGO-rem link，不重复声明域名值 | pass |
| D5 | 修改仅限批准文件且本地结构/链接检查通过 | `python scripts/verify.py`: structure pass, failures empty | pass |

## Landing 与回滚

获批完成后，canonical record 留在 EGO/DNS；EGO-rem 只保留其职责入口链接。若字段模型或域名决定改变，走新的 Owner decision / Motion 并修订 canonical record；不回写 Cloudflare DNS，也不据此删除或创建任何线上资源。

本 Motion 完成不代表域名所有权已验证，不代表 Cloudflare Zone 可访问，也不代表 rem 已对外交付。
