#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

import threading
from time import sleep

from common import is_even, BaseOddEven


class OddEven(BaseOddEven, threading.Thread):
    lock = threading.Lock()

    def run(self):
        while self.pool:
            self.lock.acquire()
            if self.pool:
                if self.even == is_even(self.pool[-1]):
                    print(self.message_template.format(self.pool.pop()))
            self.lock.release()
            sleep(0.0005)
