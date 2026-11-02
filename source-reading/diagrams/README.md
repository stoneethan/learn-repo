# 旗舰调用图

课程最终保留三张可独立讲解的图。图中的每个节点都必须能指回固定版本的代码或测试。

## 1. Java 请求生命周期

目标路径：

```text
Browser -> DispatcherServlet -> HandlerMapping -> HandlerAdapter
        -> OwnerController -> Repository -> View
```

完成标准：

- 标出每一跳的接口和运行时实现。
- 标出返回值和视图解析位置。
- 至少链接一个 Controller 测试和一个集成测试。

## 2. Gson 适配器解析链

目标路径：

```text
Gson.fromJson -> adapter lookup -> TypeAdapterFactory chain
              -> reflective/custom adapter -> target object
```

完成标准：

- 说明工厂优先级。
- 区分树模型、流式读取和反射字段绑定。
- 用自己的实验证明自定义适配器会覆盖默认行为。

## 3. AI Agent/RAG 执行链

目标路径：

```text
Input/State -> orchestration loop -> tool/RAG -> model
            -> event/result -> checkpoint
```

完成标准：

- 分别指出 LangGraph 的 State/Node/Edge/Pregel 与 Dify 的 API/Service/RAG 对应位置。
- 说明一次失败或重试如何传播。
- 标出人类可插手的扩展点。

## 文件约定

最终使用 Mermaid 保存为：

- `01-java-request-lifecycle.md`
- `02-gson-adapter-resolution.md`
- `03-ai-execution-chain.md`

图示必须附带文字说明，不能只放一张图。
