# W9：OpenAI Python SDK

> 预计用时：4–6 小时，分两次
> 固定版本：OpenAI Python `v3.42.1`
> 周分支：`study/w09-openai-python`

## 本周目标

- 区分资源 API、客户端、HTTP 传输、响应解析和流式事件。
- 不调用真实付费 API，也能用测试和 Mock 验证请求构造。
- 理解重试、超时、错误和流式输出各自所在层次。

## 会话 A：四层地图

### 1. 先预测

调用：

```python
client.responses.create(...)
```

先回答：

1. `client.responses` 直接发 HTTP 吗？
2. 请求在哪个层组装成 HTTP？
3. 普通响应和流式响应何时分叉？
4. 网络错误、429、解析错误分别由哪一层识别？

### 2. 阅读路径

- `src/openai/_client.py`
- `src/openai/_base_client.py`
- `src/openai/_response.py`
- `src/openai/_streaming.py`
- `src/openai/resources/responses/responses.py`
- `tests/test_client.py`
- `tests/test_response.py`
- `tests/test_streaming.py`

先只找入口和职责，不读取每个生成方法。资源类文件很大是正常的，重点是公共调用模式。

### 3. Python 环境

```powershell
Set-Location repos/openai-python
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip uv
.\.venv\Scripts\uv.exe sync --group dev
```

命令解释：

- 创建隔离虚拟环境。
- 在虚拟环境中安装 `uv`，再由它按锁文件和 dependency group 安装开发依赖。
- `sync` 会创建/更新 `.venv/`，不会修改项目源码。

风险与可逆性：

- 低风险；会下载较多依赖，删除 `.venv/` 即可恢复。
- 不要求设置 `OPENAI_API_KEY`。

## 会话 B：请求与流式事件

### 4. 定向测试

```powershell
.\.venv\Scripts\uv.exe run pytest tests/test_response.py tests/test_streaming.py -q
```

记录：

- 测试数量、耗时、失败原因。
- 哪个测试使用 Mock transport。
- 哪个测试证明流式分块被转换为事件。

若测试因 Python 3.14 兼容或可选依赖失败，记录完整错误；可切换到本机 Python 3.13，但不跳过证据。

### 5. 追一条请求

用 5–7 跳记录：

```text
resource method
-> client wrapper
-> request build
-> transport
-> response parse
-> public result
```

每一跳写：

- 文件与符号。
- 输入。
- 输出。
- 错误/重试在哪一步。

### 6. 流式与重试边界

回答：

- 流已经向调用者输出一部分后，能否安全地从头自动重试？
- 超时与 429 是否是同一类错误？
- 幂等风险由 SDK 负责还是调用者负责？
- 自定义 HTTP client 是扩展点还是业务逻辑入口？

## 必交产出

- [ ] SDK 四层职责表。
- [ ] 一次 `responses` 请求的调用链。
- [ ] `test_response.py` 与 `test_streaming.py` 的实际结果。
- [ ] 重试、流式中断和幂等风险说明。
- [ ] 完整的 [OpenAI Python 源码地图](../maps/04-openai-python.md)。

## 自测

1. 资源 API 与 `_base_client` 的职责边界是什么？
2. 普通响应和流式响应在公开返回值上有什么差异？
3. 为什么流式响应已输出部分内容后，自动重试需要特别谨慎？
4. 用自定义 HTTP transport 做测试的好处是什么？

<details>
<summary>参考要点</summary>

1. 资源 API 提供领域方法和参数/模型映射；base client 负责通用请求、传输、重试和客户端配置。
2. 普通响应一次性得到完整对象；流式响应得到可迭代事件，内容逐步产生。
3. 调用者可能已观察到部分结果，重放会重复副作用或造成重复输出。
4. 无需真实网络即可观察请求、注入错误和流分块，测试更快、更确定、无费用。

</details>

得分：__/4

## 过关标准

- 至少答对 3/4。
- 没有真实 API Key 时也能完成核心阅读和 Mock 测试。
- 能说明 SDK 的边界：它管理请求生命周期，但不替业务决定幂等语义。
