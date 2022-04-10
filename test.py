def digit(m):
    last = m % 10
    while m >= 10:
        m = m / 10;
    return int(m) + last
def digit(m):
    print(int(m[0])+int(m[-1]))
num = input("Введіть число: ")
print(digit(num))