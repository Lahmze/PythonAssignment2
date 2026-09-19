import random

def main():

    numbers = [random.uniform(0, 10) for _ in range(5)]
    print("Generated numbers:")
    for num in numbers:
        print(f"  {num:.4f}")

    minimum = min(numbers)
    maximum = max(numbers)

    print(f"\nMinimum value: {minimum:.4f}")
    print(f"Maximum value: {maximum:.4f}")

if __name__ == '__main__':
    main()