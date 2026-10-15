#create a tuple
languages =("c++","java","php")

#add item in tuple
languages =("react",) + languages + ("java",)
print("After adding elements to tuple:",languages)

#check the item is available in tuple
if "react" in languages:
    print("react is in the tuple")
else:
    print("react is not in the tuple")

#check the length of the tuple
print("length of the tuple:",len(languages))

#access the elements of the tuple

print("first item of the tuple:",languages[0])
print("second item of the tuple:",languages[1])
print("last item of the tuple:",languages[-1])