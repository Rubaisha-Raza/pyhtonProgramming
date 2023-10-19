myset={1,2,3,4,5,6}

#01 LENGHTH OF THE SET
print(len(myset))

#02  ADD ELEMENTS IN SET 
myset.add(7)
  # .add() do not add duplicate elements also not count it in length
myset.add(3)
myset.add('3') #add the elements of different type in a set
print(myset)

#03 REMOVE ELEMENTS FORM THE SET
myset.remove('3')
print(myset)

#04 TO REMOVE A RANDOM ELEMENT FROM THE SET
print(myset.pop())
print(myset)

#05 TO CLEAR THE SET
#myset.clear()
#print(myset)

#06 UNION OF THE SET
newset = (2,3,4,5)
print(myset.union({1,8}))


#07 INTERSECTION OF THE SET

print(myset.intersection({2,3}))
