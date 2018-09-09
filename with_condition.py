#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

import multiprocessing
from time import sleep

import common


class OddEven(common.BaseOddEven, multiprocessing.Process):
    condition_odd = multiprocessing.Condition()
    condition_even = multiprocessing.Condition()

    def run(self):
        with self.condition:
            self.condition.acquire()
            while self.pool:
                if not self.first_start:
                    self.condition.wait()
                self.first_start = False
                sleep(0.005)
                self.condition_opposite.acquire()
                if self.pool:
                    if self.even == common.is_even(self.pool[-1]):
                        print(self.message_template.format(self.pool.pop()))
                self.condition_opposite.notify()
                self.condition_opposite.release()
            self.condition.release()

    @property
    def condition(self):
        if self.even:
            return self.condition_even
        return self.condition_odd

    @property
    def condition_opposite(self):
        if not self.even:
            return self.condition_even
        return self.condition_odd
