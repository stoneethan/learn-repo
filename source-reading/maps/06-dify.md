# 源码地图 6：Dify

> 状态：未开始
> 使用模板：[source-map.md](../templates/source-map.md)
> 学习周次：W11

## 锁定身份

- 仓库：[langgenius/dify](https://github.com/langgenius/dify)
- Tag：`1.18.0`
- Commit：[`50abea97062110044f15d0e03ccecadd9ccc87ca`](https://github.com/langgenius/dify/tree/50abea97062110044f15d0e03ccecadd9ccc87ca)
- 许可证：以该 Commit 中的 `LICENSE` 为准
- 本地目录：`repos/dify/`
- 执行方式：静态精读；不启动整套 Docker

## 预备阅读入口

- Service API 对话入口：`api/controllers/service_api/app/completion.py`
- Chat 应用生成器：`api/core/app/apps/chat/app_generator.py`
- Chat 应用运行器：`api/core/app/apps/chat/app_runner.py`
- Agent 运行器：`api/core/agent/base_agent_runner.py`
- 数据集检索：`api/core/rag/retrieval/dataset_retrieval.py`
- 数据源检索服务：`api/core/rag/datasource/retrieval_service.py`
- 向量后端工厂：`api/core/rag/datasource/vdb/vector_factory.py`

## 待学习者完成

### 系统分层

| 层 | 责任 | 代表文件 | 暂不读区域 |
|---|---|---|---|
| Controller / API | <待填写> | <待填写> | <待填写> |
| App orchestration | <待填写> | <待填写> | <待填写> |
| RAG | <待填写> | <待填写> | <待填写> |
| Model / plugin | <待填写> | <待填写> | <待填写> |
| Storage / queue | <待填写> | <待填写> | <待填写> |

### 一条 Chat/RAG 请求

| 顺序 | 文件与符号 | 输入 | 输出/下一步 | 证据 |
|---|---|---|---|---|
| 1 | <待填写> | <待填写> | <待填写> | <待填写> |

### 检索链路

- 查询如何构造：
- 向量/关键词后端如何选择：
- 检索结果如何进入 Prompt：
- 引用与错误如何返回：

### 边界与风险

- 为什么不能只读一个 Controller：
- 哪些代码明确不读：
- 多租户/权限相关风险：
- 插件或模型适配器扩展点：

### 可选的小范围验证

- 测试/静态检查命令：
- 预期：
- 实际：
- 若环境不可用，记录原因而不是假装通过：

## 通过条件

- [ ] 能画出 API → Service/App → RAG → Model 的分层图。
- [ ] 能追通一条 Chat/RAG 请求，不停在接口名。
- [ ] 能说明三个扩展点和至少两个失败边界。
- [ ] W11 阶段测验至少 4/5。
