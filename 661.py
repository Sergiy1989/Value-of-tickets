
def ticket():
    v = {
        'A' : 0,
        'B' : 0, 
        'C' : 0
        }
    x = str(input())
    x1 = float(input())
    x2 = int(input())
    y = str(input())
    y1 = float(input())
    y2 = int(input())
    z = str(input())
    z1 = float(input())
    z2 = int(input())    
    if x == 'A':
        v['A'] = x1*x2
    if y == 'B':
        v['B'] = y1*y2
    if z == 'C':
        v['C'] = z1*z2

        print(v, (x1*x2)+(y1*y2)+(z1*z2))
ticket()
