from setuptools import Extension
from setuptools import setup


setup(
    name='fibonacci',
    version='1.0',
    description='Calculate n-th Fibonacci number with C Extension',
    ext_modules=[
        Extension(
            'fibonacci',
            sources=['fib.c'],
            py_limited_api=True)
    ],
)
