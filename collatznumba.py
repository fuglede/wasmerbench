from numba import njit


@njit
def collatz(target):
    start = 1
    while True:
        i = start
        steps = 0
        while i != 1:
            i = i // 2 if i % 2 == 0 else 3 * i + 1
            steps += 1
        if steps == target:
            return start
        start += 1
