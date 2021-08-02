# Computer guess number using binary search

play_game = 'y'
start = 1    # Change to any number
end = 100    # Change to any number
direction = 'N'
smallest = start
largest = end

# Game code starts here
while play_game == 'y':
    smallest = start
    largest = end
    print("Guess a number between 1 and 100:")
    try_number = end//2
    print(try_number)
    counter = 0
    direction = 'N'

    while direction != 'c':
        direction = input('Is it too large (l), too small(s), or correct(C)? ')
        if direction == 's':
            if try_number > smallest:
                smallest = try_number + 1
                try_number = (smallest + largest)//2
            print(try_number)
        if direction == 'l':
            if try_number < largest:
                largest = try_number - 1
                try_number = (smallest + largest)//2
            print(try_number)
        counter = counter + 1
    print('I got it! I tried ' + str(counter) + ' times.')
    play_game = input('Continue? ')

# Enjoy :)
