 #RECURSION IS A FUNTION WHICH CALLS ITSELF:

def fact_recursive(n):
    if n ==1 or n==0:
     return 1
    return n * fact_recursive(n-1)

n1 = int(input("enter any number: "))
fact1 = fact_recursive(n1)
print(fact1)
