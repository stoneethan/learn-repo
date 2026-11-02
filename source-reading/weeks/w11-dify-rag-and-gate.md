# W11：Dify Chat/RAG 链路与阶段验收

> 预计用时：4–6 小时，分两次
> 固定版本：Dify `1.18.0`
> 周分支：`study/w11-dify-gate`
> 执行方式：静态精读 + 小范围检查，不启动整套 Docker

## 本周目标

- 在大型多语言项目中先建立分层地图，再选一条 Chat/RAG 请求。
- 追通 API → App/Service → RAG → Model 的关键边界。
- 理解大型项目为什么必须“定向精读”，而不是逐文件硬啃。
- 通过 AI 核心与编排阶段验收。

## 会话 A：建立分层地图

### 1. 先预测

一个需要知识库的聊天请求，最可能经过：

```text
HTTP Controller -> ? -> ? -> ? -> 流式响应
```

先写出你能想到的层，并标记：

- 哪层处理鉴权。
- 哪层管理会话。
- 哪层做检索。
- 哪层调用模型。
- 哪层产生流式事件。

### 2. 候选阅读区

- `api/controllers/service_api/app/completion.py`
- `api/core/app/apps/chat/app_generator.py`
- `api/core/app/apps/chat/app_runner.py`
- `api/core/agent/base_agent_runner.py`
- `api/core/rag/retrieval/dataset_retrieval.py`
- `api/core/rag/datasource/retrieval_service.py`
- `api/core/rag/datasource/vdb/vector_factory.py`
- `api/tests/unit_tests/core/rag/`

先只找入口、接口和工厂，不进入每种向量数据库的实现。

### 3. 用搜索限定范围

```powershell
Set-Location repos/dify
rg -n "class CompletionApi|def generate|retrieve|RetrievalService|Vector" api/controllers/service_api/app/completion.py api/core/app/apps/chat api/core/rag
```

命令解释：

- `rg` 搜索指定入口、接口和类名，帮助你从大目录切出最小阅读面。
- 输出是线索，不是调用链证明。

风险与可逆性：只读搜索，低风险。

## 会话 B：追一条链路

### 4. 请求链

选定“预定义 Chat App + 知识库检索”这一条路径，记录 6–8 跳：

| 顺序 | 文件与符号 | 输入 | 输出/下一步 | 证据 |
|---|---|---|---|---|
| 1 | <待填写> | <待填写> | <待填写> | <待填写> |

明确写下不读的内容，例如：

- 每种向量数据库适配器。
- 前端画布。
- 计费与权限全链路。
- 插件市场。
- 全部 Agent 策略。

### 5. 检索与生成边界

回答：

- 查询在何时被改写成检索请求？
- 向量后端由谁选择？
- 检索结果怎样进入 Prompt/上下文？
- 没有检索结果时，行为是什么？
- 模型或插件失败时，错误怎样回到流式响应？

### 6. 最小验证

优先选择：

```powershell
py -3.14 -m compileall -q api/controllers/service_api/app/completion.py api/core/rag/retrieval/dataset_retrieval.py
```

命令解释：

- 只验证这些文件能否被当前解释器解析，不证明业务行为。
- `-q` 减少成功输出。

风险与可逆性：低风险；只在被忽略的 `__pycache__/` 中生成缓存。

如果 Python 版本不满足项目依赖，跳过运行并记录原因；静态链路仍可用代码和测试作为证据。

### 7. AI 核心与编排阶段测验

至少 4/5：

1. Micrograd 的计算图和 LangGraph 的状态图有什么本质差异？
2. OpenAI SDK 中“流式输出”与 LangGraph 中“事件流/状态更新”分别解决什么问题？
3. Dify 为什么在 Controller 与 RAG 之间需要 App orchestration 层？
4. 一条 RAG 链路的三个主要失败边界是什么？
5. 选择 Dify 中一个扩展点，说明它的收益与运维代价。

<details>
<summary>参考要点</summary>

1. Micrograd 图记录可微运算并求导；LangGraph 图编排状态和执行，不要求节点可微。
2. SDK 流式输出逐步传递模型内容；图事件流还表达节点、状态和流程生命周期。
3. 它统一应用配置、会话、Prompt、检索策略、模型调用和事件输出，避免 Controller 承担业务编排。
4. 查询/检索失败、模型/插件失败、流式中断或持久化/权限错误。
5. 示例：替换向量后端提升规模能力，但带来迁移、索引一致性、监控和故障定位成本。

</details>

## 必交产出

- [ ] Dify 分层地图。
- [ ] 一条 Chat/RAG 请求的 6–8 跳链路。
- [ ] 明确的不读范围与理由。
- [ ] 小范围静态/语法验证结果或无法运行的真实原因。
- [ ] 完整的 [Dify 源码地图](../maps/06-dify.md)。
- [ ] 5 题阶段测验，至少 4/5。
- [ ] 阶段 PR。

## 自测

本阶段测验即最终自测，分数：__/5。

## 过关标准

- 至少 4/5。
- 能画出 API → App → RAG → Model 分层并说明职责。
- 能指出至少两个扩展点和失败边界。
- 不把“没有启动 Docker”写成“完整运行通过”。
