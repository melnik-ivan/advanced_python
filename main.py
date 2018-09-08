#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""

import sys

from common import Example
import with_lock

EXAMPLES = [
    Example('Thread with lock', with_lock.OddEven),
]

EXAMPLE_BY_NAME = {
    example.name: example for example in EXAMPLES
}


def main(*examples):
    if not examples:
        examples = EXAMPLES
    for example in examples:
        example.run()


if __name__ == '__main__':
    main(*sys.argv[1:])
