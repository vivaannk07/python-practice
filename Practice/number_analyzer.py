def analyze_numbers(numbers):

    total = sum(numbers)
    average = total / len(numbers)
    largest = max(numbers)
    smallest = min(numbers)

    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    print("\nAnalysis Result:")
    print("Numbers:", numbers)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)


def main():

    numbers = []

    n = int(input("How many numbers do you want to enter? "))

    for i in range(n):
        num = int(input("Enter number: "))
        numbers.append(num)

    analyze_numbers(numbers)


main()