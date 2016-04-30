#coding:utf8
import Queue

class Chat():
    def __init__(self):
        self.msg_queue = Queue.Queue()
    def getMsg(self):
        msgs = []
        if self.msg_queue.qsize() > 0:
            for msg in range(self.msg_queue.qsize()):
                msgs.append(self.msg_queue.get())
        # else:
        #     try:
        #         msgs.append(self.msg_queue.get(timeout=60))
        #     except Queue.Empty:
        #         print '没有新消息'
        return msgs