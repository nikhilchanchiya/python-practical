#create a list of computer languages
languages = ["python","java","c++","javascript"]

print("original list:",languages)

#1. insert()
languages.insert(1,"c")
print("After insert():",languages)

#2. remove()
languages.remove("c++")
print("After remove():",languages)

#3.append()
languages.append("php")
print("After append():",languages)

#4.len()
print("length of list:",len(languages))

#5.pop()
languages.pop()
print("After pop():",languages)

#6.clear()
languages.clear()
print("After clear():",languages)

#7. delete using del
del languages[1]
print("After delete(del):",languages)