class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b!=0:
            return a/b
        else:
            return ("the division is not possible")
# object creation
Cal=Calculator()
print(Cal.add(4,5))
print(Cal.sub(4,5))
print(Cal.mul(4,5))
print(Cal.div(4,5))
