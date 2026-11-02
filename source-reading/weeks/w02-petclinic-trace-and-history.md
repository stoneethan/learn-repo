# W2：PetClinic 请求、测试与 Git 历史

> 预计用时：4–6 小时，分两次
> 固定版本：PetClinic `500158f`
> 周分支：`study/w02-petclinic-trace`

## 本周目标

- 追通 `/owners` 的一次查询与页面渲染。
- 用测试确认输入、输出和边界，而不是凭方法名猜测。
- 用 `git log`、`git blame`、Commit 和 Issue/PR 理解一次真实改动。
- 把 W1 的路径预测修正为有证据的调用链。

## 会话 A：请求与测试

### 1. 先预测两条路径

分别预测：

- `GET /owners` 不带筛选条件。
- `GET /owners?lastName=Franklin` 带筛选条件。

两者会在哪一步分叉？最后返回视图还是 JSON？

### 2. 追代码

阅读顺序：

1. `OwnerController#processFindForm`
2. `OwnerRepository` 中按姓氏分页的方法
3. `ownersList.html`
4. `OwnerControllerTests` 中与 `processFindForm` 相关的方法
5. `ClinicServiceTests` 中与 Owner Repository 相关的方法

每个跳转记录：

```text
文件 + 方法 + 输入 + 输出 + 证据
```

注意：`OwnerRepository` 是接口。继续查 Spring Data 在运行时如何提供实现，不要把“接口没有实现类”当成调用链终点。

### 3. 定向测试

```powershell
Set-Location repos/spring-petclinic
.\mvnw.cmd -Dtest=OwnerControllerTests,ClinicServiceTests test
```

风险与可逆性：低风险；只创建/更新构建产物和测试缓存。

记录：

- 运行了多少个测试？
- 哪个测试直接覆盖按姓氏查询？
- 哪个测试覆盖空结果或分页边界？

## 会话 B：Git 历史与 Issue

### 4. 查看文件演化

```powershell
git log --oneline -- src/main/java/org/springframework/samples/petclinic/owner/OwnerController.java
git blame -L 85,135 -- src/main/java/org/springframework/samples/petclinic/owner/OwnerController.java
```

命令解释：

- `git log -- <path>` 只看影响该文件的提交。
- `git blame -L` 查看指定行的最后修改 Commit。

风险与可逆性：只读命令，不修改工作区。

### 5. 追一条设计动机

从你看到的最新相关 Commit 出发，回答：

- 改了什么行为？
- 新增或修改了哪个测试？
- Commit 信息说明了什么？
- 如果找不到 Issue/PR，明确写“未找到”，并说明检索词。

不要从作者身份或代码风格推断动机；优先使用提交信息、测试和关联讨论。

### 6. 修正调用链

把 W1 的预测改成 4–6 行有证据的链路。必须包含：

- HTTP 映射。
- Controller 方法。
- Repository 查询。
- 分页结果。
- 模板或错误结果。

## 必交产出

- [ ] W2 周笔记，包含两条请求的预测与修正。
- [ ] `OwnerControllerTests`、`ClinicServiceTests` 的实际结果。
- [ ] 一段 `git log`/`git blame` 证据及设计动机结论。
- [ ] 更新 [PetClinic 源码地图](../maps/01-spring-petclinic.md) 的调用链和测试策略。

## 自测

1. `OwnerRepository` 没有手写实现类时，调用链为什么仍然能运行？
2. Controller 测试和 Service 测试分别保护什么层次？
3. 为什么 `git blame` 只能提供线索，不能单独证明设计动机？
4. `/owners` 查询结果为空的最终用户反馈由哪些层共同决定？

<details>
<summary>参考要点</summary>

1. Spring Data 在运行时生成代理并注册 Repository Bean。
2. Controller 测试保护 HTTP 映射、参数、视图和绑定结果；Service 测试保护持久化与查询行为。
3. `blame` 只显示最后修改行和 Commit，真实原因可能在该 Commit、关联 PR 或更早讨论中。
4. Controller 校验并产生绑定错误，视图模板负责呈现；Repository 只返回空结果。

</details>

得分：__/4

## 过关标准

- 至少答对 3/4。
- 调用链中每个跳转都有文件/符号或测试证据。
- 能区分“接口定义”和“运行时实现”。
