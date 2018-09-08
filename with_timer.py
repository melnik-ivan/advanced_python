#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

from threading import Thread, Timer
from time import sleep

from common import is_even, BaseOddEven


class OddEven(BaseOddEven, Thread):
    timer_even = None
    timer_odd = None

    def run(self):
        if self.even:
            self.set_timer(0.001)
            self.set_timer_opposite(0.001)
        else:
            sleep(0.1)
        while self.pool:
            if self.timer.is_alive():
                self.timer.join()
            self.set_timer_opposite(0.001)
            if self.pool:
                if self.even == is_even(self.pool[-1]):
                    print(self.message_template.format(self.pool.pop()))

    @property
    def timer(self):
        if self.even:
            return self.timer_even
        return self.timer_odd

    @property
    def timer_opposite(self):
        if self.even:
            return self.timer_odd
        return self.timer_even

    def set_timer(self, timeout):
        if self.even:
            self.__class__.timer_even = Timer(timeout, lambda: None)
        else:
            self.__class__.timer_odd = Timer(timeout, lambda: None)
        self.timer.start()

    def set_timer_opposite(self, timeout):
        if self.even:
            self.__class__.timer_odd = Timer(timeout, lambda: None)
        else:
            self.__class__.timer_even = Timer(timeout, lambda: None)
        self.timer_opposite.start()
