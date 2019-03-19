with open('test.tmx') as file:
    full=file.read()
print(full)
def parse(text,depth=0):
    current_line=0
    
    for line in text.split('\n'):
       
        if line.endswith('"csv">'):
            start=current_line
        if line.endswith('</data>'):
            end=current_line
            if depth==0:
                break
            else:
                depth-=1
        current_line+=1
    result=[]
    for line in text.split('\n')[start+1:end]:
        result.append(line.split(','))
    for line in result:
       if '' in line:
        line.remove('')
    return result


for line in parse(full):
    print(line)
print()
for line in parse(full,1):
    print(line)



