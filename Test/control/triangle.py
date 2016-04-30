
def triangle(row):
    for i in range(0,row):
        for j in range(1,row * 2):
            if row - i <= j <= row + i:
                print '*',
            else:
                print ' ',
        print '\n',

row = input()
triangle(row)