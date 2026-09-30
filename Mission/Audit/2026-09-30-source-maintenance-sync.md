# Audit - source maintenance conclusions / target constraints

> **Owner**: bitguts
> **Date**: 2026-09-30 / UTC+08:00
> **Approval Evidence**: Owner在EGO-T189当前会话批准Tier A/snapshot修复、F1/F2/F3/F5定向权威修订、保留三组快照的已落层Dojo清退，并选择“同步本次维护结论及必要工具约束，不碰另一窗口工作”。
> **Scope**: 本target记录与EGO/Tools维护约束；不更新pinnedcore、Story/EVAL/model规则，不修改EGO-rem/DNS、镜页索引或targetMotion。
> **History Triage Result**: Audit First

## 同步结论

Source Tier A implementation已与NP0 snapshot contract一致：合法`np0-runtime-{run-id}`需要ASCII alphanumeric开头、1-64字符、余位字母/数字/下划线/连字符；快照四件套regular/non-symlink、无额外内容/目录、无Dojo重定向。实际sourcegatePASS，12项测试中9PASS/3symlinkskipped；不通过删除合法snapshot制造green。

source当前methodmapping由CRAFTS S1、REM F2承接，旧RAM只history/provenance；现行consumer请求不复活retiredcapability-host。targetselected_method仍null，不复制sourceCRAFTS或source特化TierA入口清单。

SourceDojo仅清退有正式landing/correction证据且已冻结原始bytes的skill-creator Delta，其余强引用、备查资料与三组snapshot保留。targetDojo不因此获得自动删除许可，target原件/证据/30天cooldown仍按owningcustody判断。

## Published source references

- EGO-T189 authority/implementation与acceptedbootstrap证据commit=`0bacfbb7aa5884e08fd5e7609488cfe564e8c727`，已push。
- Dojo独立退出commit=`07a53bc796b8cc97f70818b113e17c4082d73802`，已push；source工作树clean，三snapshot/L365保留。唯一Delta原始4298bytes/hash已冻存，不删除历史experience。
- Source当前镜页`MPS-260930S3003-rem-instance-ego-t189.html`独立validator projection/freshness/G-ID/G-Voice/G-Distort/G-Tier=pass；Human/model/runtime仍not_run。这不是本target产品EVAL或实际双模型任务通过。
- rootCRAFTS=6.8.1、repo-consumer=2.2.1；sourcecurrentmethod轴S1/F2与九次失效引用修复，本target不复制CRAFTS。旧contract历史Git路径未直接命中，source没有猜原文/恢复兼容壳；现行请求由已声明sixfields与owningconsumerroute承接。

## 工具边界

target `verify.py` 的structure/pins PASS不是snapshot内容真实性、Human permission、modelrun或任务完成证明。保留显式files/permission/date/hash/runid与no-writeback；任何snapshot应使用自己的targetslug与quartet，不从source T189推断。generic NP0/MPS原样pins不自动跟随source代码变更；需要升级时另审pin/delta/tests，不在本次修改。

本target另一个窗口有EGO-rem、DNS、索引、Motion/镜页未提交工作；本批不覆盖/删除/暂存这些内容。只按明确路径提交本Audit与EGO/Tools两项。bootstrap R1已Done、产品真实EVAL仍in-progress，维护同步不代替Sol/Luna或Human验收。
