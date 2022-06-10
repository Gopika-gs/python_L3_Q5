f = open('readme.txt','r')
line = f.readlines()
line = [x.strip() for x in line]
print(line)