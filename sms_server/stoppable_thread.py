import threading
import time

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._status = 'running'

    def stop(self):
        if(self._status == 'running'):
            self._status = 'stopping'

    def stopped(self):
        self._status = 'stopped'

    def is_running(self):
        return (self._status == 'running')

    def is_stopping(self):
        return (self._status == 'stopping')

    def is_stopped(self):
        return (self._status == 'stopped')
