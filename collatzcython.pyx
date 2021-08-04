cpdef int collatz(int target):
    cdef int start, i, steps
    start = 1
    while True:
        i = start
        steps = 0
        while True:
            if i == 1:
                break
            i = i // 2 if i % 2 == 0 else 3 * i + 1
            steps += 1
        if steps == target:
            return start
        start += 1
