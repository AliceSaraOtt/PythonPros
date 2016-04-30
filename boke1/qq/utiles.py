#coding:utf8
import Queue

class Chat(object):
    def __init__(self):
        self.msg_queue = Queue.Queue()
    def get_msg(self):
        new_msg = []
        # print self.msg_queue.qsize()
        if self.msg_queue.qsize() > 0:
            for msg in range(self.msg_queue.qsize()):
                new_msg.append(self.msg_queue.get_nowait()) # 防止阻塞 nowait
        else:
            try:
                new_msg.append(self.msg_queue.get(timeout=60))
            except Queue.Empty:
                print '没有新消息'
        return new_msg