dict = {
    "apple": "a fruit",
    "ball": "a toy",
    "cat": "an animal",
    "dog": "an other type of animal",
"mylist": "[1,2,3,4]"
}

print(dict.items())
print(dict.keys())
dict.update({"mylist":"[5,6]", "eye": "Part of body"})
print(dict)
#this method is use instead of [print(dict["dog"])] to avoid error if the key is invalid
print(dict.get("dog"))