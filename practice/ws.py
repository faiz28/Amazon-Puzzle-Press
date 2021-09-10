from hashlib import new
import random
import string

from pprint import pprint

handle = open('/etc/dictionaries-common/words')
words = handle.readlines()
handle.close()

words = [ random.choice(words).upper().replace("'",'').strip() for _ in range(5)]

grid_size = 20

grid = [ [ '_' for _ in range(grid_size)] for _ in range(grid_size)]

def print_grid():
    for x in range(grid_size):
        print('-\t'*5 + ' '.join(grid[x]))

print_grid()

orientatios = [ 'leftright', 'updown', 'diagonalup','diagonaldown' ]

for word in words:
    word_length = len(word)
    print(word_length)

    placed = False
    while not placed:
        orientation = random.choice(orientatios)

        if orientation == 'leftright':
            step_x = 1
            step_y = 0
        if orientation == 'updown':
            step_x = 0
            step_y = 1
        if orientation == 'diagonaldown':
            step_x = 1
            step_y = 1
        if orientation == 'diagonalup':
            step_x = 1
            step_y = -1

        x_position = random.randint(0,grid_size)
        y_position = random.randint(0,grid_size)

        ending_x = x_position + word_length*step_x
        ending_y = y_position + word_length*step_y

        if ending_x<0 or ending_x >= grid_size: continue
        if ending_y<0 or ending_y >= grid_size: continue

        failed = False

        for i in range(word_length):
            character = word[i]

            new_position_x = x_position + i*step_x
            new_position_y = y_position + i*step_y

            character_at_new_position = grid[new_position_x][new_position_y]

            if character_at_new_position != '_':
                if character_at_new_position == character:
                    continue
            else:
                failed = True
                break
        
        if failed:
            continue
        else:
            for i in range(word_length):
                character = word[i]

                new_position_x = x_position +i*step_x
                new_position_y = y_position +i*step_y

                grid[new_position_x][new_position_y] = character
            
            placed = True