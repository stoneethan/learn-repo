# 源码地图 3：Spring Framework

> 状态：未开始
> 使用模板：[source-map.md](../templates/source-map.md)
> 学习周次：W6–W7

## 锁定身份

- 仓库：[spring-projects/spring-framework](https://github.com/spring-projects/spring-framework)
- Tag：`v7.0.10`
- Commit：[`33a85b0bec67adb759aa898e3b80d603786be082`](https://github.com/spring-projects/spring-framework/tree/33a85b0bec67adb759aa898e3b80d603786be082)
- 许可证：Apache-2.0
- 本地目录：`repos/spring-framework/`

## 预备阅读入口

### IoC

- `spring-context/src/main/java/org/springframework/context/annotation/AnnotationConfigApplicationContext.java`
- `spring-beans/src/main/java/org/springframework/beans/factory/support/AbstractBeanFactory.java`
- `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`
- `spring-beans/src/main/java/org/springframework/beans/factory/support/AbstractAutowireCapableBeanFactory.java`

### MVC

- `spring-webmvc/src/main/java/org/springframework/web/servlet/DispatcherServlet.java`
- `spring-webmvc/src/main/java/org/springframework/web/servlet/mvc/method/annotation/RequestMappingHandlerMapping.java`
- `spring-webmvc/src/main/java/org/springframework/web/servlet/mvc/method/annotation/RequestMappingHandlerAdapter.java`

## 待学习者完成

### IoC 调用图

| 顺序 | 文件与符号 | 输入 | 输出/下一步 | 证据 |
|---|---|---|---|---|
| 1 | <待填写> | <待填写> | <待填写> | <待填写> |

### MVC 请求图

| 顺序 | 文件与符号 | 输入 | 输出/下一步 | 证据 |
|---|---|---|---|---|
| 1 | <待填写> | <待填写> | <待填写> | <待填写> |

### 核心接口

| 接口 | 责任 | 默认实现 | 扩展方式 |
|---|---|---|---|
| <待填写> | <待填写> | <待填写> | <待填写> |

### 定向测试

- 命令：
- 预期：
- 实际：
- 测试保护的行为：

### 设计取舍

- 为什么需要 BeanDefinition：
- 为什么 Controller 不直接处理 HTTP：
- 当前仍未理解：

## 通过条件

- [ ] 能解释容器刷新与按需获取 Bean 的区别。
- [ ] 能从 `DispatcherServlet` 追到 `OwnerController`。
- [ ] 能指出至少三个可替换扩展点。
- [ ] W7 阶段测验至少 4/5。
