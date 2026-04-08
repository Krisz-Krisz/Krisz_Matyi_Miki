def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number using an iterative method.

    This avoids exponential recursion and can compute large indices like 900 quickly.
    """
    if n < 0:
        raise ValueError("Fibonacci index must be a non-negative integer.")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main() -> None:
    try:
        user_input = input("Enter the Fibonacci index to compute (non-negative integer): ")
        index = int(user_input)
        result = fibonacci(index)
        print(f"Fibonacci({index}) = {result}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
