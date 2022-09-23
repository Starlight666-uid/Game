print ("-------Приветствуем вас в игре в крестики-нолики-------")
print("---Правила игры будут выведены ниже для ознакомления---")
print("----------Если вы конечно с ней и не знакомы----------")
print(" ----Каждый игрок выбирает для себя крестик либо нолик----")
print("----И по очерёдно ставит выбранный собой знак в пустое поле----")
print("----Побеждает тот, кто соберёт 3 своих знака по диагонали, вертикали, или горизонатали----")

field = [ [" " , " " ,  " "],
        [" " ," " ," "],
        [" " , " " , " "]
]

def show():
    print()
    print("     | 0 | 1 | 2 |")
    print(f"  ----------------- ")
    for i, row in enumerate(field):
        row_str = f"   {i} | {' | '.join (row)} | "
        print(row_str)
        print(" ------------------")
    print()

def ask():
    while True:
        x, y = map(int, input("         Ваш ход: ").split())

        if 0 > x or x > 2 or 0 > y or y > 2 :
            print("Координаты вне диапазона!")
            continue
        if field[x][y] != " ":
            print (" Клетка занята! ")
            continue
        return  x, y

count = 0
while True:
    count += 1

    show()

    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print ("Ходит нолик")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if count == 9:
        print("Ничья")
        break


def win_list():
    win_check =  [((0,0),(0,1),(0,2)) , ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
               ((0,2),(1,1),(2,0)) , ((0,0),(1,1),(2,2)), ((0,0),(1,0),(2,0)),
               ((0,1),(1,1),(2,1)) , ((0,2),(1,2),(2,2))]
    for cord in win_list:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

