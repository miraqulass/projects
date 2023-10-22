import random

def display(room):
    print(room)

room = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]
print("All the rooms are dirty")
display(room)

x = 0
y = 0

while x < 6:
    while y < 6:
        room[x][y] = random.choice([0,1])
        y += 1
    x += 1
    y = 0

print("Before cleaning the room I detect all of these random dirt")
display(room)
x = 0
y = 0
z = 0
while x < 6:
    while y < 6:
        if room[x][y] == 1:
            print("Vacuum in this location now,",x, y)
            room[x][y] = 0
            print("cleaned", x, y)
            z += 1
        y += 1
    x += 1
    y = 0
pro = (100-((z/36)*100))
print("Room is clean now, Thanks for using : 3710933")
display(room)
print('performance=',pro,'%')



# def getdpos(board):
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == 'd':
#                 return [i,j]
# def nextMove(posr, posc, board):
#     di,dj = getdpos(board)
#     if posr > di:
#         print ('Vacuum has moved UP')
#     elif posr < di:
#         print ('Vacuum has moved DOWN')
#     else:
#         if posc > dj:
#             print ('Vacuum has moved LEFT')
#         elif posc < dj:
#             print ('Vacuum has moved RIGHT')
#         else:
#             print ('The room is CLEAN')
# if _name_ == "_main_":
#     pos = [int(i) for i in input().strip().split()]
#     board = [[j for j in input().strip()] for i in range(3)]
#     nextMove(pos[0], pos[1], board)\