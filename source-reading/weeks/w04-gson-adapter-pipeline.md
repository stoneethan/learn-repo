# W4：Gson API 与适配器解析

> 预计用时：4–6 小时，分两次
> 固定版本：Gson `gson-parent-2.15.0`
> 周分支：`study/w04-gson-adapters`

## 本周目标

- 区分 Gson 公共门面、类型描述、适配器、工厂和流式读写。
- 追通 `Gson.fromJson` 如何找到具体 `TypeAdapter`。
- 理解工厂顺序会决定最终序列化行为。

## 会话 A：理解 API 分层

### 1. 先预测

给定：

```java
record Owner(long id, String name) {}
Owner owner = new Gson().fromJson(json, Owner.class);
```

不看源码，预测：

- `Gson` 直接解析每一个字段，还是把工作交给其他对象？
- JSON 字符串、JSON 树、Token 流之间是什么关系？
- 自定义 `TypeAdapter` 如何注册并参与选择？

### 2. 定向阅读

按顺序阅读：

1. `Gson.java` 中的 `fromJson` 与 Adapter 获取方法。
2. `TypeAdapter.java`。
3. `GsonBuilder.java` 中注册工厂的入口。
4. `TypeAdapterFactory.java`。
5. `TypeAdapters.java` 和 `ReflectiveTypeAdapterFactory.java` 的职责边界。

每读一跳，先输出“输入 → 决策 → 输出”，再继续。

### 3. 定向测试

```powershell
Set-Location repos/gson
mvn -pl gson -am -Dtest=GsonTest,GsonTypeAdapterTest -Dsurefire.failIfNoSpecifiedTests=false test
```

命令解释：

- `-pl gson` 只构建 Gson 模块。
- `-am` 同时构建它依赖的模块。
- `-Dtest=...` 缩小测试范围。

风险与可逆性：低风险；会下载依赖并生成 `target/`，不会修改源码。

若环境未安装全局 Maven，先记录实际问题，再用项目提供的构建入口解决；不要静默跳过测试。

## 会话 B：画出解析链

### 4. 工厂选择链

列出至少 4 个 AdapterFactory/Adapter，并回答：

- 为什么顺序很重要？
- `@JsonAdapter`、内置类型、集合、反射类型的优先级如何体现？
- 如果自定义工厂返回 `null`，下一步是什么？
- 如果它返回一个 Adapter，后面的工厂还会执行吗？

### 5. 用一个最小对象验证

构造一个最小 Java 对象与 JSON：

- 先使用默认 Gson。
- 再注册一个只改变一个字段表示法的 `TypeAdapter`。
- 比较输出和输入反序列化结果。

本实验在 W5 正式完成；W4 只需写出最小实验设计和预测。

### 6. 更新地图

填写 [Gson 源码地图](../maps/02-gson.md) 中的 API 分层、工厂优先级和第一版 `fromJson` 调用链。

## 必交产出

- [ ] Gson 分层表：门面、类型描述、工厂、Adapter、流读写。
- [ ] `Gson.fromJson` 的 4–6 跳调用链。
- [ ] 定向测试结果和证据。
- [ ] 自定义 Adapter 实验的输入、预测与预期差异。

## 自测

1. `TypeAdapterFactory` 返回 `null` 与返回 Adapter 分别意味着什么？
2. `TypeToken` 为什么比直接传 `Class<?>` 更能保留泛型信息？
3. `TypeAdapter` 与 `JsonSerializer` / `JsonDeserializer` 在数据层和性能取舍上有什么差异？
4. 为什么工厂顺序本身就是 API 行为的一部分？

<details>
<summary>参考要点</summary>

1. 返回 `null` 表示当前工厂不处理，继续询问后续工厂；返回 Adapter 表示由它接管该类型。
2. `TypeToken` 捕获编译期泛型签名，`Class` 会擦除元素类型等信息。
3. Adapter 直接处理 Token 流，通常更底层、更快；`JsonSerializer`/`JsonDeserializer` 先转成 JSON 树，写起来方便但可能多做对象转换。
4. 同一类型可由多个工厂处理，先命中者胜出；顺序改变可直接改变字段映射、兼容性或性能。

</details>

得分：__/4

## 过关标准

- 至少答对 3/4。
- 能从 `fromJson` 追到具体 Adapter 的决策点。
- 能用自己的话解释工厂返回 `null` 的含义。
