# Vibe Engineering Cybernetics

一个受《工程控制论》思想启发的 AI Coding Agent 执行治理规范。

本仓库不是提示词合集，也不是单纯的 `AGENTS.md` 模板。它尝试把工程控制论中的系统、约束、状态、反馈、稳定性等思想，转译成一套轻量级的 AI 编程代理执行协议，用于约束和指导 Codex、OpenCode、Claude Code、Cursor 等非确定性 coding agent 在真实代码仓库中的行为。

## 这个仓库是干什么的

现代 AI coding agent 很强，但也容易出现一些典型问题：

- 忘记项目约束
- 擅自扩大修改范围
- 过度重构
- 忽略用户已有改动
- 缺少验证和复盘
- 把重要假设藏在上下文里

本项目的目标是提供一个轻量级治理运行时，让 agent 在执行任务时遵循更稳定的闭环：

```text
读取入口
  -> 任务分类
  -> 风险评估
  -> 加载对应规则
  -> 执行工作流
  -> 检查与验证
  -> 必要时更新显式状态
```

换句话说，它希望让 AI agent 不只是“看到需求就动手”，而是先判断任务类型和风险，再选择合适的执行强度。

## 核心定位

本项目受工程控制论启发，但不是数学控制系统实现。

它不会追求传递函数、状态方程、严格稳定性证明等数学形式化目标。v1 的目标更务实：

- 思想上对齐工程控制论
- 工程上提供可复制的治理目录
- 使用 `AGENTS.md`、`.ai/`、文档和脚本约束 agent 行为
- 用 validator 做基础结构校验
- 后续逐步发展 CLI、MCP、CI 等工具链

简短地说：

```text
Engineering Cybernetics as inspiration
AI agent governance as implementation target
lightweight execution discipline as v1 scope
```

## 适用对象

本仓库面向：

- OpenAI Codex
- OpenCode
- Claude Code
- Cursor
- Gemini CLI
- 未来支持仓库级指令的 coding agent

你可以把它作为一个项目级治理模板，复制到自己的代码仓库中，让不同 agent 在同一套规则下工作。

## 目录结构

```text
.
├── AGENTS.md
├── .ai/
│   ├── constitution/      # 稳定原则和长期理念
│   ├── invariants/        # 不应违反的核心不变量
│   ├── policies/          # 可结构化解析的执行约束
│   ├── runtime/           # 持续执行和上下文恢复控制
│   ├── router/            # 任务分类、风险评估、加载规则
│   ├── workflows/         # 不同任务类型的执行闭环
│   ├── skills/            # 可复用操作过程
│   ├── checklists/        # 完成前检查清单
│   ├── evaluation/        # 执行质量和治理合规评估
│   ├── state/             # 显式运行时状态
│   ├── adapters/          # Codex/OpenCode/Claude Code/Cursor 适配说明
│   └── index.md           # 给 agent 读取的治理地图
├── docs/
│   └── runtime/
│       └── agent_execution_protocol.md
├── tools/
│   └── validate_runtime.py
├── references/
│   └── engineering-cybernetics/
└── ai_governance_runtime_overview_manifest.md
```

## 快速使用

当前最简单的使用方式是：

1. 将本仓库中的 `AGENTS.md`、`.ai/`、`docs/runtime/agent_execution_protocol.md`、`tools/` 复制到目标项目根目录。
2. 根据目标项目实际情况，微调 `AGENTS.md`。
3. 让 coding agent 从 `AGENTS.md` 开始读取项目规则。
4. 运行校验器确认治理结构没有断链。

```bash
python tools/validate_runtime.py
```

CI 或发布流程中可以使用更严格的形式：

```bash
python tools/validate_runtime.py --warnings-as-errors
```

## Agent 应该如何执行

Agent 的默认加载顺序在 `AGENTS.md` 中定义：

1. 读取 `.ai/README.md`
2. 读取 `.ai/index.md`
3. 读取 `.ai/constitution/core.md`
4. 读取 `.ai/invariants/core.md`
5. 使用 `.ai/router/task_classification.md` 分类任务
6. 使用 `.ai/router/risk_levels.md` 和 `.ai/router/disturbance_model.md` 评估风险
7. 对长任务、多轮任务或中断恢复任务读取 `.ai/runtime/continuity.md`
8. 使用 `.ai/router/loading_rules.md` 加载对应 policies、workflows、skills、checklists 和 state

更完整的共享执行协议见：

- `docs/runtime/agent_execution_protocol.md`

## 当前能力

目前仓库已经包含：

- 项目入口 `AGENTS.md`
- 分层治理目录 `.ai/`
- 文档、功能开发、bugfix、重构、审阅、发布等 workflow
- Codex、OpenCode、Claude Code、Cursor adapter
- checklist 和 evaluation 输出格式
- 目标满足度和质量准则检查
- 显式 state 文件说明
- 无依赖 Python validator

## 当前边界

这个项目目前仍是 v1 雏形，重点是轻量治理规范。

它暂时不是：

- 完整 agent runtime
- 自动执行框架
- 严格数学控制系统
- 可证明稳定性的形式化系统
- 完整 CLI/MCP 产品

后续可以继续演进：

- Python CLI
- MCP server
- GitHub Actions 自动打包 Release
- 示例任务 examples
- 更强的 validator
- 针对不同 agent 的安装指南

## Release 包

仓库包含 GitHub Actions 自动发布流程。push 到 `master` 后会运行 validator，并打包一个可复制到其他项目根目录的 zip。

Release 包说明见：

- `docs/runtime/release_package.md`

## 参考材料

`references/engineering-cybernetics/` 中保存了《工程控制论》相关参考资料。

这些资料作为思想背景存在，项目治理定义应以 `.ai/`、`AGENTS.md` 和 `docs/` 中的内容为准。

## License

MIT
