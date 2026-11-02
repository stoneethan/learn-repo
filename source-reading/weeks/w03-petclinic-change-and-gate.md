# W3：PetClinic 真实改动与阶段验收

> 预计用时：4–6 小时，分两次
> 固定版本：PetClinic `500158f`
> 周分支：`study/w03-petclinic-gate`

## 本周目标

- 通过一个真实小改动理解“需求 → 代码 → 测试”的闭环。
- 独立复述 PetClinic 的入口、请求链、测试与扩展点。
- 完成第一份源码地图，通过 Java 项目破冰阶段测验。

## 会话 A：研究真实改动

### 1. 先不看 diff，先预测

场景：用户请求一个不存在的分页，例如 `/owners?page=0` 或 `/owners?page=999`。

先回答：

- 代码最可能在哪里判断页码越界？
- 越界后应该返回错误页、空列表，还是重定向？
- 需要修改哪些层？
- 哪个测试能证明修复？

### 2. 查看固定 Commit 的 diff

```powershell
Set-Location repos/spring-petclinic
git show --stat --oneline 500158f732419217507c7656904b8e6aa1bcc0d6
git show 500158f732419217507c7656904b8e6aa1bcc0d6 -- src/main/java/org/springframework/samples/petclinic/owner/OwnerController.java src/test/java/org/springframework/samples/petclinic/owner/OwnerControllerTests.java
```

命令解释：

- `--stat` 先看改动范围。
- 第二条只看 Owner 的代码与测试 diff。

风险与可逆性：只读命令，不修改工作区。

### 3. 验证修复

```powershell
.\mvnw.cmd -Dtest=OwnerControllerTests#processFindFormRedirectsOutOfBoundsPageToFirstPage test
```

记录：

- 测试构造了什么输入？
- 期望的 HTTP 状态是什么？
- 期望的跳转 URL 是什么？
- 这个测试为什么比只检查“没有异常”更有价值？

## 会话 B：完成源码地图与阶段验收

### 4. 完成源码地图

填写 [PetClinic 源码地图](../maps/01-spring-petclinic.md)，至少包括：

- 项目定位。
- 锁定版本和构建命令。
- 模块地图。
- `/owners` 调用链。
- 一个测试保护的边界。
- 两个扩展点：例如 Repository 实现替换、Controller/模板扩展。
- 一个仍待确认的问题。

### 5. 阶段测验

先独立回答 5 题，再展开参考要点。每题 1 分。

1. 从一个陌生 Java 项目到“能运行”，最小证据链是什么？
2. `/owners?lastName=Franklin` 从 HTTP 入口到 HTML 的 4–6 个关键跳转是什么？
3. Spring Data Repository 接口和运行时实现之间是什么关系？
4. 为什么越界分页测试要检查状态码和跳转 URL，而不只是方法返回值？
5. 为 PetClinic 新增一个只读报表入口时，你会复用哪些抽象，哪些地方需要新增？

<details>
<summary>参考要点</summary>

1. 固定版本 → 找到构建入口 → 成功构建 → 定向测试 → 找到启动入口。
2. `DispatcherServlet` → HandlerMapping → OwnerController → OwnerRepository → Page → ownersList 模板。
3. 接口声明查询契约，Spring Data 创建代理并注册为 Bean，调用时把方法语义转换为查询。
4. 状态码和 URL 是用户可观察行为；只检查字符串返回无法证明 HTTP 语义和参数保留。
5. 复用 MVC、Repository、分页和模板基础设施；新增查询契约、Controller 路由、视图模型和模板。

</details>

### 6. 脱稿复述

用 3 分钟，不看地图回答：

- 入口是什么？
- 控制流怎么走？
- 为什么这样分层？
- 至少两个扩展点及代价？

## 必交产出

- [ ] 真实 Commit 的改动摘要、测试和用户可观察行为。
- [ ] 完整的 [PetClinic 源码地图](../maps/01-spring-petclinic.md)。
- [ ] 5 题阶段测验答案与得分。
- [ ] 阶段分数至少 4/5 后，创建到 `main` 的 PR。

## 自测

本阶段测验即最终自测，分数：__/5。

## 过关标准

- 阶段测验至少 4/5。
- 源码地图没有无证据的调用关系。
- 能脱稿讲 3 分钟。
- 定向测试实际通过，或有真实失败与修复记录。
- PR 通过 `git diff --check` 和课程检查脚本。
