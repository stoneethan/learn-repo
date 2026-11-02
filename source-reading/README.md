# 12 周 Java × AI 开源项目阅读

> 当前状态：课程脚手架已完成，等待 W1 开始。
>
> 目标：12 周后，面对一个陌生项目，能在 30 分钟内找到入口、构建方式、一条关键调用链和至少两个扩展点，并用面试官听得懂的方式讲清楚。

## 从这里开始

1. 先读 [源码阅读方法](00-reading-method.md)，知道每一轮应该看什么、交付什么。
2. 打开 [学习进度](01-progress.md)，当前只从 W1 开始，不提前赶进度。
3. 开始 W1 前完成一次 3–5 题基线诊断；具体问题在 [W1 任务](weeks/w01-petclinic-orientation.md) 中。
4. 每完成一次学习，更新周笔记和源码地图；每完成一个阶段，通过 5 题检查后再前进。

## 学习契约

- 每周投入 4–6 小时，拆成两次 2–3 小时的会话，具体星期按周安排。
- 先看全景，再进入一条真实调用链；不在没有地图时逐行硬读。
- 每讲 5–10 分钟，你必须输出一次预测、代码、图、命令结果或口头解释，然后立即纠偏。
- 每周至少一个可验证产出物，并提交到 Git。
- 每周 3–5 题、每阶段 5 题，得分达到 80% 才进入下一阶段。
- 不背结论：必须同时说明“入口是什么、控制流怎么走、为什么这样设计、扩展点在哪里”。

## 12 周路线

| 周次 | 项目 | 核心能力 | 主要产出 |
|---|---|---|---|
| W1 | Spring PetClinic | 项目全景、构建、启动入口 | 总览、环境冒烟、`/owners` 请求预测 |
| W2 | Spring PetClinic | Controller → Repository → Template、测试与 Git 历史 | 请求轨迹、测试记录 |
| W3 | Spring PetClinic | 独立复述一次真实改动 | 源码地图 1、阶段测验 |
| W4 | Gson | API 分层、`TypeAdapter`、工厂优先级 | Gson API 地图 |
| W5 | Gson | 反射、异常、测试、自定义 Adapter | 源码地图 2、Java 实验 |
| W6 | Spring Framework | BeanDefinition、IoC 容器刷新、依赖注入 | IoC 调用图 |
| W7 | Spring Framework | `DispatcherServlet` 到 Controller | 源码地图 3、MVC 时序图、阶段测验 |
| W8 | Micrograd | 计算图、反向传播、参数更新 | 公式与代码对照、梯度实验 |
| W9 | OpenAI Python SDK | 客户端、重试、响应、流式传输 | 源码地图 4、Mock 请求链 |
| W10 | LangGraph | State、Node、Edge、Pregel、Checkpoint | 源码地图 5、状态图实验 |
| W11 | Dify | API → Service → RAG → 模型调用 | 源码地图 6、阶段测验 |
| W12 | OpenAI Agents Python | 独立冷启动、与 LangGraph 对比 | 冷启动报告、最终测验、PR 演练 |

## 最终作品

完成课程时，`source-reading/` 中应包含：

- 6 份源码地图：PetClinic、Gson、Spring Framework、OpenAI Python、LangGraph、Dify。
- 3 张旗舰图：Java 请求生命周期、Gson 适配器解析链、AI Agent/RAG 执行链。
- 1 份独立冷启动报告：OpenAI Agents Python，与 LangGraph 做设计对比。
- 12 份周笔记、4 份阶段检查、1 次 Issue → 分支 → Commit → PR 演练。

## Git 与 GitHub 约定

- 周任务分支：`study/wNN-主题`。
- 冲刺分支：`course/source-reading-12w`。
- Commit 使用 `study(wNN): ...`、`notes(wNN): ...`、`lab(wNN): ...`。
- 每个阶段验收通过后再合并回 `main`；未通过的实验保留在分支中并记录失败原因。
- 不提交 `.LEARNING/`、`repos/`、虚拟环境、构建产物、密钥或上游源码副本。

## 自检

在仓库根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\source-reading\scripts\check-course.ps1
git diff --check
```

课程检查脚本只读取 Markdown、验证相对链接和文件结构，并扫描常见密钥格式；它不会修改文件。
