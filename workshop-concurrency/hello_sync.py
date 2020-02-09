from time import sleep


def hello():
    print('Hello')
    sleep(3)
    print('World')


def main():
    for _ in range(3):
        hello()


if __name__ == '__main__':
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in  {elapsed:0.2f} seconds.")
