# Strings are immutable

a = "!Tiger !!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Tiger", "AD"))
# This replace mwthod will change all the charecters present in a string with same name will be change with given name
print(a.split(" "))

blogHeading = "this is mY new blog in term og bloging"
print(blogHeading.capitalize())
print(a.count("!"))
print(a.find("rr"))
print(a.find("r"))
print(a.index("r"))
