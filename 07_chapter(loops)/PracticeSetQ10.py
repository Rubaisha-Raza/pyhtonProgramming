#   WRITE A PROGRAM TO PRINT MULTIPLICATION TABLE OF "n" USING FOR LOOP IN REVERSED ORDER.

n = int(input("ENTER THE NUMBER: "))
for i in range(10,0,-1):
   print(str(n)+"x"+str(i)+"="+str(i*n))
   #print(f"{n}x{i}={n*i}")    USING f STRING