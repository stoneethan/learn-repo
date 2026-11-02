# 固定版本与环境

## 为什么锁定版本

开源项目的 `main` 每天都在变化。课程中的目录、类名和调用链必须以固定 Tag/Commit 为准。升级版本是单独的学习任务，不在阅读中途悄悄切换。

## 课程版本

| 项目 | 固定版本 | Commit | 许可证 | 周次 | 执行深度 |
|---|---|---|---|---|---|
| [Spring PetClinic](https://github.com/spring-projects/spring-petclinic) | `main@2026-09-29` | `500158f732419217507c7656904b8e6aa1bcc0d6` | Apache-2.0 | W1–W3 | 构建、运行、定向测试 |
| [Gson](https://github.com/google/gson) | `gson-parent-2.15.0` | `fcd416909db2bea96eb916bcfb2d0a83cb9b86c3` | Apache-2.0 | W4–W5 | 定向测试、Adapter 实验 |
| [Spring Framework](https://github.com/spring-projects/spring-framework) | `v7.0.10` | `33a85b0bec67adb759aa898e3b80d603786be082` | Apache-2.0 | W6–W7 | 选择模块定向测试 |
| [Micrograd](https://github.com/karpathy/micrograd) | `main@2026-08-03` | `7bc720e951fe422b8f8814aa5aa1b64121d26b4c` | MIT | W8 | 单元测试、最小实验 |
| [OpenAI Python](https://github.com/openai/openai-python) | `v3.42.1` | `190dd5aee1053dd2093d2a5c3937f604860310a3` | Apache-2.0 | W9 | 定向测试、Mock，无真实付费调用 |
| [LangGraph](https://github.com/langchain-ai/langgraph) | `1.2.19` | `5bd231cbfd913e05ebc662f519eb9a655bc766df` | MIT | W10 | Python 包定向测试、最小状态图 |
| [Dify](https://github.com/langgenius/dify) | `1.18.0` | `50abea97062110044f15d0e03ccecadd9ccc87ca` | 以仓库 LICENSE 为准 | W11 | 静态精读，不启动整套 Docker |
| [OpenAI Agents Python](https://github.com/openai/openai-agents-python) | `v0.24.0` | `17d994bd3045dae71acda676a4ef4762ed8ecd94` | MIT | W12 | 独立冷启动，不跟教程逐行读 |

## 本地目录约定

所有上游源码放入被 Git 忽略的 `repos/`：

```text
repos/
├── spring-petclinic/
├── gson/
├── spring-framework/
├── micrograd/
├── openai-python/
├── langgraph/
├── dify/
└── openai-agents-python/
```

获取固定版本时，先浅克隆，再切换到表中的 Tag 或 Commit。

### Tag 示例

```powershell
git clone https://github.com/google/gson.git repos/gson
git -C repos/gson checkout gson-parent-2.15.0
```

### Commit 示例

```powershell
git clone https://github.com/karpathy/micrograd.git repos/micrograd
git -C repos/micrograd checkout 7bc720e951fe422b8f8814aa5aa1b64121d26b4c
```

命令解释：

- `git clone` 下载项目历史和源码。
- `git -C repos/... checkout ...` 只切换本地目录到固定版本。

风险与可逆性：

- 低风险；不会修改上游远程仓库。
- `checkout` 会改变本地 `repos/` 下对应工作区，这些目录已被忽略且可重新克隆。
- 不要在 `repos/` 内保留唯一学习笔记；笔记统一写入 `source-reading/`。

## 已核对环境

- JDK 17.0.18。
- Maven 3.9.14，Java 项目优先使用各自的 `mvnw.cmd` 或 `gradlew.bat`。
- Python 3.14.3，通过 `py -3.14 -m venv` 创建项目虚拟环境。
- Git、GitHub CLI、Docker 和 WSL 2 已安装。
- 不设置真实 API Key 作为课程前置条件；默认使用仓库测试或 Mock。

## 升级规则

只有当固定版本完成阶段验收后，才允许做版本迁移练习。迁移必须单独开分支，记录变更的入口、测试失败和行为差异，不覆盖旧地图。
