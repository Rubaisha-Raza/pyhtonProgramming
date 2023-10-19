#WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS:
def func_recursive(n):
     if n == 1:
       return 1
     else:
          return (n + func_recursive(n-1) )
n1 = int(input("enter any number: "))
func1 = func_recursive(n1)
print("The sum of the first ",n1, " natural number: ",func1)
