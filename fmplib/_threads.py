from threading import Thread


class ReturnThread(Thread):
    
    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self.value = {}