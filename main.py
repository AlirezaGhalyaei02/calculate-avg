def calculate_avg():
    while True:
        try:
            numbers = list(map(float, input().split()))

            if not numbers:
                raise ValueError

            break

        except ValueError:
            print("Invalid Input! Enter a valid input.")

    return sum(numbers) / len(numbers)


print(f"{calculate_avg():.2f}")
