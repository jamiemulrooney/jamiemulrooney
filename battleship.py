ship_positions = []

hit_or_miss = []

def display():
    global ship_positions
    return ship_positions


def start_new(b_start, s_start, d_start):
    for i in range(20):
        ship_positions.append('_')


    b_start = b_start - 1
    print(f'b_start: {b_start}')
    for i in range(b_start, b_start+4):
        ship_positions[i] = 'B'



    s_start = s_start - 1
    print(f's_start: {s_start}')
    for i in range(s_start, s_start+3):
        ship_positions[i] = 'S'

    d_start = d_start - 1
    print(f'd_start: {d_start}')
    for i in range(d_start, d_start+2):
        ship_positions[i] = 'D'


    return ship_positions



def guess(predict):
    global ship_positions
    global hit_or_miss
    predict = ''
    predict = predict - 1
    position = int(predict)
    if ship_positions[position] != '_':
        print('HIT')
        ship_positions[position] = 'H'

        
    else:
        print('MISS')
        ship_positions[position] = 'M'
        


    return ship_positions


def display_guesses():
    global ship_positions
    global hit_or_miss
    lenght = len(ship_positions)
    for i in range(lenght):
        if ship_positions[i] == 'H':
            x = 'H'
            add_hit = int(x)
            hit_or_miss.append(add_hit)
        else:
            x = 'M'
            add_miss = int(x)
            hit_or_miss.append(add_miss)

    return hit_or_miss



    
