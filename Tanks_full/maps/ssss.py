with open('city.tmx') as file:
    full = file.readlines()
i=0
print(full)
for line in full:
   if i==2:
       print(i)
       print(line[1])
       print(line)
       break
   i+=1
