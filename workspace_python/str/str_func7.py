a="1213a"

print(a.isdigit()) #숫자만
print(a.isalpha()) #글자만
print(a.isalnum()) # 알파벳(a-z, A-Z) 또는 숫자(0-9)로만 이루어져 있을 경우

s = "Life is too short"
print(s.startswith("Life"))
print(s.endswith("short"))