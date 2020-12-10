def spam(divide_by):
    try:                        #try節でエラーが起こるとexcept節に移行する
        return 42 / divide_by
    except ZeroDivisionError:
        print('エラー：不正な引数です。')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divide_by):
    return 42 / divide_by

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))              #ここでエラー
    print(spam(1))              #except節に移行するため実行されない
except ZeroDivisionError:
    print('エラー：不正な引数です。')
