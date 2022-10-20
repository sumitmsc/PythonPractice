mix=[12.0,"ram",[1,2,3],(4,5,6),2j+1]

a=mix[-2]
print("This is the output of a=mix[-2]==> ",a)
print(mix)

mix.append([23,44,55])
print(mix)

count=mix.count(False)
print(count)

mix.remove("ram")

print(mix)
c=mix.pop(0)
print(c)
print(mix)