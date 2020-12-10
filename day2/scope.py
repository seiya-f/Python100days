def spam():
    eggs = 99
    bacon()     #別のローカルスコープでeggsに0が代入される
    print(eggs) #99を出力

def bacon():
    ham = 101
    eggs = 0
    
spam()
