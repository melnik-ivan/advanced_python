#!/usr/bin/env python3
"""This module contains example that causes segmentation fault"""

import sys

RECURSION_LIMIT = 50000
sys.setrecursionlimit(RECURSION_LIMIT)


def just_recursion_func():
    """Called self"""
    just_recursion_func()


def main():
    """Runs infinite recursion"""
    just_recursion_func()


if __name__ == '__main__':
    main()
