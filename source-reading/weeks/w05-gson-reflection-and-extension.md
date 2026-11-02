# W5：Gson 反射、异常与扩展

> 预计用时：4–6 小时，分两次
> 固定版本：Gson `gson-parent-2.15.0`
> 周分支：`study/w05-gson-extension`

## 本周目标

- 理解反射适配器怎样读取字段并完成对象绑定。
- 用测试和实验区分“没有字段”“字段值为 null”“类型不支持”等失败。
- 完成一个最小自定义 `TypeAdapter` 实验。
- 完成第二份源码地图，通过 W4–W5 的 Gson 周检查。

## 会话 A：反射与边界

### 1. 先预测

对一个普通 Java class：

- Gson 通过构造器创建对象，还是可能绕过构造器？
- 字段名、注解、排除策略和序列化名由哪一层决定？
- 遇到循环引用、不可访问字段或非法 JSON 时，错误在哪一层出现？

### 2. 阅读路径

按顺序阅读：

1. `gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java`
2. `gson/src/main/java/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java`
3. `gson/src/main/java/com/google/gson/internal/ReflectionAccessFilterHelper.java`
4. `gson/src/main/java/com/google/gson/stream/JsonReader.java` 的错误分支
5. 对应功能测试：`CircularReferenceTest`、`ReflectionAccessFilterTest`、`NullObjectAndFieldTest`

每次输出：

- 这个对象是否负责“选择”“创建”还是“读写”？
- 失败是返回 `null`、跳过字段，还是抛异常？
- 哪个测试证明这一点？

### 3. 定向测试

```powershell
Set-Location repos/gson
mvn -pl gson -am -Dtest=CustomTypeAdaptersTest,CustomSerializerTest,CustomDeserializerTest -Dsurefire.failIfNoSpecifiedTests=false test
```

记录实际测试数量和结果。只写“命令完成”不算通过，要确认测试确实被执行。

## 会话 B：自定义 Adapter 实验

### 4. 实验目标

在 `source-reading/labs/java/gson-adapter/` 建立最小 Maven 项目：

- 定义一个小型不可变对象。
- 默认使用 Gson 完成一次序列化和反序列化。
- 为其中一种字段写一个自定义 `TypeAdapter`。
- 用同一个 JSON 对比默认行为与自定义行为。

限制：

- 不复制 Gson 上游源码。
- 只依赖公开 Gson API。
- 至少一个测试覆盖正常输入，一个测试覆盖失败输入。

### 5. 先写验收测试

在实现前写清：

```text
Given 一份含边界值的 JSON
When 使用默认 Gson 和自定义 Gson 分别反序列化
Then 我预测两者在哪个字段上不同，为什么
```

运行测试，先观察失败，再实现最小 Adapter。

### 6. 完成源码地图

填写 [Gson 源码地图](../maps/02-gson.md)：

- `fromJson` 调用链。
- 工厂优先级。
- 反射适配器职责。
- 自定义 Adapter 实验证据。
- 至少两个扩展点及代价。

## 必交产出

- [ ] Gson 反射与异常阅读记录。
- [ ] 可运行的 `source-reading/labs/java/gson-adapter/` 最小实验。
- [ ] Adapter 实验的预测、测试、结果和结论。
- [ ] 完整的 [Gson 源码地图](../maps/02-gson.md)。
- [ ] 周测验与 Commit。

## 自测

1. 反射适配器的核心职责是什么？它不负责什么？
2. 为什么“能反序列化”不等于“对象已经通过正规构造器初始化”？
3. `JsonSerializer` / `JsonDeserializer` 比直接 `TypeAdapter` 更容易用在哪里，又牺牲了什么？
4. 为不可信 JSON 选择反射访问策略时，最重要的安全边界是什么？

<details>
<summary>参考要点</summary>

1. 它负责字段发现、命名/排除、绑定和读写调度；类型信息、工厂选择、Token 流由其他层负责。
2. Gson 可能通过对象分配机制创建实例，再写字段；构造器不变量不一定自动执行。
3. 树模型更直观、易处理结构变化，但增加中间对象和复制成本。
4. 避免让不可信输入决定任意类型实例化，使用合适的过滤/白名单或显式 DTO，并验证业务不变量。

</details>

得分：__/4

## 过关标准

- 至少答对 3/4。
- 测试与实验实际运行。
- 能解释自定义 Adapter 为什么覆盖或没有覆盖默认行为。
- 源码地图包含命令、结果和代价，不只是类名列表。
