#!/usr/bin/env python3
"""Advanced Python Courses. Homework #5"""

import asyncio
import multiprocessing
import socket
import sys

HOST = 'localhost'
MANAGER = multiprocessing.Manager()

PRIME_CACHE = MANAGER.dict({1: True, 2: True})
STATRS_PORT = MANAGER.dict({9555: None,
                            9556: None,
                            9557: None,
                            9558: None})


def is_prime(number: int) -> bool:
    if number < 1 or number % 1:
        raise ValueError('Invalid value for number: %s\n'
                         'Argument must be a natural number.' % number)
    prime = PRIME_CACHE.get(number, None)
    if prime is not None:
        return prime
    prime = True
    for sub_num in range(2, number):
        if not number % sub_num:
            prime = False
            break
        if sub_num > number // sub_num:
            break
    PRIME_CACHE[number] = prime
    return prime


def is_prime_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, port))
    sock.listen(5)
    while True:
        STATRS_PORT[port] = True
        connection, _ = sock.accept()
        number = int(connection.recv(1024).decode())
        result = is_prime(number)
        connection.send(str(1 if result else 0).encode())
        connection.close()


async def async_is_prime(number):
    port = None
    while not port:
        for key, value in STATRS_PORT.items():
            if value:
                port = key
                break
    STATRS_PORT[port] = False
    connection = socket.create_connection((HOST, port))
    connection.send(str(number).encode())
    data = await LOOP.sock_recv(connection, 1024)
    connection.close()
    return bool(int(data.decode()))


async def prime_range_sum(*range_):
    result = 0
    for num in range(*range_):
        if await async_is_prime(num):
            result += num
    return result


if __name__ == '__main__':
    try:
        SERVERS = [multiprocessing.Process(target=is_prime_server, args=(p,))
                   for p in STATRS_PORT.keys()]
        for server in SERVERS:
            server.start()
        LOOP = asyncio.get_event_loop()
        print(LOOP.run_until_complete(
            prime_range_sum(*(int(x) for x in sys.argv[1:]))
        ))
    finally:
        for server in SERVERS:
            server.terminate()
