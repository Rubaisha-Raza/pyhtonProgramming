#strip function remove extra spaces at the begining and end of the string 
#Example:
# this = "      Harry is good programmer       "
# print(this)
# print(this.strip())


#write a python function to remove a given word from a list and strip it at the same time>
#user define>>
def removeSplit(string, word):
    string = string.replace(word,"")
    return string.strip()
this = "    Happy new year buddy    "

n = removeSplit(this, "buddy")
print(n)
#User Input
def removeSplit(string, word):
    string = string.replace(word,"Hey")
    return string.strip()
newString = input("Write your string: ")
remove = input("")
n = removeSplit(newString,remove)
print(n)