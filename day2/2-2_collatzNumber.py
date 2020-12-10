#3.11 (p78)

def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    elif number % 2 == 1:
        return int(3 * number + 1)

try:
    print('整数を入力してください。')
    number = int(input())
except ValueError:
    print('整数を入力してください。')
    number = int(input())

print(number)
while number != 1:
    number = collatz(number)
    print(number)

#無限ループを用いた別解

#while True:
#    print(number)
#    number = collatz(number)
#
#    if number == 1:
#        break
#
#print(1)
