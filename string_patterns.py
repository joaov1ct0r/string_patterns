def pattern_1(amount: int) -> None:
    for i in range(amount):
        print("*" * amount)

def pattern_2(amount: int) -> None:
    for i in range(amount + 1):
        print("*" * i)

def pattern_3(amount: int) -> None:
    for i in range(1, amount + 1):
        acc = ""
        for j in range(1, i + 1):
            acc  += str(j)
        print(acc)

def pattern_4(amount: int) -> None:
    for i in range(1, amount + 1):
        acc = ""
        for j in range(1, i + 1):
            acc += str(i)
        print(acc)

def pattern_5(amount: int) -> None:
    for i in range(amount, -1, -1):
        print("*" * i)

def pattern_6(amount: int) -> None:
    for i in range(amount, 0, -1):
        acc = ""
        for j in range(1, i + 1):
            acc += str(j)
        print(acc)

def pattern_7(amount: int) -> None:
    width = (amount * 2) - 1
    acc = ""
    for j in range(1, amount * 2, 2):
        obs_acc = str("*" * j).center(width)
        acc += obs_acc + "\n"
    print(acc)

def pattern_8(amount: int) -> None:
    width = (amount * 2) - 1
    acc = ""
    for i in reversed(range(1, amount * 2, 2)):
        obs_acc = str("*" * i).center(width)
        acc += obs_acc + "\n"
    print(acc)

def pattern_9(amount: int) -> None:
    width = (amount * 2) - 1
    acc = ""
    for j in range(1, amount * 2, 2):
        obs_acc = str("*" * j).center(width)
        acc += obs_acc + "\n"

    for i in reversed(range(1, amount * 2, 2)):
        obs_acc = str("*" * i).center(width)
        acc += obs_acc + "\n"
    print(acc)

def pattern_10(amount: int) -> None:
    for i in range(1, amount + 1):
        print("*" * i)

    for j in reversed(range(1, amount, 1)):
        print("*" * j)

def pattern_11(amount: int) -> None:
    for i in range(0, amount):
        acc = ""
        for j in range(0, i + 1):
            acc += bin(j).replace("0b", "")
        print(acc)


if __name__ == "__main__":
    amount = input("Insira a quantidade desejada: ")
    amount = int(amount)
    # pattern_1(amount)
    # pattern_2(amount)
    # pattern_3(amount)
    # pattern_4(amount)
    # pattern_5(amount)
    # pattern_6(amount)
    # pattern_7(amount)
    # pattern_8(amount)
    # pattern_9(amount)
    # pattern_10(amount)
    pattern_11(amount)