# -*- coding:utf-8 -*-
__author__ = 'Daily'

from twisted.internet.protocol import ServerFactory, Protocol
from twisted.internet import reactor
from PyQt4.QtCore import QThread
from PyQt4.QtCore import QCoreApplication
import sys
import msgpack


class Server(Protocol):

    #此处用于重写server的protocal
    def connectionMade(self):
        print 'Got connection from', self.transport.client
        #msg =['sample', 'test', 1, 2, 3]
        #msg_send = msgpack.packb(msg)+'###'
        #self.send_data(msg_send)
        #print "send_data to client:",self.transport.client,msg

    def connectionLost(self, reason):
        print self.transport.client, 'disconnected'

    def dataReceived(self, data):
        if data is not None:
            #print 'Get data:' + str(data)
            self.on_data(data)  #dispatch 
        else :
            print "dataReceived is None!"

    def send_data(self,data):
        if data is not None:
            self.transport.write(data)
        else :
            print "send_data is None!"


class CustomServerFactory(ServerFactory):
    protocol = Server

    def __init__(self, on_data):

        self.proto = None
        self.on_data = on_data

    def buildProtocol(self, addr):
        self.proto = ServerFactory.buildProtocol(self, addr)
        self.proto.on_data = self.on_data
        return self.proto

class ServerThread(QThread):
    def __init__(self, port, on_data, sep):
        QThread.__init__(self)
        self.port = port
        self.on_data = on_data
        self.sep = sep

    def run(self):
        self.factory = CustomServerFactory(self.on_data)
        reactor.listenTCP(self.port, self.factory)
        reactor.run(installSignalHandlers=0)

    def send_data(self, data):
        self.factory.proto.send_data(data + self.sep + '\n')

if __name__ == '__main__':
    def helper(x):
        print x

    app = QCoreApplication(sys.argv)
    #t = ClientThread(9000, helper)
    t = ServerThread(1234, helper)
    t.start()
    app.exec_()

