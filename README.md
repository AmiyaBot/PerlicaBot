<div align="center">

# PerlicaBot

**AmiyaBot 的终末地版本**

基于 [AmiyaBot](https://www.amiyabot.com/) 框架的终末地聊天机器人<br>
专为《明日方舟：终末地》(Arknights: Endfield) 玩家打造

</div>

<div>
    <img alt="license" src="https://img.shields.io/badge/license-MIT-green">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white">
    <img alt="platform" src="https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-blueviolet">
</div>

## 📖 项目简介

PerlicaBot 是基于 AmiyaBot 框架开发的聊天机器人，专门为《明日方舟：终末地》（Arknights: Endfield）游戏设计。项目名称源于游戏中的角色"佩莉卡"（Perlica），旨在为终末地玩家提供便捷的游戏辅助功能和互动体验。

## ✨ 主要特性

- 🤖 基于成熟的 AmiyaBot 框架
- 🎮 专为终末地游戏设计的功能
- 🔌 支持插件扩展
- 📊 完整的日志记录系统
- 🛠️ 易于配置和部署

## 🚀 快速开始

详细部署指南请参阅 [部署文档](docs/DEPLOYMENT.md)。

### 环境要求

- Python 3.10 或更高版本
- pip 包管理器

### 安装步骤

1. 克隆仓库

```bash
git clone https://github.com/AmiyaBot/PerlicaBot.git
cd PerlicaBot
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 配置机器人

编辑 `config/config.yaml` 文件，填入你的机器人配置信息：

```yaml
bot:
  appid: "你的机器人AppID"
  token: "你的机器人Token"
```

4. 启动机器人

```bash
python perlica.py
```

## 📝 使用指南

### 基础命令

- `帮助` / `help` - 显示帮助信息
- `关于` - 查看机器人信息
- `佩莉卡` - 触发佩莉卡问候

### 配置说明

配置文件位于 `config/config.yaml`，主要配置项包括：

- **bot**: 机器人基础配置（AppID、Token等）
- **admin**: 管理员账号列表
- **plugins**: 插件相关配置
- **log**: 日志配置

## 🔧 开发指南

### 项目结构

```
PerlicaBot/
├── config/           # 配置文件目录
│   └── config.yaml  # 主配置文件
├── plugins/         # 插件目录
├── log/            # 日志目录
├── perlica.py      # 主程序入口
├── requirements.txt # 依赖列表
└── README.md       # 项目说明
```

### 开发插件

PerlicaBot 支持通过插件扩展功能。插件开发请参考 [AmiyaBot 插件开发文档](https://www.amiyabot.com/develop/plugin/)。

## 🤝 贡献

欢迎为 PerlicaBot 做出贡献！你可以：

- 提交 Bug 报告或功能建议到 [Issues](../../issues)
- 开发新的插件功能
- 完善文档和示例
- 分享使用经验

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 🙏 鸣谢

- [AmiyaBot](https://github.com/AmiyaBot/Amiya-Bot) - 核心框架
- [AmiyaBot-core](https://github.com/AmiyaBot/Amiya-Bot-core) - 框架核心
- 《明日方舟：终末地》官方 - 游戏内容

## 📮 联系方式

- 项目地址：https://github.com/AmiyaBot/PerlicaBot
- AmiyaBot 官网：https://www.amiyabot.com/

---

<div align="center">
「准备好了吗？让我们一起探索终末地的世界！」 —— 佩莉卡
</div>
