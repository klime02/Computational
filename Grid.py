
dot = '.'
sp = ' '
wline = []
lline = []
UserInWidth = input('Enter the width:')
w = int(UserInWidth)
wc= 0
UserInLength = input('Enter the length:')
l = int(UserInLength)
lc = 0
print('The width is', w, 'and the length is', l,', and the area is', w*l)

while wc < w:
    wline.append(dot)
    wc +=1

while lc < l:
    lline.append(dot)
    lc +=1
lc = 0
class PrintWidth:
    def __init__(self,w):
        self.w = w
        wc = 0
        while wc < w:
            print(wline[wc],sp,end="")
            wc +=1
        print(sp)

while lc < l:
    PrintWidth(w)
    lc +=1
