class arthemetic_operations:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return self.a-self.b
    
    def mul(self,a,b):
        return self.a*self.b
    
    def div(self,a,b):
        return self.a/self.b
    
    def mod(self,a,b):
        return self.a%self.b
    
    def power(self,a,b):
        return self.a**self.b   

arthemetic_operation = arthemetic_operations(10,5)
print(arthemetic_operation.add(10,5))
print(arthemetic_operation.sub(20,5))
print(arthemetic_operation.mul(10,5))
print(arthemetic_operation.div(10,5))
print(arthemetic_operation.mod(10,5))
print(arthemetic_operation.power(10,5))
