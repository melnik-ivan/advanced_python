import os
import sys

from fibonacci_py.fibonacci import fibonacci_n as fibonacci_n_py
from fibonacci import fibonacci_n as fibonacci_n_c
from fibonacci_pyx import fibonacci_n as fibonacci_n_pyx
from tools.benchmark import benchmark

LOG_FILE = 'benchmark.log'


def main(fib_number=93, iters=100):
    fib_number = int(fib_number)
    iters = int(iters)
    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, 'a') as log:
            log.write('=' * 80)
            log.write('\n')

    with open(LOG_FILE, 'a') as log:
        log.write('FIB NUMBER: {}, ITERS: {}\n'.format(fib_number, iters))

    with benchmark('With C extension', LOG_FILE):
        for _ in range(iters):
            fibonacci_n_c(fib_number)

    with benchmark('With Cython extension', LOG_FILE):
        for _ in range(iters):
            fibonacci_n_pyx(fib_number)

    with benchmark('With pure python 3', LOG_FILE):
        for _ in range(iters):
            fibonacci_n_py(fib_number)

if __name__ == '__main__':
    main(*sys.argv[1:])
