"""
终末地基础功能插件
提供终末地相关的基础查询功能
"""
from amiyabot import PluginInstance, Message, Chain

# 创建插件实例
bot = PluginInstance(
    name='终末地基础功能',
    version='1.0.0',
    plugin_id='endfield-basic',
    description='提供终末地游戏的基础功能，包括角色查询、武器查询等',
    document='''
    终末地基础功能插件
    
    可用命令：
    - 终末地 - 显示终末地相关信息
    - 佩莉卡 - 佩莉卡角色信息
    - 角色列表 - 显示可用角色列表
    '''
)


# 终末地信息
@bot.on_message(keywords=['终末地', 'endfield', 'Endfield'])
async def endfield_info(data: Message):
    """终末地游戏信息"""
    info_text = '''《明日方舟：终末地》

《明日方舟：终末地》是鹰角网络开发的3D即时战略RPG游戏，
是《明日方舟》系列的新作品。

游戏背景：
故事发生在与罗德岛时间线不同的平行世界"塔洛斯-II"星球，
玩家将作为终末地公司的行动负责人，
与各具特色的干员们一起探索这个充满未知的新世界。

特色系统：
- 开放世界探索
- 即时战略战斗
- 基地建设
- 多样化的角色养成

佩莉卡是游戏中的重要角色之一！'''
    return Chain(data).text(info_text)


# 佩莉卡角色信息
@bot.on_message(keywords=['佩莉卡信息', 'perlica info'])
async def perlica_info(data: Message):
    """佩莉卡角色信息"""
    info_text = '''【佩莉卡 - Perlica】

佩莉卡是终末地中的重要角色，她是一位充满活力的战术专家。

角色特点：
- 职业：战术专家
- 擅长制定作战策略
- 性格活泼开朗
- 对战术研究充满热情

经典台词：
「准备好了吗？让我们一起探索终末地的世界！」
「佩莉卡随时待命！」

更多详细信息敬请期待游戏正式上线！'''
    return Chain(data).text(info_text)


# 角色列表
@bot.on_message(keywords=['角色列表', '干员列表'])
async def character_list(data: Message):
    """显示终末地角色列表"""
    characters_text = '''终末地角色列表

目前已知的部分角色：
━━━━━━━━━━━━━━
🌟 佩莉卡 (Perlica)
   战术专家，活力四射

🌟 恩德敏 (Endministrator)  
   终末地公司管理者

🌟 陈
   来自龙门的精英干员

━━━━━━━━━━━━━━
更多角色信息将在游戏上线后持续更新！

提示：发送 "佩莉卡信息" 可以查看详细角色信息'''
    return Chain(data).text(characters_text)


# 游戏进度查询
@bot.on_message(keywords=['游戏进度', '开发进度', '什么时候上线'])
async def game_progress(data: Message):
    """游戏开发进度"""
    progress_text = '''《明日方舟：终末地》开发进度

游戏目前仍在开发中，敬请期待！

已公开内容：
✅ 游戏概念宣传片
✅ 部分角色设计
✅ 游戏玩法演示
✅ 世界观设定

关注官方渠道获取最新消息：
- 明日方舟官网
- 官方微博
- 官方B站账号

让我们一起期待终末地的到来！'''
    return Chain(data).text(progress_text)
