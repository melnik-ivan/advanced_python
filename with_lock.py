#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

from threading import Thread, Lock
from time import sleep

from common import is_even, BaseOddEven


class OddEven(BaseOddEven, Thread):
    lock = Lock()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while self.pool:
            self.lock.acquire()
            if self.pool:
                if self.even == is_even(self.pool[-1]):
                    print(self.message_template.format(self.pool.pop()))
            self.lock.release()
            sleep(0.0005)
