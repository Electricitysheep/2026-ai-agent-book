# 第六卷：从社交裂变到系统自动化——腾讯 (Tencent) 的全域控制

> *"当别人都在拼命造出最强的 IDE 时，拥有国内最恐怖社交与企业协作生态的腾讯，选择了另一条路。他们不仅要接管你的代码，他们要像操作 QQ 和企业微信一样，接管你的整个桌面。"*

---

![Tencent Logo](https://github.com/Tencent.png)

## 📖 第一节：基础简介与生态位
**企业背景**：腾讯 (Tencent)，拥有中国最大的社交与职场通讯底座（微信/企业微信）。
**2026 主力大模型**：Hunyuan (混元) 企业级矩阵，以及底层的 TokenHub 网关。
**核心战略**：做“全栈连接器”。不卷枯燥的刷榜，而是要把 Agent 以最无感知的方式，直接镶嵌进全国网民和员工每天都要打开的微信和操作系统界面里。

---

## 2. WorkBuddy：潜伏在桌面的超级员工

2026 年中旬，腾讯云正式发布了震撼级的产品——**WorkBuddy**。
这不再是一个需要在浏览器里打开的网页端大模型，而是一个深度嵌入到 Windows 和 macOS 系统底层的全场景桌面 AI 智能体。

*(腾讯云官方：WorkBuddy 超级个体看板)*
*(腾讯云官方：WorkBuddy 超级个体看板)*
![WorkBuddy Super Individual Banner](./assets/codebuddy_banner.png)


### OS-Level (操作系统级) 自动化
WorkBuddy 的恐怖之处在于它能直接进行本地计算机的自动化操作。
借助底层的视觉语言模型（VLM），WorkBuddy 能“看到”你桌面的情况。你对它说：“把昨天的财报数据提取出来，发给团队的李总”。
它会在后台直接操作本地文件系统，甚至能原生地调起**企业微信**，自动检索联系人并发送附件。这种操作不再是通过死板的 API，而是模拟真实的 UI 级点击与拖拽。

---

## 3. CodeBuddy 2.0 与开放标准协议

在专业软件开发领域，腾讯打出了第二张王牌：由“腾讯元宝代码大模型”驱动的 **CodeBuddy 2.0**。
但在 2026 年，这不仅是一个写代码的工具，腾讯试图去定义整个 AI Agent 行业的“规矩”。

*(腾讯 CodeBuddy VS Code 原生界面与 ACP 协议直连)*
![Tencent Hunyuan Architecture](https://avatars.githubusercontent.com/u/158582294?v=4)

### 拥抱 ACP (Agent Client Protocol) 协议
在 2026 年的编辑区大战中，MCP (Model Context Protocol) 和 ACP 是两大最顶尖的协议。

### ACP 协议与 MCP 的终极对决
在深入了解 CodeBuddy 2.0 之前，我们必须谈谈 ACP (Agent Client Protocol) 与 MCP (Model Context Protocol) 的战争。
MCP 是由 Anthropic 牵头，各大 IDE 追随的“上下文模型协议”，它侧重于让大模型读取外部工具。
而腾讯支持的 ACP 更加硬核，它是一种“客户端控制协议”。这意味着在企业内网中，CodeBuddy 能够以更高的权限在本地执行 `git rebase` 甚至 `docker build`。腾讯元宝代码大模型在这一层面上，真正实现了端侧算力与云端大模型的无缝“交接”。

*(腾讯 CodeBuddy VS Code 原生界面直连)*
![CodeBuddy Official Logo](./assets/codebuddy_logo.svg)

CodeBuddy 2.0 宣布原生支持 Zed 编辑器首创的 **ACP 协议**。
这意味着什么？这意味着腾讯把“Agent 大脑（服务器端）”和“UI 面板（客户端）”彻底解耦了。极客们可以把 CodeBuddy 2.0 的 Agent 核心抽离出来，完美无缝地插入到他们自己喜欢的任何（支持 ACP 的）编辑器中，不再受限于官方指定的 IDE。

### CodeBuddy.md：全行业的 Playbook
这是腾讯 2026 年极具野心的一步。
他们推出了 `CodeBuddy.md` 开放标准。这个 Markdown 文件就像是整个项目的“宪法”或 Playbook。
无论你拉起的是阿里的通义灵码、字节的 Trae，还是腾讯的 CodeBuddy，只要你的项目根目录下有这个 `CodeBuddy.md`，所有 AI Agent 都会自动读取其中的指令设定、依赖版本号和编码规范（Source of Truth）。

> *"腾讯的底层逻辑依然是连接：无论你是企业微信里的同事，还是系统里的某个应用程序，或者是写代码时的不同环节，WorkBuddy 和 CodeBuddy 要做的，就是把这些孤岛统统连起来，变成一张网。"*

