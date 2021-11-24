class kasr:

    def __init__(self,a=0,b=None):
       self.a=a
       if b!=0:
            self.b=b
       else:
           self.b=1
        
    
    def show(self):
        print(self.a,"/",self.b)

    def sum(self,other):
        result=kasr()
        result.a=self.a*other.b + self.b*other.a
        result.b=self.b*other.b
        return result

    def mul(self,x,y):
        soorat=x.a * y.a
        makhraj=x.b * y.b
        result=kasr(soorat,makhraj)
        return result

    def sub(self,other):
        result=kasr()
        result.a=self.a*other.b - self.b*other.a
        result.b=self.b*other.b
        return result

    def dive(self,other):
        result=kasr()
        result.a=self.a * other.b
        result.b=self.b * other.a
        return result

    def simple(self):
        if self.a > self.b: 
         small = self.b
        else: 
         small = self.a 
        for i in range(1, small+1): 
         if((self.a % i == 0) and (self.b % i == 0)): 
            bmm = i 

        result=kasr()
        result.a=int(self.a/bmm)
        result.b=int(self.b/bmm)
        
        return result



def menue():
    print(""" chose one:
    1->Addition of two fractions
    2->Multiply two fractions
    3->Subtraction of two fractions
    4->Divide into two fractions
    5->Exit""")
#def Get_values():
    #print("sorat kasr ra vared konid:")
    #numerator=int(input())
    #print("makhraj kasr ra vared konid:")
    #Denominator=int(input())
while True:
    menue()
    
    c=int(input())
    if c==5:
       break
    print("sorat kasr1 ra vared konid:")
    numerator1=int(input())
    print("makhraj kasr1 ra vared konid:")
    Denominator1=int(input())

    k1=kasr(numerator1,Denominator1)
    k1.show()

    print("sorat kasr1 ra vared konid:")
    numerator2=int(input())
    print("makhraj kasr1 ra vared konid:")
    Denominator2=int(input())

    k2=kasr(numerator2,Denominator2)
    k2.show()
   
    if c==1:
        k_1=k1.simple()
        k_2=k2.simple()
        res=k_1.sum(k_2)
        rslt=res.simple()
        print("result is:")
        
        rslt.show()

    elif c==2:
        k_1=k1.simple()
        k_2=k2.simple()
        res=k_1.mul(k_1,k_2)
        rslt=res.simple()
        #print(k1.show ,"*",k2.show,"=",end="\n")
        print("result is:")
        rslt.show()

    elif c==3:
        k_1=k1.simple()
        k_2=k2.simple()
        res=k_1.sub(k_2)
        #rslt=res.simple()
        print("result is:")
        
        res.show()

    elif c==4:
        k_1=k1.simple()
        k_2=k2.simple()
        res=k_1.dive(k_2)
        rslt=res.simple()
        print("result is:")
        
        rslt.show()

    

    