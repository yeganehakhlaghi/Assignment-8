class Time:
    def __init__(self,h=0,m=0,s=0):
        self.h=h
        self.m=m
        self.s=s

    def show(self):
        print(self.h,":",self.m,":",self.s)


    def chek(self):
        
        if self.s>59:
            p=int(self.s/60)
            self.m+=p
            self.s=self.s%60

        if self.m>59:
            p=int(self.m/60)
            self.h+=p
            self.m=self.m%60

        if self.s < 0:
            self.m-=1
            self.s +=60

        if self.m < 0:
            self.h -=1
            self.m+=60

        if self.h<0:
            self.h=0
        #result=Time()

    def sum(self,other):
        result=Time()
        result.h=self.h+other.h
        result.m=self.m+other.m
        result.s=self.s+other.s
        return result

    def sub(self,other):
        result=Time()
        result.s=self.s-other.s
        result.m=self.m-other.m
        result.h=self.h-other.h
        return result
     
    def time_to_sec(self):
        
        
        return (self.h*3600+self.m*60+self.s)




def menu():
    print(""" chose one:
    1->Addition of two Time
    2->Subtraction of two Time
    3->Convert seconds to time
    4->Convert Time to seconds 
    5->Exit""")



while True:
    menu()
    c=int(input())
    
    
    

    if c==1:
        print("for Time1:")
        hour1=int(input("Enter hour:"))
        minute1=int(input("Enter minuter:"))
        second1=int(input("Enter second:"))

        t1=Time(hour1,minute1,second1)
        t1.chek()
        t1.show()

        print("for Time2:")
        hour2=int(input("Enter hour:"))
        minute2=int(input("Enter minuter:"))
        second2=int(input("Enter second:"))

        t2=Time(hour2,minute2,second2)
        t2.chek()
        t2.show()

        res=t1.sum(t2)
        res.chek()
        res.show()
    elif c==2:
        print("for Time1:")
        hour1=int(input("Enter hour:"))
        minute1=int(input("Enter minuter:"))
        second1=int(input("Enter second:"))

        t1=Time(hour1,minute1,second1)
        t1.chek()
        t1.show()

        print("for Time2:")
        hour2=int(input("Enter hour:"))
        minute2=int(input("Enter minuter:"))
        second2=int(input("Enter second:"))

        t2=Time(hour2,minute2,second2)
        t2.chek()
        t2.show()

        res=t1.sub(t2)
        res.chek()
        res.show()
    elif c==3:
        #print("for Time1:")
        hour=int(input("Enter hour:"))
        minute=int(input("Enter minuter:"))
        second=int(input("Enter second:"))
        t=Time(hour,minute,second)
        t.chek()
        t.show()

        print("result=")
        res=t.time_to_sec()
        res.show()

    elif c==4:
        second=int(input("Enter second:"))
        t=Time(s=second)
        t.chek()
        t.show()

    elif c==5:
        break

