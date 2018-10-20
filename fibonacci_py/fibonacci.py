def fibonacci_n(num):
    if num == 0:
        return 0

    if num > 0:
        prev_results = (0, 0)
        for _ in range(num):
            result = sum(prev_results) or 1
            prev_results = prev_results[1], result
        return result
    return -1
