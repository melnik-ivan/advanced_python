#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

from threading import Thread, Condition
from time import sleep

from common import is_even, BaseOddEven


class OddEven(BaseOddEven, Thread):
    condition_odd = Condition()
    condition_even = Condition()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_start = self.even

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
                    if self.even == is_even(self.pool[-1]):
                        print(self.message_template.format(self.pool.pop()))
                self.condition_opposite.notify()
                self.condition_opposite.release()
            self.condition.release()

    @property
    def condition(self):
        if self.even:
            return self.condition_even
        else:
            return self.condition_odd

    @property
    def condition_opposite(self):
        if not self.even:
            return self.condition_even
        else:
            return self.condition_odd
