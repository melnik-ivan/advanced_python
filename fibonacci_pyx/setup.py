from Cython.Build import cythonize
from distutils.core import setup

setup(
    version='1.0',
    description='Calculate n-th Fibonacci number with Cython Extension',
    ext_modules=cythonize("fibonacci_pyx.pyx")
)
