# PerlicaBot 插件目录

这个目录用于存放 PerlicaBot 的插件。

## 插件开发

PerlicaBot 基于 AmiyaBot 框架，支持通过插件扩展功能。

### 插件结构示例

```python
from amiyabot import PluginInstance, Message, Chain

# 创建插件实例
bot = PluginInstance(
    name='示例插件',
    version='1.0.0',
    plugin_id='example-plugin',
    description='这是一个示例插件',
    document='插件使用说明'
)

@bot.on_message(keywords=['示例'])
async def example_handler(data: Message):
    return Chain(data).text('这是一个示例回复')
```

### 开发文档

更多插件开发信息请参考：
- [AmiyaBot 插件开发文档](https://www.amiyabot.com/develop/plugin/)
- [AmiyaBot 官方插件示例](https://github.com/AmiyaBot/Amiya-Bot-plugins)

## 插件安装

将开发好的插件文件夹放入此目录，重启机器人即可自动加载。
