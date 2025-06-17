import time

def main():
    start_time = time.perf_counter()
    for _ in range(100):
        fibonacci(30)
    run_time = time.perf_counter() - start_time
    print(f"Run time was {run_time} seconds")

def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    main()

