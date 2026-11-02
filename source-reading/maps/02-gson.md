# 源码地图 2：Gson

> 状态：未开始
> 使用模板：[source-map.md](../templates/source-map.md)
> 学习周次：W4–W5

## 锁定身份

- 仓库：[google/gson](https://github.com/google/gson)
- Tag：`gson-parent-2.15.0`
- Commit：[`fcd416909db2bea96eb916bcfb2d0a83cb9b86c3`](https://github.com/google/gson/tree/fcd416909db2bea96eb916bcfb2d0a83cb9b86c3)
- 许可证：Apache-2.0
- 本地目录：`repos/gson/`

## 预备阅读入口

- 公共门面：`gson/src/main/java/com/google/gson/Gson.java`
- 构建器：`gson/src/main/java/com/google/gson/GsonBuilder.java`
- 适配器抽象：`gson/src/main/java/com/google/gson/TypeAdapter.java`
- 适配器工厂：`gson/src/main/java/com/google/gson/TypeAdapterFactory.java`
- 反射绑定：`gson/src/main/java/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java`
- 默认适配器：`gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java`
- 功能测试：`gson/src/test/java/com/google/gson/functional/`

## 待学习者完成

### 一句话定位

<待填写>

### `fromJson` 解析链

| 顺序 | 文件与符号 | 输入 | 输出/下一步 | 证据 |
|---|---|---|---|---|
| 1 | <待填写> | <待填写> | <待填写> | <待填写> |

### AdapterFactory 优先级

| 工厂/适配器 | 何时命中 | 为什么排在这里 | 证据 |
|---|---|---|---|
| <待填写> | <待填写> | <待填写> | <待填写> |

### 自定义 TypeAdapter 实验

- 实验路径：`source-reading/labs/java/`
- 预测：
- 实际结果：
- 结论与代价：

### 扩展点

| 扩展点 | 使用场景 | 风险 |
|---|---|---|
| <待填写> | <待填写> | <待填写> |

## 通过条件

- [ ] 能画出类型描述 → 工厂选择 → Adapter → 对象/JSON 的链路。
- [ ] 能解释反射适配器与自定义适配器谁优先，并用实验证明。
- [ ] 定向测试通过。
- [ ] 5 道自测至少答对 4 道。
