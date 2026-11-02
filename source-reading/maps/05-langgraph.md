# 源码地图 5：LangGraph

> 状态：未开始
> 使用模板：[source-map.md](../templates/source-map.md)
> 学习周次：W10

## 锁定身份

- 仓库：[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- Release：`1.2.19`
- Commit：[`5bd231cbfd913e05ebc662f519eb9a655bc766df`](https://github.com/langchain-ai/langgraph/tree/5bd231cbfd913e05ebc662f519eb9a655bc766df)
- 许可证：MIT
- 本地目录：`repos/langgraph/`

## 预备阅读入口

- `libs/langgraph/langgraph/graph/state.py`
- `libs/langgraph/langgraph/graph/_node.py`
- `libs/langgraph/langgraph/pregel/_algo.py`
- `libs/langgraph/langgraph/pregel/_loop.py`
- `libs/langgraph/langgraph/pregel/_checkpoint.py`
- `libs/langgraph/tests/test_algo.py`
- `libs/langgraph/tests/test_pregel.py`

## 待学习者完成

### 四个核心词

| 概念 | 一句话解释 | 代码位置 | 常见误解 |
|---|---|---|---|
| State | <待填写> | <待填写> | <待填写> |
| Node | <待填写> | <待填写> | <待填写> |
| Edge | <待填写> | <待填写> | <待填写> |
| Super-step | <待填写> | <待填写> | <待填写> |

### 最小状态图

- 输入：
- 节点 1：
- 节点 2：
- 节点 3：
- 预期最终状态：
- 实际最终状态：

### 执行调用链

| 顺序 | 文件与符号 | 输入 | 输出/下一步 | 证据 |
|---|---|---|---|---|
| 1 | <待填写> | <待填写> | <待填写> | <待填写> |

### Checkpoint

- 保存什么：
- 何时保存：
- 如何恢复：
- 失败与重放风险：

### 扩展点与代价

| 扩展点 | 用途 | 代价/风险 |
|---|---|---|
| <待填写> | <待填写> | <待填写> |

## 通过条件

- [ ] 能用自己的话解释 State/Node/Edge/Super-step。
- [ ] 能运行一个三节点状态图并解释合并结果。
- [ ] 能说明 Checkpoint 的价值与重放风险。
- [ ] 5 道自测至少答对 4 道。
