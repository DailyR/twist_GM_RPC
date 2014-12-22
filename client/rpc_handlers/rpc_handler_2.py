__author__ = 'Daily'

from rpc_base import RPC_Base

class RPC_Handler_2(RPC_Base):
    def __init__(self, poller):
        self.eid = 'test'
        super(RPC_Handler_2, self).__init__(poller, self.eid)

    def test(self, arg1, arg2, arg3):
    	print "here is test"
    	print 'arg1=',arg1
    	print 'arg2=',arg2
    	print 'arg3=',arg3

    def GM2(self, arg1, arg2, arg3):
    	print "here is GM2"
        self.client.test(10,11,"Daily")  #call client function

if __name__ == '__main__':
    rpc_sample = RPC_Handler_2(1)
    rpc_sample.test(1,2,3)


