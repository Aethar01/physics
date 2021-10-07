def timesTables():
    #let's write a simple program that plots a times table

    #initialize the first number
    a = 1

    #loop over the first number
    while (a < 10):
        #initialize the second number
        b = 1
        #loop over the second number (so long as it's not bigger than the first)
        while (b <= a):
            #work out the answer
            c = a * b
            #format the printing according to whether the answer has two digits or one
            if (c >= 10):
                print(a, 'x', b, ' = ', c)
            else:
                print(a, 'x', b, ' =  ', c)

            #increment the second number
            b = b + 1
        #increment the first number
        a = a + 1

def quadFormula(a,b,c):
    x1 = (-b + (b**2.0 - 4.0 * a * c)**0.5) / (2.0 * a)
    x2 = (-b - (b**2.0 - 4.0 * a * c)**0.5) / (2.0 * a)
    return(x1, x2)

print(quadFormula(a = float(input("a = ")), b = float(input("b = ")), c = float(input("c = "))))