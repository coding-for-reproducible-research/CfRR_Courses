import time
from concurrent.futures import ProcessPoolExecutor

def main():
    start_time = time.perf_counter()
    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(fibonacci, [30]*100)
    run_time = time.perf_counter() - start_time
    print(f"Run time was {run_time} seconds")

def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    main()

