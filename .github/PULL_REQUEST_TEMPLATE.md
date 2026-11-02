## 变更范围

<!-- 说明本 PR 对应周次、阶段和实际完成内容。 -->

- 周次：
- 阶段：
- 关联 Issue：

## 学习证据

- [ ] 周笔记包含预测、实际结果和纠偏过程。
- [ ] 源码地图记录固定 Ref/Commit、命令、预期和实际结果。
- [ ] 定向测试已运行，或记录了无法运行的真实原因。
- [ ] 阶段测验达到 4/5；未达到时不勾选。

## 安全与仓库卫生

- [ ] 不包含 API Key、Token、密码或其他密钥。
- [ ] 不包含 `.LEARNING/`、`repos/`、`.venv/`、`target/`、`build/`。
- [ ] 不复制上游项目源码；引用使用固定版本链接。
- [ ] 失败实验保留错误、原因和修复，未删除证据。

## 验证

```powershell
powershell -ExecutionPolicy Bypass -File .\source-reading\scripts\check-course.ps1
git diff --check
```

结果：

- 课程检查：
- Diff 检查：
- 定向测试：

## 合并说明

<!-- 说明为什么已经达到阶段标准，以及未完成内容如何处理。 -->
