#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

import threading

from common import is_even, BaseOddEven


class OddEven(BaseOddEven, threading.Thread):
    event_even = threading.Event()
    event_odd = threading.Event()

    def run(self):
        if not self.even:
            self.event.set()
        while self.pool:
            self.event.wait()
            if self.pool:
                if self.even == is_even(self.pool[-1]):
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
