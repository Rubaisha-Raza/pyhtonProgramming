#   WRITE A PROGRAM TO GREET ALL THE PERSONS NAMES STORED IN THE LIST L1 AND WHICH START WITH S
l1 = ["harry","sachin","sohail","raghav"]
for name in l1:
    if name.startswith("s"):
        print("hello "+name)