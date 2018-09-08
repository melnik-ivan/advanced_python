#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

from threading import Thread, Semaphore
from time import sleep

from common import is_even, BaseOddEven


class OddEven(BaseOddEven, Thread):
    semaphore_even = Semaphore(1)
    semaphore_odd = Semaphore(0)

    def run(self):
        while self.pool:
            self.semaphore.acquire()
            if self.pool:
                if self.even == is_even(self.pool[-1]):
                    print(self.message_template.format(self.pool.pop()))
            self.semaphore_opposite.release()
            sleep(0.0005)

    @property
    def semaphore(self):
        if self.even:
            return self.semaphore_even
        return self.semaphore_odd

    @property
    def semaphore_opposite(self):
        if self.even:
            return self.semaphore_odd
        return self.semaphore_even
