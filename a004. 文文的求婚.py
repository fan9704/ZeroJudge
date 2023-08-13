def func(num: int) -> str:
    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        return "閏年"
    else:
        return "平年"


while True:
    try:
        print(func(int(input())))
    except EOFError:
        break
