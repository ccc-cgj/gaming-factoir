__author__ = "Vibius_Vibidius_Zosimus"


# welcome message
print("Hello! Welcome to Tower of Hanoni!")
diffi = int(input("Enter difficulty (2 ~ 64): "))

diffi_range = []
for jerry in range(2, 65):
    diffi_range.append(jerry)

while diffi not in diffi_range:
    print(":( try again")
    diffi = int(input("Enter difficulty (2 ~ 64): "))

# initiate piles
pile1 = []
for jerry in range(1, diffi + 1):
    pile1.append(jerry)
pile2 = []
pile3 = []

# initiate game
game_on = True
times = 0
chances = pow(2, diffi) + 9

while game_on:
    times += 1

    print("You have", chances - times + 1, "moves left")

    # print current piles
    print("pile 1:", pile1, "\npile 2:", pile2, "\npile 3:", pile3)

    # player input 1
    first_pile = int(input("Enter number of pile picked from: "))
    while first_pile == '' or first_pile not in [1, 2, 3]:
        if first_pile == '':
            print("error: no input")
        elif first_pile not in [1, 2, 3]:
            print("error: no such pile")
        else:
            print("error, this is python's fault")
        first_pile = int(input("Enter number of pile picked from: "))

    # player input 2
    second_pile = int(input("Enter number of pile placed onto: "))
    while second_pile == '' or second_pile not in [1, 2, 3] or second_pile == first_pile:
        if second_pile == '':
            print("error: no input")
        elif second_pile not in [1, 2, 3]:
            print("error: no such pile")
        elif second_pile == first_pile:
            print("error: same pile")
        else:
            print("error: blame python")
        second_pile = int(input("Enter number of pile placed onto: "))

    if first_pile == 1:
        temp_pile_one = pile1
    elif first_pile == 2:
        temp_pile_one = pile2
    elif first_pile == 3:
        temp_pile_one = pile3

    if second_pile == 1:
        temp_pile_two = pile1
    elif second_pile == 2:
        temp_pile_two = pile2
    elif second_pile == 3:
        temp_pile_two = pile3

    if temp_pile_two == [] or temp_pile_one[0] < temp_pile_two[0]:
        temp_pile_two.reverse()
        temp_pile_two.append(temp_pile_one.pop(0))
        temp_pile_two.reverse()
    else:
        print("error: no-can-do")
        times -= 1

    if first_pile == 1:
        pile1 = temp_pile_one
    elif first_pile == 2:
        pile2 = temp_pile_one
    elif first_pile == 3:
        pile3 = temp_pile_one

    if second_pile == 1:
        pile1 = temp_pile_two
    elif second_pile == 2:
        pile2 = temp_pile_two
    elif second_pile == 3:
        pile3 = temp_pile_two

    if pile1 == [] and pile2 == []:
        print("yay!")
        game_on = False
    elif pile1 == [] and pile3 == []:
        print("yay!")
        game_on = False
    elif times > pow(2, int(diffi)) + 8:
        print("nooooo! you lost!")
        game_on = False
    else:
        print("game still on\n")
