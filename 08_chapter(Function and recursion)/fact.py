def fact(n):
    product = 1
    for i in range (n):
     product = product * (1+i)
    return(product)
n1 = int(input("enter the number you want the factorial of: "))
fact1 = fact(n1)
print(fact1)