def fibonacci_n(num):
    cdef long long result, prev_results_0, prev_results_1
    if num == 0:
        return 0

    if num > 0:
        prev_results_0 = 0
        prev_results_1 = 0
        for _ in xrange(num):
            result = prev_results_0 + prev_results_1 or 1
            prev_results_0, prev_results_1 = prev_results_1, result
        return result
    return -1
