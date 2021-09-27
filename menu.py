import battleship

selection = ' '
while selection != '5':
    print('1.Start new game (enter ship locations) : ')
    print('2.View ships')
    print('3.Make a new guess')
    print('4.View hits/misses')
    print('5.Exit')

    selection = input('enter option 1-5: ')

    if selection == '1': 
        b_start = int(input('Emter the ship position of ship B: '))
        s_start = int(input('Emter the ship position of ship S: '))
        d_start = int(input('Emter the ship position of ship D: '))
        battleship.start_new(b_start, s_start, d_start)


    if selection == '2':
        answer = battleship.display()
        print(answer)

    if selection == '3':
        whats_your_guess = int(input('take a guess:'))
        battleship.guess(whats_your_guess)

    if selection == '4':
        answer2 = battleship.display_guesses()
        print(answer2)
        