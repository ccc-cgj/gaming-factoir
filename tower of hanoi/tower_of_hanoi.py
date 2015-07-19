pile1 = []
for jerry in range(1, 5):
    pile1.append(jerry)
pile2 = []
pile3 = []

game_on = True
times = 0
print(pile2 == [])

while game_on:
    times += 1

    print("pile 1:", pile1, "\npile 2:", pile2, "\npile 3:", pile3)

    first_pile = ''
    while first_pile == '' or first_pile not in ['1', '2', '3']:
        first_pile = input("Enter number of pile picked from: ")
    second_pile = ''
    while second_pile == '' or second_pile not in ['1', '2', '3'] or second_pile == first_pile:
        second_pile = input("Enter number of pile placed onto: ")

    if first_pile == '1':
        temp_pile_one = pile1
    elif first_pile == '2':
        temp_pile_one = pile2
    elif first_pile == '3':
        temp_pile_one = pile3

    if second_pile == '1':
        temp_pile_two = pile1
    elif second_pile == '2':
        temp_pile_two = pile2
    elif second_pile == '3':
        temp_pile_two = pile3

    if temp_pile_two == [] or temp_pile_one[0] < temp_pile_two[0]:
        temp_pile_two.reverse()
        temp_pile_two.append(temp_pile_one.pop(0))
        temp_pile_two.reverse()

    if first_pile == '1':
        pile1 = temp_pile_one
    elif first_pile == '2':
        pile2 = temp_pile_one
    elif first_pile == '3':
        pile3 = temp_pile_one

    if second_pile == '1':
        pile1 = temp_pile_two
    elif second_pile == '2':
        pile2 = temp_pile_two
    elif second_pile == '3':
        pile3 = temp_pile_two

    if pile1 == [] and pile2 == []:
        game_on = False
    elif pile1 == [] and pile3 == []:
        game_on = False
    elif times > 34:
        game_on = False
    else:
        print("game still on", times)
