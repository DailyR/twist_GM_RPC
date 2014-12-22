# -*- coding:utf-8 -*-
#!/usr/bin/env python
"""
客户端程序
1.连接上服务器后，打印欢迎信息
2.第1秒后发送一条消息
3.第2秒后发送断开连接命令。
"""
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor
from twisted.internet.protocol import ClientCreator
import msgpack


class MessageSend(Protocol):
    def connectionMade(self):
        # 连接上服务器后，打印出欢迎信息
        msg =['test', 'GM2', 1, 2, 3]
        msg_send = msgpack.packb(msg)+'###'
        self.transport.write(msg_send)
    def sendMessage(self,msg):
        # 发送一条消息
        self.transport.write(msg)

    
c = ClientCreator(reactor,MessageSend)
c.connectTCP("localhost",12345)
reactor.run()