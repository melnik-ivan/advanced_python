import contextlib
from decimal import Decimal
import time


@contextlib.contextmanager
def benchmark(name, log_file):
    row_template = '{name:25}{result}\n'
    start_time = time.perf_counter()
    yield
    end_time = time.perf_counter()
    result = round(Decimal(end_time - start_time), 5)
    row = row_template.format(name = name,
                              result = result)
    with open(log_file, 'a') as log:
        log.write(row)
