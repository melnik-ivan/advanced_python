#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

import sys

from common import Example

import with_condition
import with_event
import with_lock
import with_semaphore

EXAMPLES = [
    Example('Process with lock', with_lock.OddEven),
    Example('Process with condition', with_condition.OddEven),
    Example('Process with semaphore', with_semaphore.OddEven),
    Example('Process with event', with_event.OddEven),
]

EXAMPLE_BY_NAME = {
    example.name: example for example in EXAMPLES
}


def main(*example_names):
    if not example_names:
        examples = EXAMPLES
    else:
        examples = [
            EXAMPLE_BY_NAME[example] for example in example_names
        ]
    for example in examples:
        example.run()


if __name__ == '__main__':
    main(*sys.argv[1:])
