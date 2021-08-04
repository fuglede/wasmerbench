#pythran export collatz(int)
def collatz(target):
    start = 1
    while True:
        i = start
        # One has to be very careful about how to set steps here; moving it a tiny bit,
        # will cause Pythran to generate invalid code:
        # https://github.com/serge-sans-paille/pythran/issues/1861
        steps = 0
        while i != 1:
            i = i // 2 if i % 2 == 0 else 3 * i + 1
            steps += 1
        if steps == target:
            return start
        start += 1
