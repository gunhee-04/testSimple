def say_nick(nick):
    if nick == "바보":
        return
    
    print("나의 별명은 %s 입니다" % nick)

say_nick('바보')
say_nick('천재')

def say_myself(name,age,man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself('홍길동', 34)
say_myself('홍길동', 34 , False)