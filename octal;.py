def octaal(num):
    if num < 8:
        return str(num)
    else:
        return octaal(num //8) + octaal(num % 8)

number = int(input())
print(octaal(number))
