# 课程进度

> 只勾选已经完成并验证的项目。日期、得分和 Commit 必须来自真实学习记录。

## 总进度

| 阶段 | 周次 | 状态 | 阶段测验 | 合并 PR |
|---|---|---|---|---|
| Java 项目破冰 | W1–W3 | 未开始 | 0/5 | 待创建 |
| Java 库与框架 | W4–W7 | 未开始 | 0/5 | 待创建 |
| AI 核心与编排 | W8–W11 | 未开始 | 0/5 | 待创建 |
| 独立冷启动 | W12 | 未开始 | 0/5 | 待创建 |

## 周任务

- [ ] [W1：PetClinic 项目全景](weeks/w01-petclinic-orientation.md)
- [ ] [W2：PetClinic 请求、测试与 Git 历史](weeks/w02-petclinic-trace-and-history.md)
- [ ] [W3：PetClinic 真实改动与阶段验收](weeks/w03-petclinic-change-and-gate.md)
- [ ] [W4：Gson API 与适配器解析](weeks/w04-gson-adapter-pipeline.md)
- [ ] [W5：Gson 反射、异常与扩展](weeks/w05-gson-reflection-and-extension.md)
- [ ] [W6：Spring IoC 容器](weeks/w06-spring-ioc.md)
- [ ] [W7：Spring MVC 请求链与阶段验收](weeks/w07-spring-mvc-and-gate.md)
- [ ] [W8：Micrograd 反向传播](weeks/w08-micrograd-autograd.md)
- [ ] [W9：OpenAI Python SDK](weeks/w09-openai-python-sdk.md)
- [ ] [W10：LangGraph 执行模型](weeks/w10-langgraph-runtime.md)
- [ ] [W11：Dify RAG 链路与阶段验收](weeks/w11-dify-rag-and-gate.md)
- [ ] [W12：独立冷启动与最终验收](weeks/w12-cold-start-and-final-gate.md)

## 六份源码地图

- [ ] [Spring PetClinic](maps/01-spring-petclinic.md)
- [ ] [Gson](maps/02-gson.md)
- [ ] [Spring Framework](maps/03-spring-framework.md)
- [ ] [OpenAI Python](maps/04-openai-python.md)
- [ ] [LangGraph](maps/05-langgraph.md)
- [ ] [Dify](maps/06-dify.md)

## 三张旗舰图

- [ ] Java 请求生命周期：浏览器 → PetClinic → Spring MVC → Repository → Template
- [ ] Gson 适配器解析链：类型描述 → AdapterFactory 选择 → 反射/自定义 Adapter
- [ ] AI 执行链：State/Input → 编排循环 → Tool/RAG → Model → Event/Result

## 最终验收

- [ ] 12 份周笔记齐全，每题答案和实际得分可见。
- [ ] 6 份源码地图均记录固定版本、命令、结果和扩展点。
- [ ] 3 张旗舰图可以脱稿讲解。
- [ ] [OpenAI Agents Python 冷启动报告](cold-start/openai-agents-python.md) 在 30 分钟内独立完成。
- [ ] 完成一次 Issue → 分支 → Commit → PR 演练。
- [ ] 课程检查脚本与 `git diff --check` 通过。

## 更新格式

每次学习结束追加一行：

```text
YYYY-MM-DD · WNN · 用时 · 完成内容 · 测验得分 · Commit SHA
```
