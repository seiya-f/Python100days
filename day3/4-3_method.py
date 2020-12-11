#リストのメソッドは文字列や定数の値に対しては呼び出せない
spam = ['a', 'b', 'c', 'd']

spam.index('c')     #'c'のインデックスを出力

spam.append('e')    #'e'を末尾に追加

spam.insert(5, 'f') #'f'をインデックス5に挿入

spam.remove('c')    #'c'を削除

spam.sort()         #リストの値をソート

spam.sort(reverse=True)         #リストの値を逆順にソート

