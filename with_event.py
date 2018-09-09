#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

import multiprocessing

import common


class OddEven(common.BaseOddEven, multiprocessing.Process):
    event_even = multiprocessing.Event()
    event_odd = multiprocessing.Event()

    def run(self):
        if self.even:
            self.event_opposite.set()
        while self.pool:
            self.event.wait()
            self.event.clear()
            if self.pool:
                if self.even == common.is_even(self.pool[-1]):
                    print(self.message_template.format(self.pool.pop()))
            self.event_opposite.set()

    @property
    def event(self):
        if self.even:
            return self.event_even
        return self.event_odd

    @property
    def event_opposite(self):
        if self.even:
            return self.event_odd
        return self.event_even
