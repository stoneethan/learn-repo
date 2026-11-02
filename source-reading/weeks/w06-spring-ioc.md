# W6：Spring IoC 容器

> 预计用时：4–6 小时，分两次
> 固定版本：Spring Framework `v7.0.10`
> 周分支：`study/w06-spring-ioc`

## 本周目标

- 区分 BeanDefinition、BeanFactory、ApplicationContext 和具体 Bean 实例。
- 理解容器刷新与按需获取 Bean 是两条不同时间线。
- 追踪创建、属性注入和初始化回调。

## 会话 A：先建容器地图

### 1. 先预测

对：

```java
try (var context = new AnnotationConfigApplicationContext(AppConfig.class)) {
    var service = context.getBean(Service.class);
}
```

先回答：

1. `new` 时已经创建 `Service` 实例了吗？
2. `AppConfig` 先变成什么，再变成什么？
3. `getBean` 时若实例尚不存在，容器如何保证依赖可用？
4. `@Autowired` 由谁处理，发生在构造、属性赋值还是初始化前后？

### 2. 阅读路径

- `spring-context/src/main/java/org/springframework/context/annotation/AnnotationConfigApplicationContext.java`
- `spring-context/src/main/java/org/springframework/context/support/AbstractApplicationContext.java`
- `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`
- `spring-beans/src/main/java/org/springframework/beans/factory/support/AbstractBeanFactory.java`
- `spring-beans/src/main/java/org/springframework/beans/factory/support/AbstractAutowireCapableBeanFactory.java`

只追一个普通单例 Bean 的路径，不进入 AOP 自动代理、循环依赖特判、AOT 和完整事件机制。

### 3. 定向测试

```powershell
Set-Location repos/spring-framework
.\gradlew.bat :spring-context:test --tests "*AnnotationConfigApplicationContext*"
```

命令解释：

- 使用项目自带 Gradle Wrapper。
- 只运行与 Annotation 配置容器相关的测试。

风险与可逆性：低风险；会下载 Gradle/依赖并生成缓存和构建产物，不修改源码。

如果通配符没有匹配到测试，记录实际输出，改为同模块的明确测试类。不要把“零测试”当作通过。

## 会话 B：追踪一个 Bean 的生命周期

### 4. 调用链

用 5–8 跳记录：

```text
构造 ApplicationContext
-> 注册/读取 BeanDefinition
-> refresh
-> finishBeanFactoryInitialization
-> preInstantiateSingletons
-> createBean
-> instantiate / populate / initialize
```

每个箭头回答：

- 输入是什么？
- 谁负责下一步？
- 失败可能在哪里出现？

### 5. 关键接口

至少解释以下接口中的一个职责与一个常见误解：

- `BeanFactory`
- `ListableBeanFactory`
- `BeanDefinition`
- `BeanPostProcessor`
- `AutowireCapableBeanFactory`

不要只复制注释；用自己的话并链接到调用位置。

### 6. 测试证据

找一个测试，说明它保护的场景：

- 构造器注入。
- 属性注入。
- 初始化回调。
- 找不到依赖或存在多个候选者。

四选一深入即可，但必须找到具体测试方法。

## 必交产出

- [ ] W6 周笔记中的 IoC 预测与修正。
- [ ] 一个普通单例 Bean 的生命周期调用链。
- [ ] Spring 模块定向测试实际输出。
- [ ] 一个具体测试和它保护的行为。
- [ ] 更新 [Spring Framework 源码地图](../maps/03-spring-framework.md) 的 IoC 部分。

## 自测

1. BeanDefinition 和 Bean 实例有什么区别？
2. 为什么 `ApplicationContext` 常被视为增强版 `BeanFactory`？
3. 构造器注入与属性注入发生的时间点有什么不同？
4. `BeanPostProcessor` 在生命周期中的价值是什么？它带来什么风险？

<details>
<summary>参考要点</summary>

1. BeanDefinition 是创建配置/元数据，Bean 是按定义创建出的运行时对象。
2. ApplicationContext 提供 BeanFactory 能力，并增加资源、事件、国际化、生命周期等应用级能力。
3. 构造器参数在对象实例创建前解析；属性注入在对象实例创建后填充。
4. 它允许框架在初始化前后扩展或替换 Bean 行为，但处理器顺序、代理和初始化副作用会带来调试复杂度。

</details>

得分：__/4

## 过关标准

- 至少答对 3/4。
- 能画出 Container refresh 与 getBean 的时间关系。
- 调用链不把接口和实现混为一个节点。
