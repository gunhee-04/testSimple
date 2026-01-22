a=1

def vartest(b):
    global a
    a=a+b
    print(a)

b=10
vartest(b)
print(a)



# 함수로 값을 전달하는 방법
# call by value
# call by reference 