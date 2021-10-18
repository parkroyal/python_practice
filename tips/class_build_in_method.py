"""
__str__() 方法 (method) 是類別 (class) 的預設方法之一，這是物件 (object) 的字串 (string) 表達形式。
不同的物件利用內建函數 (built-in function) print() 會印出他們各自的字串表達形式，例如這裡整數 22 ，浮點數 22.0 ，字串 "22" ，以及含有一個整數 22 的串列 (list)
"""
# a = 22
# print(a)
# a = 22.0
# print(a)
# a="22"
# print(a)
# a = [22]
# print(a)
# print(a.__str__())

"""如果是印出自行定義的物件實體 (instance) ，例如這邊用 Demo() 建立的變數 (variable) d ，預設會印出類別名稱及實體物件所在的記憶體位址
想要印出物件專屬或是自行設定的訊息，這就得重新定義 __str__() 方法了，例如這邊 Demo2 類別的 __str__() 方法回傳屬性 i 的字串形式"""
class Demo:
    def __init__(self, i):
        self.i = i

# d = Demo(9527)
# print(d)
# print(d.__str__())

class Demo:
    def __init__(self, i):
        self.i = i
    def __str__(self) -> str:
        return str(self.i)

d = Demo(9527)
print(d)
