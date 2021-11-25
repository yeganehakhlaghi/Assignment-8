class number:
    def __init__(self , a=0, b=0):
        self.a=a
        self.b=b

    def show(self):
        print(self.a,"+",self.b,"i")
    
    def sum(self,other):
        result=number()
        result.a=self.a+other.a
        result.b=self.b+other.b
        return result

    def mul(self,other):
        result=number()
        result.a = (self.a*other.a) - (self.b*other.b)
        result.b = self.b*other.a + self.a*other.b
        return result

    def sub(self,other):
        result=number()
        result.a=self.a-other.a
        result.b=self.b-other.b
        return result


def menu():
    print("""choose one: 
    1->Add two complex numbers
    2->Multiply two complex numbers
    3->Subtraction of two complex numbers
    4->exit""")

while True:
    menu()
    k=int(input())
    if k==4:
        break
    R1=int(input("Enter the real part of the number1:"))
    I1=int(input("Enter the imaginary part of the number1:"))
    num1=number(R1,I1)
    num1.show()
    
    R2=int(input("Enter the real part of the number2:"))
    I2=int(input("Enter the imaginary part of the number2:"))
    num2=number(R2,I2)
    num2.show()

    if k==1:
        res=num1.sum(num2)
        print("The result is:")
        res.show()

    if k==2:
        res=num1.mul(num2)
        print("The result is:")
        res.show()

    if k==3:
        res=num1.sub(num2)
        print("The result is:")
        res.show()

    
#num1=number(2,3)
#num1.show()
