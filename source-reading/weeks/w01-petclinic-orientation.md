# W1：Spring PetClinic 项目全景

> 预计用时：4–6 小时，分两次
> 固定版本：[`500158f732419217507c7656904b8e6aa1bcc0d6`](https://github.com/spring-projects/spring-petclinic/tree/500158f732419217507c7656904b8e6aa1bcc0d6)
> 周分支：`study/w01-petclinic-orientation`

## 本周目标

完成后你应该能够：

- 不靠目录逐页浏览，先说清 PetClinic 是一个什么项目。
- 找到构建入口、应用入口、Controller 入口和模板入口。
- 解释 Maven Wrapper 和 `src/main`、`src/test` 各自负责什么。
- 对 `/owners` 请求提出一份可验证的调用路径预测。

## 开始前基线诊断

先不看资料，用 5 分钟简短回答：

1. 拿到一个陌生 Java 项目，你前 10 分钟会先看哪三类文件？
2. 你怎样判断项目“真的能运行”，而不是只看 README？
3. 一个 HTTP 请求从浏览器到 HTML，中间可能经过哪些层？

这三题不计入本周分数，只用于选择讲解深度。答案直接写在周笔记里。

## 会话 A：拿到可复现版本

### 1. 获取固定版本

```powershell
git clone https://github.com/spring-projects/spring-petclinic.git repos/spring-petclinic
git -C repos/spring-petclinic checkout 500158f732419217507c7656904b8e6aa1bcc0d6
```

命令解释：

- 第一条下载项目历史和源码到被 Git 忽略的 `repos/`。
- 第二条把工作区切换到课程固定 Commit。

风险与可逆性：

- 低风险；不修改上游远程仓库。
- 只影响 `repos/spring-petclinic/`，损坏时可删除并重新克隆。

### 2. 先预测，再读

在打开 Java 文件前，回答：

- 应用主类最可能位于哪个目录？
- `/owners` 这个 URL 最可能由哪个包处理？
- 页面 HTML 最可能由服务端模板还是前端 SPA 生成？
- 哪个测试最可能证明 `/owners` 行为？

每个回答写出“依据”，不能只写猜测。

### 3. 构建与定向测试

```powershell
Set-Location repos/spring-petclinic
.\mvnw.cmd -DskipTests package
.\mvnw.cmd -Dtest=OwnerControllerTests test
```

命令解释：

- `mvnw.cmd` 使用项目自带 Maven Wrapper，避免依赖全局 Maven 版本。
- `package` 编译并打包，`-DskipTests` 暂时跳过测试。
- 定向测试只验证 Owner Controller 的主要行为。

风险与可逆性：

- 低风险；会下载依赖并创建 `target/`，不会修改源码。
- `target/` 已在仓库根 `.gitignore` 中忽略。

预期证据：

- 构建出现 `BUILD SUCCESS`。
- 定向测试通过数为正，没有测试因找不到而被静默跳过。

## 会话 B：画第一张项目地图

### 4. 只读这些文件

- `README.md`
- `pom.xml`
- `src/main/java/org/springframework/samples/petclinic/PetClinicApplication.java`
- `src/main/java/org/springframework/samples/petclinic/owner/OwnerController.java`
- `src/main/resources/templates/owners/ownersList.html`
- `src/test/java/org/springframework/samples/petclinic/owner/OwnerControllerTests.java`

每次只回答一个问题，再进入下一个：

1. `PetClinicApplication#main` 怎样启动应用？
2. `/owners` 对应哪个方法？它的方法签名接收什么、返回什么？
3. Controller 返回值 `owners/ownersList` 对应哪个资源？
4. 哪个测试名称最直接证明“按姓氏查询”？
5. 哪些目录本周明确不读？

### 5. 你的第一份路径预测

用 4–6 个节点预测：

```text
Browser -> <未知入口> -> <未知组件> -> <未知数据源> -> <未知模板>
```

每个“未知”都注上你准备检查的文件。W2 再验证，不要求现在正确。

## 必交产出

- [ ] 填写 [W1 周笔记模板](../templates/weekly-session.md) 中的基线诊断与两轮记录。
- [ ] 创建 W1 分支并提交命令、预期、实际输出和路径预测。
- [ ] 更新 [PetClinic 源码地图](../maps/01-spring-petclinic.md) 的构建与入口部分。
- [ ] 记录至少一个构建失败或环境问题；若没有失败，写明“未遇到”。

## 自测

> 先独立作答，再展开参考要点。

1. 为什么源码阅读要先固定 Commit，而不是直接读 `main`？
2. `src/main` 与 `src/test` 各自向读者提供了什么证据？
3. Maven Wrapper 相比直接使用全局 Maven 有什么好处？

<details>
<summary>参考要点</summary>

1. `main` 会移动，固定 Commit 才能让路径、行为和实验结果可复现。
2. `src/main` 是运行时代码；`src/test` 用输入、输出和边界证明设计意图。
3. 项目自带确定版本，减少“我本机能跑、换机器失败”的环境差异。

</details>

得分：__/3

## 过关标准

- 至少 3 题答对 2 题。
- 能说清项目定位、构建命令、应用入口和 `/owners` 的初步预测。
- 不把未验证的调用关系写成事实。
