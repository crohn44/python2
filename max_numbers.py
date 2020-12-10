# Small Excersize #2
numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6]

max_numbers = max(numbers)
print(max_numbers)

min_numbers = min(numbers)
print(min_numbers)

even_numbers = numbers
for number in even_numbers:
    if number % 2 == 0:
        print(number)

positive_numbers = numbers
for number in positive_numbers:
    if number > 0:
        print(number) 

positive_numbers2 = numbers
for number in positive_numbers2:
    if number <= 0:
        positive_numbers2.remove(number) 
print(positive_numbers2)

multiply_numbers = 2*numbers
print(multiply_numbers)