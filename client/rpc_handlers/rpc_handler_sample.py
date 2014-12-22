__author__ = 'Daily'

from rpc_base import RPC_Base
import msgpack

class RPC_Handler_Sample(RPC_Base):
    def __init__(self, poller):
        self.eid = 'sample'
        super(RPC_Handler_Sample, self).__init__(poller, self.eid)

    def test(self, arg1, arg2, arg3):
    	print "Client gm_order has been called!"
    	print 'arg1=',arg1
    	print 'arg2=',arg2
    	print 'arg3=',arg3

        #self.client.test(1,2,3)
        
if __name__ == '__main__':
    rpc_sample = RPC_Handler_Sample(1)
    rpc_sample.test(1,2,3)


