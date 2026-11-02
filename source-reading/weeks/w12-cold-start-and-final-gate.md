# W12：独立冷启动与最终验收

> 预计用时：4–6 小时，分两次
> 固定版本：OpenAI Agents Python `v0.24.0`
> 周分支：`practice/w12-openai-agents-cold-start`

## 本周目标

- 在不使用逐行导读的情况下，30 分钟内摸清一个陌生 Agent 项目的入口、模块和一条执行链。
- 将 OpenAI Agents Python 与 LangGraph 做有证据的设计对比。
- 完成三张旗舰图、最终测验和 Issue → 分支 → Commit → PR 演练。

## 会话 A：独立冷启动

### 1. 计时开始前

只准备：

- 固定版本源码。
- 空白的 [冷启动报告](../cold-start/openai-agents-python.md)。
- 一个 30 分钟计时器。

不要先打开课程路径提示、网络解读或 AI 答案。

### 2. 30 分钟流程

| 时间 | 动作 |
|---|---|
| 0–5 分钟 | README、许可证、构建入口、项目定位 |
| 5–10 分钟 | 目录、核心包、示例、测试入口 |
| 10–18 分钟 | 选择一个最小 Agent Run，追 3–6 跳 |
| 18–25 分钟 | 找 Tool/Handoff/Result 和至少两个扩展点 |
| 25–30 分钟 | 写下事实、推断、未知项与下一步 |

计时结束后才能请我批改。批改只指出证据缺口，不先给完整答案。

## 会话 B：对比、图和 PR

### 3. 与 LangGraph 对比

至少比较：

- 编排单位：图节点 vs Agent/Runner。
- 状态载体与持久化边界。
- Tool 与 Handoff 的扩展方式。
- 适合的场景与不适合的场景。

每个结论必须附代码或测试证据。

### 4. 定稿三张旗舰图

- Java 请求生命周期。
- Gson Adapter 解析链。
- AI Agent/RAG 执行链。

每张图附带一段 100–200 字说明，能脱稿讲 2 分钟。

### 5. 最终测验

至少 4/5：

1. 面对陌生项目，前 10 分钟你的检查顺序是什么？
2. 怎样证明一条调用关系，而不是凭类名猜？
3. Java 框架和 AI 编排框架在“选择与分派”上有什么共同模式？
4. 为什么大型项目必须先定义不读范围？
5. 你怎样判断一次源码阅读已经从“知道类名”升级为“能指导修改”？

<details>
<summary>参考要点</summary>

1. README/Release/构建入口 → 目录与示例 → 测试入口 → 一条用户路径。
2. 文件、符号、运行时注册/实现、测试或实验共同证明。
3. 都通过注册、接口和策略选择把调用者与实现解耦，例如 Factory/Mapping/Node。
4. 代码量远超可读预算；不限定路径会把时间耗在低价值分支。
5. 能预测改动影响、定位测试、说明扩展点和失败边界，并做最小实验验证。

</details>

### 6. Issue → 分支 → Commit → PR 演练

先确认目标 Issue 不存在，再执行：

```powershell
git switch main
git pull --ff-only
gh issue create --title "Complete W12 OpenAI Agents cold-start report" --body "Track the independent 30-minute source-reading exercise and its evidence."
git switch -c practice/w12-openai-agents-cold-start
```

完成报告与图后：

```powershell
git add source-reading
git commit -m "study(w12): complete openai agents cold start"
git push -u origin practice/w12-openai-agents-cold-start
gh pr create --fill
```

命令解释：

- `issue create` 建立可追踪任务。
- 分支隔离 W12 产物。
- Commit 只包含真实完成的学习证据。
- PR 将任务、变更和验收连接起来。

风险与可逆性：

- 中等外部写入风险：会创建公开 Issue、分支和 PR。
- 不会直接修改 `main`；合并前可由你复核。
- 若内容未完成，使用 PR 草稿或暂不创建，不伪造“已通过”。

## 必交产出

- [ ] [OpenAI Agents 冷启动报告](../cold-start/openai-agents-python.md)，实际用时不超过 30 分钟。
- [ ] 与 LangGraph 的设计对比。
- [ ] 三张旗舰图的 Markdown/Mermaid 版本。
- [ ] 5 题最终测验，至少 4/5。
- [ ] Issue、分支、Commit、PR 的完整链接。
- [ ] 更新 [总进度](../01-progress.md)。

## 自测

本阶段测验即最终自测，分数：__/5。

## 最终过关标准

- 独立冷启动在 30 分钟内完成，无法确认的内容明确标为未知。
- 三张图均可指向固定版本代码或测试。
- 至少答对 4/5。
- 课程检查脚本、Markdown 链接、`git diff --check` 全部通过。
- 公开仓库没有密钥、上游源码副本、虚拟环境或构建产物。
