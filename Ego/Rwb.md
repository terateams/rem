# rem RWB（Rem Workbench）

> **Player**: yangjun / bitguts
> **Status**: draft
> **Version**: 0.1.0
> **Freshness**: 2026-10-05

**Reader**: Player（商务人士与 Human 参与者）。SI Agent 平时读 [AGENTS.md](../AGENTS.md)。

RWB = Rem Workbench，中文名 RW底座。它是 REM 的工作台：以操作系统为基础，由 VS Code 加若干 CLI 组成，业务对象是 REM 仓库。RWB 说明底座是什么。SI 怎么行动由 [RAP](RAP.md) 与 `AGENTS.md` 规定。

RWB 不是 REM 的第四组成部分，不是指令文件，不赋权，不替代 Mission / EVAL。

## 分层（Layers）

| 层 | 内容 | 来源 |
|---|---|---|
| 操作系统 | RWB 的基础：文件、窗口、进程。 | Player，2026-10-05 |
| RWB | VS Code 加若干 CLI。 | Player，2026-10-05 |
| SI | Copilot、Codex，在 VS Code 内使用。Claude Code 暂不在工作台内。 | Player，REM 工作台说明；Codex 版本见 [RAP](RAP.md) 规则 6 |
| 业务对象 | REM 仓库 `terateams/rem`。 | Player，2026-10-05 |

## 接入顺序（Access order）

1. CLI。
2. MCP。
3. computer use。

computer use 是兜底。RWB 要兼容它。

| 来源 |
|---|
| Player，2026-10-05 16:16 |

## 基线（Baselines）

目标版本数据出自 2026-10-05 的网页调查。本次 SI 在 macOS 27.0.1 arm64 实测 `uv 0.12.14`，低于目标 `0.12.23`；`uv run python --version` 返回 Python 3.14.4。该结果只描述本机，不代表其他设备。

| # | 基线 | 来源 |
|---|---|---|
| 1 | bash 与 PowerShell 7 并存，按系统分工：Mac、Linux、WSL2 用 bash 一系，Windows 原生用 PowerShell 7。 | Player 给出两个基线（2026-10-05 18:15）。分工与主流做法一致：[GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) 在 Linux、macOS 用 bash，在 Windows 用 pwsh；[VS Code](https://code.visualstudio.com/docs/terminal/profiles) 在 Linux、macOS 默认用 `$SHELL`，在 Windows 默认用 PowerShell |
| 2 | shell 里只写调用（npx、uvx、CLI 子命令）。有逻辑的部分用 Node 或 Python 写。不为同一件事写 `.sh` 与 `.ps1` 两份。 | Player，2026-10-05 18:39：据 SI 的调查更新 |
| 3 | bash 取 Ubuntu LTS 附带的 bash 5.x。Mac 不要求另装 bash，命令限于 bash 与 zsh 通用的写法。 | Player，2026-10-05 18:39。macOS 自带 bash 3.2.57（[说明](https://jmmv.dev/2019/11/macos-bash-baggage.html)，写于 2019 年；SI 未核实 macOS 最新版） |
| 4 | PowerShell 取 7.6 LTS。Windows 自带的 5.1 不在基线内。 | Player，2026-10-05 18:39。7.6 于 2026-03-18 发布，支持到 2028-11-14：[微软](https://learn.microsoft.com/en-us/powershell/scripting/install/powershell-support-lifecycle)。5.1 的说明：SI 判断 |
| 5 | Linux 取 WSL2 上的 Ubuntu LTS，当前为 26.04。在管理员 PowerShell 里运行 `wsl --install` 默认安装 Ubuntu，之后重启。要求 Windows 10 2004 以上或 Windows 11。 | Player 给出基线（2026-10-05 18:15）。[Ubuntu](https://ubuntu.com/wsl/docs/latest/reference/distributions/)、[微软](https://learn.microsoft.com/en-us/windows/wsl/install) |
| 6 | Node.js 取 LTS。当前是 Node 26：2026 年 10 月进入 LTS，支持到 2029 年 4 月。从 Node 27 起每年一个主版本，且都成为 LTS。 | Player，2026-10-05 18:39。[Node.js](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule) |
| 7 | uv 取最新稳定版（0.12.23，2026-10-03）。Python 由 uv 安装并在项目里钉住，暂取 3.14。 | Player，2026-10-05 18:39。[uv](https://pypi.org/project/uv/)、[Python 下载页](https://www.python.org/downloads/) |
| 8 | 不考虑 Warp。 | Player，2026-10-05 18:39 |

## CLI 规则（CLI rules）

| # | 规则 | 来源 |
|---|---|---|
| 1 | CLI 按需安装，用后移除。必要的才长期保留。 | Player，2026-10-05 16:20 |
| 2 | 安装任何 CLI 都须 Player 批准，包括 npx、uvx 的临时调用。 | Player，2026-10-05 20:09 |
| 3 | 运行器调用须钉版本，不用 latest。 | [M2 决定](../Repo/days/2026-10-01/Motion/motion-cf-cli-stack-decision-2026-09-30.md)：不在生产路径浮动安装 latest |
| 4 | 每次安装与移除是 Tools 动作，按 [AGENTS.md](../AGENTS.md) 工作方法第 4 条留证。 | `AGENTS.md` |
| 5 | 保留的 CLI 登记在 [Tools](Tools.md)：名称、用途、来源、安装方式、保留理由。未登记的视为用后即删。登记表另行落地。 | SI 建议，待 Player 确认 |
| 6 | 仓库自有 Python 脚本统一使用 `uv run python ...`；根目录 `.python-version` 固定 Python 3.14。 | Player 当前对话选择 D3 |

单条 CLI 的判断顺序（SI 建议，待 Player 确认；每一步都先取得 Player 批准）：

1. 有 npm 包或 Python 包：用 npx 或 uvx 这类运行器，不安装。
2. 有三系统通用的单文件程序：下载到临时位置，用后删除。
3. 只有系统包管理器版本（macOS 的 Homebrew、Windows 的 winget、Ubuntu 的 apt）：安装，用后卸载。
4. 以上都不行：另行讨论，不预设容器方案。

## 已知与待定的 CLI（Known CLIs）

| CLI | 状态 | 来源 |
|---|---|---|
| `cf@1.0.0-beta.9` | 管理 Cloudflare 资源。已定。 | [M2 决定](../Repo/days/2026-10-01/Motion/motion-cf-cli-stack-decision-2026-09-30.md)；版本与执行由 Player 报告，SI 未独立核实 |
| `wrangler@4.145.0` | 上传页面。已定。 | 同上 |
| PDF 的 CLI | 待定，可能包括 Pandoc。Pandoc 是独立程序，按判断顺序走系统包管理器。生成 PDF 还要另装 PDF 引擎，引擎待定。 | Player，2026-10-05 20:09；引擎一项：SI 判断 |

## 边界（Boundary）

- RWB 不规定 SI 的行为规则。规则的源头是 [RAP](RAP.md)，SI 读 `AGENTS.md`。
- 不新增第二个指令文件。
- REM 服务商务人士，不是程序员。（Player）
- Warp 与 Claude Code 不在 RWB 内。（Player）

## 待定（Open）

- “CLI 使用”的含义：Player 与 SI 都从命令行进入，还是只指 SI 通过命令行操作。
- 各 CLI 是否另有 MCP 入口。
- PDF 的 CLI 与 PDF 引擎。
- 本机 `uv 0.12.14` 低于目标 `0.12.23`；是否升级仍须 Player 批准。
- Python 3.15：原定 2026-10-01 发布，python.org 下载页尚未列出，SI 无法确认是否已发布。发布并过首个修订版后再决定是否升级基线。
- macOS 最新版自带的 bash 版本未核实。这不影响基线 3，因为基线不依赖 Mac 的 bash 版本。
