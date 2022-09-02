from nonebot import on_command, get_driver
from nonebot.adapters import Message
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11.message import MessageSegment
from nonebot.params import CommandArg, ArgPlainText

from .main import GetFursuitRand, GetFursuitByName, GetFurByIdCommand

__help_plugin_name__ = 'Python版本的绒狸!!!'
__help_version__ = '1.0'

__des__ = "获取毛毛图"
__cmd__ = f"""
指令前缀 + 指令
当前配置的指令前缀为: {" ".join(list(get_driver().config.command_start))}
""".strip()
__list__ = """

来只毛 | 随机获取一张毛毛图
来只 [毛毛名称] | 获取一张[毛毛名称]的图
查Fid [毛毛名称]| 获取[毛毛名称]的所有图片的Fid (未完成) [制作中]
找毛图 [Fid] | 获取一张指定FurID的图片 (未完成)

""".strip()
__usage__ = f"{__des__}\n\nUsage:\n{__cmd__}\n\nCommandList:[指令名 | 指令介绍]\n{__list__}"
TITLE = "---407---ヾ(≧▽≦*)o---"  # 触角
TITLE2 = "今天你吸毛了嘛（＾∀＾●）ﾉｼ"  # 呆毛
DOWM = "---407---ヾ(≧▽≦*)o---"  # 尾巴


def send_img(img_url):
    return MessageSegment.image(img_url)


# 随机兽图API
# GetFursuitRand
# 来只毛模块


rancom = on_command("来只毛", priority=5)


@rancom.handle()
async def getranfc():
    data = GetFursuitRand()
    data = data.get('data')
    id = str(data.get('id'))
    # cid = data.get('cid')
    name = data.get('name')
    # name = "test"
    pic_url = data.get('url')
    # pic_url = data.get('thumb')
    # thumb = data.get('thumb')
    ser = "随机获取"
    msg = (TITLE +
           "\n" + TITLE2 +
           "\n" + "FurID: " + id +
           "\n" + "毛毛名字: " + name +
           "\n" + "搜索方式: " + ser +
           "\n" + send_img(pic_url) +
           "\n" + DOWM)
    await rancom.finish(msg)


# 名称搜图API
# GetFursuitByName
# 来只 {毛毛名字} 模块


nameser = on_command("来只", priority=5)


@nameser.handle()
async def namesernamegetfunc(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("name", args)


@nameser.got("name", prompt="你想吸哪只毛毛捏?(。・ω・。)")
async def getname(fur_name: str = ArgPlainText("name")):
    data = GetFursuitByName(fur_name)
    code = data.get('code')
    if code == 200:
        data = data.get('data')
        id = str(data.get('id'))
        # cid = data.get('cid')
        name = data.get('name')
        pic_url = data.get('url')
        # thumb = data.get('thumb')
        ser = "名称搜索"
        msg = (TITLE +
               "\n" + TITLE2 +
               "\n" + "FurID: " + id +
               "\n" + "毛毛名字: " + name +
               "\n" + "搜索方式: " + ser +
               "\n" + send_img(pic_url) +
               "\n" + DOWM)
        await nameser.finish(msg)

    elif code == 404:
        msg = "该毛毛不存在或者未收录进绒狸毛毛数据库哟(●'◡'●)"
        await nameser.finish(msg)


# GetFurByIdCommand
# FID搜图API
# 找毛图

GFBIC = on_command("找毛图", priority=5)


@GFBIC.handle()
def GFBIC_FUNC(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("fid", args)


@GFBIC.got("fid", prompt="乃想找 id 是什么的图片捏?(。・ω・。)")
async def GFBIC_GOT(gfbic_fid: str = ArgPlainText("fid")):
    data = GetFurByIdCommand(gfbic_fid)
    code = data.get('code')
    if code == 200:
        data = data.get('data')
        id = str(data.get('id'))
        # cid = data.get('cid')
        name = data.get('name')
        pic_url = data.get('url')
        # thumb = data.get('thumb')
        ser = "名称搜索"
        msg = (TITLE +
               "\n" + TITLE2 +
               "\n" + "FurID: " + id +
               "\n" + "毛毛名字: " + name +
               "\n" + "搜索方式: " + ser +
               "\n" + send_img(pic_url) +
               "\n" + DOWM)
        await GFBIC.finish(msg)

    elif code == 404:
        msg = "该ID不存在或者未收录进绒狸毛毛数据库哟(●'◡'●)"
        await GFBIC.finish(msg)

# 每日鉴毛
# GetDailyFurCommand



