# W7：Spring MVC 请求链与阶段验收

> 预计用时：4–6 小时，分两次
> 固定版本：Spring Framework `v7.0.10`
> 周分支：`study/w07-spring-mvc-gate`

## 本周目标

- 理解 `DispatcherServlet` 是请求分派器，不是 Controller 本身。
- 追通 URL → HandlerMapping → HandlerAdapter → Controller → 返回值处理。
- 将 W1–W3 的 PetClinic 经验与框架源码连接起来。
- 完成第三份源码地图与 Java 库/框架阶段验收。

## 会话 A：MVC 主链路

### 1. 先预测

浏览器请求 `/owners?lastName=Franklin` 后，预测：

- 哪个 Servlet 接收请求？
- 它直接调用 `OwnerController`，还是先查询 Handler？
- Handler 是什么类型？
- 谁负责真正调用 Controller 参数和返回值处理？
- 页面模板在哪一步被选中？

### 2. 阅读路径

- `spring-webmvc/src/main/java/org/springframework/web/servlet/DispatcherServlet.java`
- `spring-webmvc/src/main/java/org/springframework/web/servlet/mvc/method/annotation/RequestMappingHandlerMapping.java`
- `spring-webmvc/src/main/java/org/springframework/web/servlet/mvc/method/annotation/RequestMappingHandlerAdapter.java`
- `spring-webmvc/src/main/java/org/springframework/web/servlet/HandlerMapping.java`
- `spring-webmvc/src/main/java/org/springframework/web/servlet/HandlerAdapter.java`

重点看：

- `doDispatch` 的职责分派。
- `getHandler` 的决策。
- `handle` 的调用。
- 返回 `ModelAndView` 或视图名后的处理。

### 3. 定向测试

```powershell
Set-Location repos/spring-framework
.\gradlew.bat :spring-webmvc:test --tests "*DispatcherServlet*"
```

记录实际测试数、失败和耗时。若测试过多，可选择一个与 Handler 分派直接相关的方法，但不能把模块编译当作行为测试。

## 会话 B：连接框架与业务项目

### 4. 双项目对照

| PetClinic 节点 | Spring Framework 责任 | 证据 |
|---|---|---|
| `/owners` 路由 | <待填写> | <待填写> |
| `OwnerController` | <待填写> | <待填写> |
| `owners/ownersList` | <待填写> | <待填写> |

回答：

- PetClinic 为什么看起来没有 `DispatcherServlet` 代码？
- Spring Boot 的自动配置和嵌入式服务器在哪些位置把框架能力接起来？
- 如果替换消息转换器或参数解析器，应该扩展哪个点？

### 5. 完成三张内部图

在源码地图中至少保存：

- IoC 生命周期图。
- MVC 请求生命周期图。
- 核心扩展点表。

旗舰图的最终定稿可以到 W12，但 W7 必须有可讲解版本。

### 6. Java 库/框架阶段测验

每题 1 分，至少 4/5。

1. Gson 的 AdapterFactory 与 Spring 的 HandlerMapping 有什么共同的“选择后分派”模式？
2. 为什么框架通常先定义接口，再在运行时选择实现？
3. `DispatcherServlet` 为什么不应该包含业务逻辑？
4. 从 Bean 生命周期看，Controller 是如何成为可调用 Bean 的？
5. 选 Gson 和 Spring Framework 各一个扩展点，说明扩展后的收益与风险。

<details>
<summary>参考要点</summary>

1. 两者都根据输入元数据选择处理者，把变化隔离在注册/工厂机制中。
2. 接口稳定调用边界，运行时实现支持替换、测试和多策略。
3. 它的职责是前端控制器与分派，业务逻辑放在 Controller/Service 层更易复用和测试。
4. 扫描/配置产生 BeanDefinition，容器实例化并注入依赖，MVC 再注册其 Handler 信息。
5. 示例：自定义 Gson Adapter 提升兼容性但增加维护成本；MVC 参数解析器扩展可统一协议处理，但顺序和异常传播更复杂。

</details>

## 必交产出

- [ ] Spring MVC 请求链的证据表。
- [ ] Spring 与 PetClinic 对照表。
- [ ] 完整的 [Spring Framework 源码地图](../maps/03-spring-framework.md)。
- [ ] 5 题阶段测验，至少 4/5。
- [ ] 创建阶段 PR，并附定向测试与课程检查结果。

## 自测

本阶段测验即最终自测，分数：__/5。

## 过关标准

- 能脱稿说明 `DispatcherServlet` 与 `HandlerMapping`、`HandlerAdapter` 的分工。
- 能连接 PetClinic 的 Controller 到框架分派链。
- 至少答对 4/5。
- PR 中没有上游源码副本或构建产物。
