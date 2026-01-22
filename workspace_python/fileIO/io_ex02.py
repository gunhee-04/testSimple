# 파일 생성
f = open("newfile4.txt" , 'w')
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

f = open("newfile4.txt" , 'r')

char = f.read()
print(char)    
f.close()