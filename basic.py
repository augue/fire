f  = 1
def salt():
    global f
    val = int(input("ENter number"))
    if val < 0:
        print("error")
    elif val == 0:
        print(f)
    else:
        for n in range(1,val+1):
            f = f * n
        print(f)
salt()