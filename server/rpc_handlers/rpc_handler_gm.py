__author__ = 'Daily'

from rpc_base import RPC_Base

class RPC_Handler_GM(RPC_Base):
    def __init__(self, poller):
        self.eid = 'test'
        super(RPC_Handler_GM, self).__init__(poller, self.eid)


    def GM_order(self, arg1, arg2, arg3):
    	print "here is GM_order"
        self.client.test(10,11,"Daily")  #call client function

if __name__ == '__main__':
    rpc_sample = RPC_Handler_2(1)
    rpc_sample.test(1,2,3)


