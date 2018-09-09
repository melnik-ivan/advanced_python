#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

import multiprocessing
from time import sleep

import common


class OddEven(common.BaseOddEven, multiprocessing.Process):
    semaphore_even = multiprocessing.Semaphore(1)
    semaphore_odd = multiprocessing.Semaphore(0)

    def run(self):
        while self.pool:
            self.semaphore.acquire()
            if self.pool:
                if self.even == common.is_even(self.pool[-1]):
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
