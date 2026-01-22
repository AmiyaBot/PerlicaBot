# PerlicaBot 部署指南

本文档将指导您完成 PerlicaBot 的部署过程。

## 系统要求

### 最低要求
- Python 3.10 或更高版本
- 2GB RAM
- 1GB 可用磁盘空间
- 稳定的网络连接

### 推荐配置
- Python 3.11+
- 4GB+ RAM
- 5GB+ 可用磁盘空间

## 安装步骤

### 1. 安装 Python

确保系统已安装 Python 3.10+：

```bash
python --version
# 或
python3 --version
```

如果未安装，请访问 [Python官网](https://www.python.org/) 下载安装。

### 2. 克隆项目

```bash
git clone https://github.com/AmiyaBot/PerlicaBot.git
cd PerlicaBot
```

### 3. 安装依赖

建议使用虚拟环境：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 4. 配置机器人

复制配置示例文件：

```bash
cp config/config.yaml.example config/config.yaml
```

编辑 `config/config.yaml`，填入您的机器人配置。

### 5. 启动机器人

```bash
python perlica.py
```

## 常见问题

详见完整文档。

## 获取帮助

- 项目 Issues: https://github.com/AmiyaBot/PerlicaBot/issues
- AmiyaBot 官方文档: https://www.amiyabot.com/
