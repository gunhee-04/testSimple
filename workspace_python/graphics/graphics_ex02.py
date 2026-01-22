import turtle as t

t.clear()
t.home()
t.shape('turtle')
line_len = input('길이 :') #150

line_len = int(line_len)

n = 12

for i in range(n):
    t.forward(line_len)
    t.left(360/n)

t.mainloop()