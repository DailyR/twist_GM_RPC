__author__ = 'Daily'

from rpc_manager import RPC_Manager
from data_handler import Data_Handler
from transport import ClientThread
from rpc_handlers.rpc_handler_sample import RPC_Handler_Sample
from rpc_handlers.rpc_handler_2 import RPC_Handler_2

from PyQt4.QtCore import QCoreApplication
import sys
from PyQt4 import QtCore, QtGui

class Window( QtGui.QMainWindow ):
    def __init__( self ):
        super( Window, self ).__init__()
        self.setWindowTitle( "GM-GUI" )
        self.resize( 200, 300 )
        label = QtGui.QLabel( "Here is GM-GUI paint" )
        label.setAlignment( QtCore.Qt.AlignCenter )
        self.setCentralWidget( label )

class GM_RPC(object):
    def __init__(self, sep, port):
        self.sep = sep
        self.rpc_manager = RPC_Manager()
        self.data_handler = Data_Handler(sep, self.rpc_manager.on_data)
        self.thread = ClientThread(port, self.data_handler, sep)
        self.register_handlers()

    def register_handlers(self):
        sample = RPC_Handler_Sample(self.thread)
        self.rpc_manager.register(sample)
        test = RPC_Handler_2(self.thread)
        self.rpc_manager.register(test)

    def start(self):
        self.thread.start()



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    #rpc = GM_RPC('###', 9000)
    rpc = GM_RPC('###', 12345)
    rpc.start()
    demo = Window()
    demo.show()
    app.exec_()


