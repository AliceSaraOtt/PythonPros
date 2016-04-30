x = 0

def gui(x):
    x += 1
    if x < 100:
        return gui(x)
    else:
        return x

print gui(x)