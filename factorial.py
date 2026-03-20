#finding factorials in py
#4! = 1*2*3*4

#without using fun

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i
    print(fact)
#using fun
    def calc_fact(n):
        fact = 1

        for i in range(1, n+1):

            fact *= i
            print(fact)

calc_fact(6)
calc_fact(7)            #using function we can do multiple task