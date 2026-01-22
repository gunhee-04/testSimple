name="나의 이름은 홍길동입니다. habby"
print(len(name))
print(name.count('b'))
a="Python is not best choice"
pos = a.find('b')
if pos == -1:
    print('값이 없다')
else: 
    print( pos , '번째 자리에 있다')
