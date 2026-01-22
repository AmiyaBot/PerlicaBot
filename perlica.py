import asyncio
from amiyabot import AmiyaBot, Message, Chain

# 创建PerlicaBot实例 - 终末地版本
bot = AmiyaBot(
    appid='your_appid',
    token='your_token',
    app_name='PerlicaBot',
    log_name='PerlicaBot'
)


@bot.on_message(keywords=['帮助', 'help'])
async def help_handler(data: Message):
    """帮助命令处理器"""
    help_text = '''PerlicaBot - 终末地版本
    
欢迎使用佩莉卡机器人！这是基于AmiyaBot框架的终末地版本。

可用命令：
- 帮助/help - 显示此帮助信息
- 关于 - 查看机器人信息

更多功能开发中...'''
    return Chain(data).text(help_text)


@bot.on_message(keywords=['关于'])
async def about_handler(data: Message):
    """关于命令处理器"""
    about_text = '''PerlicaBot - AmiyaBot的终末地版本

这是一个基于AmiyaBot框架开发的聊天机器人，
专为《明日方舟：终末地》玩家打造。

项目地址：https://github.com/AmiyaBot/PerlicaBot
基于框架：AmiyaBot (https://www.amiyabot.com/)'''
    return Chain(data).text(about_text)


@bot.on_message(keywords=['佩莉卡', 'perlica', 'Perlica', 'PERLICA'])
async def perlica_greeting(data: Message):
    """佩莉卡问候语"""
    return Chain(data).text('佩莉卡随时待命！')


if __name__ == '__main__':
    bot.start()
