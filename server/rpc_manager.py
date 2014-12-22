__author__ = 'Daily'

import msgpack

class RPC_Manager(object):
    def __init__(self):
        pass

    def register(self, rpc_handler):
        setattr(self, rpc_handler.eid, rpc_handler)

    def call(self, eid, fun_name, *param):
        getattr(getattr(self, eid), fun_name)(*param)

    def on_data(self, data):
        unpack_msg = msgpack.unpackb(data)
        self.call(*unpack_msg)

if __name__ == "__main__":
    pass