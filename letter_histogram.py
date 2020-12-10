word = input('Enter a Word! ')
word = word.lower

letter_histogram = {}

while True:
    count = 0
    try:
        word.remove('a')
        count += 1
    except: 
        if count > 0:
            letter_histogram['a'] = count
        break

print(letter_histogram)