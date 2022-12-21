# List Method

l = [1, 2, 3, 4, 5, 9, 7, 8, 15, 16, 78]
l.append(6)
print(l)
l.sort()  # It will print the list in accending order
print(l)
l.sort(reverse=True)  # It will print the list in decending order
print(l)
l.reverse()  # It will reverse the list
print(l)
print(l.index(78))  # It will give us the index of the value of List
print(l.count(1))
l.insert(2, 899999)
print(l)

m = [900, 800, 1100]
l.extend(m)
print(l)
