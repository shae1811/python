## TASK 1
# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user
five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]
# print(five_by_five_grid)
# first step is to add colum 6 and row 6
# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)
# output the grid with the flipped card
## TASK 2
# given a six by six grid, work out what card was flipped
# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)
# five_by_five_grid.append(['X','0','0','X','X'])
# print(five_by_five_grid)
# for li in five_by_five_grid:
#     five_by_five_grid.append([9])
# print(li)
for list in five_by_five_grid:
    count = 0
    for item in list:
        if item =='X':
            count = count +1
    if count % 2 == 0:
        list.append('0')
    else:
        list.append('X')
# print(five_by_five_grid)



five_by_five_grid.append(five_by_five_grid[4])


counter = 0
for list in five_by_five_grid:
    print (list)
    counter = counter +1