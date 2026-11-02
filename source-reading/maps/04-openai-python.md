# 源码地图 4：OpenAI Python SDK

> 状态：未开始
> 使用模板：[source-map.md](../templates/source-map.md)
> 学习周次：W9

## 锁定身份

- 仓库：[openai/openai-python](https://github.com/openai/openai-python)
- Tag：`v3.42.1`
- Commit：[`190dd5aee1053dd2093d2a5c3937f604860310a3`](https://github.com/openai/openai-python/tree/190dd5aee1053dd2093d2a5c3937f604860310a3)
- 许可证：Apache-2.0
- 本地目录：`repos/openai-python/`

## 预备阅读入口

- `src/openai/_client.py`
- `src/openai/_base_client.py`
- `src/openai/_response.py`
- `src/openai/_streaming.py`
- `src/openai/resources/responses/responses.py`
- `tests/`

## 待学习者完成

### 分层地图

| 层 | 责任 | 不负责 | 证据 |
|---|---|---|---|
| <待填写> | <待填写> | <待填写> | <待填写> |

### 一次请求的调用链

| 顺序 | 文件与符号 | 输入 | 输出/下一步 | 证据 |
|---|---|---|---|---|
| 1 | <待填写> | <待填写> | <待填写> | <待填写> |

### 流式事件

- 响应如何从字节流变成事件：
- 哪个类型暴露给调用者：
- 中途失败如何处理：

### 重试与错误

- 重试入口：
- 可重试条件：
- 幂等风险：

### 扩展点与代价

| 扩展点 | 用途 | 风险 |
|---|---|---|
| `http_client` / transport | <待填写> | <待填写> |
| 其他扩展点 | <待填写> | <待填写> |

## 安全约束

- 默认只运行测试和 Mock，不要求真实 API Key。
- 不记录或提交任何密钥。
- 若以后做真实调用，必须使用环境变量并设置费用上限。

## 通过条件

- [ ] 能区分公共资源 API、客户端层和 HTTP 传输层。
- [ ] 能说明正常响应与流式响应在类型转换上的差异。
- [ ] 能指出一个重试边界和一个幂等风险。
- [ ] 5 道自测至少答对 4 道。
