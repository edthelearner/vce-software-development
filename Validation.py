while True:
    try:
        age = int(input('How old are you? '))
        break
    except ValueError:
        print('Please enter a whole number')

print('Your age is: ' + str(age))

#Reference: http://www.easypythondocs.com/validation.html
