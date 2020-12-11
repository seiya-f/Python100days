#文字列や整数
spam = 42
cheese = spam               #spamに格納された値が代入される

spam = 100      #cheeseの中のspamは42のままである



#リストでは
spam = [0, 1, 2, 3, 4, 5]
cheese = spam               #spamというリストの参照が代入されている

cheese[1] = 'j'             #spamとcheeseの出力結果は一致する
