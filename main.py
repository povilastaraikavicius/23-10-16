# squares = [number * number for number in range(10) if number != 5]
# print(squares)

# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)

# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A")])

# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A") or "e" in name])


# squares = [number * number for number in range(10) if number % 2 == 0]
# print(squares)




# Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.

# squares = [ number for number in range(1, 1000) if number % 6 == 0]
# print(squares)


# Raskite visus skaičius iš 1-1000, kuriuose yra 9.


squares = [number for number in range(1, 1000) if "9" in str(number)]
print(squares)
