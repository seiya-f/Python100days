def eggs(some_parameter):
    some_parameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

#copyモジュールのcopy()やdeepcopy()関数で元の値を変更せずに代入も可能。
