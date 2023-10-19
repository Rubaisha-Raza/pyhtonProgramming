#  WRITE A PROGRAM TO DETECT A SPAM COMMENT
text =input("ENTER COMMENT HERE \n")

if ("make a lot of money" in text or "buy now" in text or "subscribe this" in text or "click this" in text):
    spam = True 
    
else:
    spam = False
if (spam):
    print("THIS IS A SPAM TEXT")
else:
    print("THIS IS NOT A SPAM COMMENT")
