# -*- coding:utf-8 -*-
#!/usr/bin/env python

__author__ = 'Daily'

from twisted.internet.protocol import Protocol
from transport import ServerThread
from rpc_manager import RPC_Manager
from data_handler import Data_Handler
from PyQt4.QtCore import QCoreApplication
from rpc_handlers.rpc_handler_sample import RPC_Handler_Sample
from rpc_handlers.rpc_handler_gm import RPC_Handler_GM
import sys

class GM_Server(object):

    def __init__(self, sep, port):
        self.sep = sep
        self.rpc_manager = RPC_Manager()
        #print dir(self.rpc_manager)
        self.data_handler = Data_Handler(sep, self.rpc_manager.on_data)
        self.thread = ServerThread(port, self.data_handler, sep)
        self.register_handlers()


    def register_handlers(self):
        sample = RPC_Handler_Sample(self.thread)
        self.rpc_manager.register(sample)
        test = RPC_Handler_GM(self.thread)
        self.rpc_manager.register(test)

    def start(self):
        self.thread.start()


if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    rpc_server = GM_Server('###', 12345)
    print 'Server started'
    rpc_server.start()
    app.exec_()