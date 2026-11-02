# W10：LangGraph 执行模型

> 预计用时：4–6 小时，分两次
> 固定版本：LangGraph `1.2.19`
> 周分支：`study/w10-langgraph`

## 本周目标

- 理解 State、Node、Edge、Super-step 与 Checkpoint 的职责。
- 追一次图执行从输入、节点调度到状态合并的路径。
- 用一个三节点状态图验证 reducer/状态更新行为。

## 会话 A：画执行模型

### 1. 先预测

给定 `A -> B -> C`：

1. 用户输入直接进入哪个节点？
2. 每个节点读取完整 State，还是只接收局部参数？
3. 两个并行节点同时更新同一个字段时会发生什么？
4. Checkpoint 是日志、缓存，还是可恢复状态？

### 2. 阅读路径

- `libs/langgraph/langgraph/graph/state.py`
- `libs/langgraph/langgraph/graph/_node.py`
- `libs/langgraph/langgraph/pregel/_algo.py`
- `libs/langgraph/langgraph/pregel/_loop.py`
- `libs/langgraph/langgraph/pregel/_checkpoint.py`
- `libs/langgraph/tests/test_algo.py`
- `libs/langgraph/tests/test_channels.py`
- `libs/langgraph/tests/test_pregel.py` 中一个最小路径测试

`test_pregel.py` 很大，先用测试名定位最小图执行场景，不要顺序读完。

### 3. Python 环境

```powershell
Set-Location repos/langgraph
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip uv
Set-Location libs/langgraph
..\..\.venv\Scripts\uv.exe sync --group dev
```

若 monorepo 的 workspace 安装入口与预期不同，记录 `pyproject.toml` 证据和实际修复命令，不把失败隐藏掉。

### 4. 定向测试

```powershell
..\..\.venv\Scripts\uv.exe run pytest tests/test_algo.py tests/test_channels.py -q
```

记录测试数量与结果。`test_pregel.py` 太大，只运行通过测试名筛出的一个场景。

## 会话 B：最小状态图实验

### 5. 实现三节点图

在 `source-reading/labs/python/langgraph-state/` 建立最小实验：

- 定义包含 `count` 与 `messages` 的 State。
- 三个节点按顺序执行。
- 至少一个节点只做确定性计算，不调用模型。
- 用事件流或执行结果验证节点顺序和最终状态。

关键编排代码由你写；环境配置和报错排查可以协作。

### 6. 执行链

记录 5–8 跳：

```text
invoke input
-> graph validation/compilation
-> task scheduling
-> node execution
-> channel/state update
-> next super-step
-> checkpoint/result
```

每跳附文件、符号和测试或运行证据。

### 7. Checkpoint 风险

回答：

- 同一输入重放是否一定安全？
- 外部工具已经执行过，恢复时怎样避免重复副作用？
- Checkpoint 能恢复状态，是否也能自动恢复外部系统的一致性？

## 必交产出

- [ ] State/Node/Edge/Super-step 四词解释与代码位置。
- [ ] 三节点状态图及其运行结果。
- [ ] 一次执行的 5–8 跳链路。
- [ ] Checkpoint 重放风险说明。
- [ ] 完整的 [LangGraph 源码地图](../maps/05-langgraph.md)。

## 自测

1. Node 与普通函数的关系是什么？
2. Edge 为什么不能简单等同于“上一行代码执行完”？
3. 并行节点更新同一状态字段时，为什么需要明确的 reducer/合并策略？
4. Checkpoint 恢复为什么不能自动保证有副作用的工具只执行一次？

<details>
<summary>参考要点</summary>

1. Node 是注册到图中的可调用执行单元，输入/输出受 State 和执行模型约束。
2. Edge 表达图的下一个路由关系，可能受条件、并行和 super-step 调度影响。
3. 并发更新需要确定、可重复的合并规则，否则结果依赖完成顺序。
4. 外部工具可能已经产生真实副作用；恢复本地状态不会回滚外部系统。

</details>

得分：__/4

## 过关标准

- 至少答对 3/4。
- 三节点图实际运行，最终状态与预测一致或有解释。
- 能区分“状态可恢复”和“副作用可回滚”。
