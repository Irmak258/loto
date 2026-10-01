from random import randint

column_count = int(input("Enter the number of columns: "))

fixed_number = int(input("Enter your fixed number (0 if none): "))

forbidden_numbers = []

forbidden = input("Enter the numbers you do not want to play: ")

if forbidden != "":
    for i in forbidden.split(","):
        forbidden_numbers.append(int(i))

columns = []

for i in range(column_count):

    column = []

    if fixed_number != 0:
        column.append(fixed_number)

    while len(column) < 6:

        number = randint(1, 90)

        if number not in column and number not in forbidden_numbers:
            column.append(number)

    column.sort()

    while column in columns:

        column = []

        if fixed_number != 0:
            column.append(fixed_number)

        while len(column) < 6:

            number = randint(1, 90)

            if number not in column and number not in forbidden_numbers:
                column.append(number)

        column.sort()

    columns.append(column)


print("Lottery Coupon:")

for i in range(column_count):
    print(i + 1, ". column:", columns[i])
