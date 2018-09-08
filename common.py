#!/usr/bin/env python3
"""Advanced Python Courses. Homework #3"""


def is_even(num):
    return not num % 2


class BaseOddEven(object):
    _even_by_name = {
        'EVEN': True,
        'ODD': False,
    }

    def __init__(self, pool, name, *args, **kwargs):
        super().__init__(name=name, *args, **kwargs)
        self._name = name
        self.pool = pool
        self.even = self.even_by_name()
        self._message_template = None
        self.first_start = self.even

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, value):
        self._name = value

    @property
    def message_template(self):
        if not self._message_template:
            self._message_template = '{:4} worker pops: {}'.format(
                self.name,
                '{:>3}',
            )
        return self._message_template

    def even_by_name(self):
        even = self._even_by_name.get(self.name, None)
        if even is None:
            raise ValueError('Invalid name: %s' % self.name)
        return even


class Example(object):
    def __init__(self, name, worker_class):
        if len(name) > 80:
            raise ValueError('Example name must be shorter than 80 symbols')
        self.name = name
        self.worker_class = worker_class
        self.edge_sym = '='
        self.edge_size = 80

    @property
    def edge(self):
        left_edge_len = (self.edge_size - len(self.name)) // 2
        right_edge_len = self.edge_size - left_edge_len - len(self.name)
        return '{}{}{}'.format(
            self.edge_sym * left_edge_len,
            self.name,
            self.edge_sym * right_edge_len
        )

    def run(self):
        print(self.edge)
        pool = [x for x in range(100, -1, -1)]
        workers = (
            self.worker_class(pool, 'EVEN'),
            self.worker_class(pool, 'ODD'),
        )
        for worker in workers:
            worker.start()
        for worker in workers:
            worker.join()
            print('Worker "{}" finished work'.format(worker.name))
