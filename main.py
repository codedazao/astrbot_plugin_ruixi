from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp

@register("ruixibot", "dazaocode", "瑞希机器人的逻辑层", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    # @filter.command("helloworld")
    # async def helloworld(self, event: AstrMessageEvent):
    #     """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
    #     user_name = event.get_sender_name()
    #     message_str = event.message_str # 用户发的纯文本消息字符串
    #     message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
    #     logger.info(message_chain)
    #     yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!") # 发送一条纯文本消息
    
    @filter.command("测试通讯")
    async def married(self,event: AstrMessageEvent):
        group_id = event.group_id
        logger.info(f"发送的群号为${group_id}")
        logger.info(f"发送者为${event.get_sender_name()}")
        logger.info(f"何时发送的消息${event.timestamp}")
        send_message_chain = [
            Comp.Plain(f"发送的群号为${group_id} \n 发送者为${event.get_sender_name()} \n 何时发送的消息${event.timestamp}")
        ]
        yield event.plain_result(send_message_chain)

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
