steps = 0
def hanoi(a, b, c, n):
    global steps
    if n == 1:
        steps+=1
        print("[STEP{:>4}] {}->{}".format(steps, a, b))
    else:
        hanoi(a,b,c,n-1)
        steps+=1
        print("[STEP{:>4}] {}->{}".format(steps, a, c))
        hanoi(b,c,a,n-1)
N = eval(input())
hanoi("A", "C", "B", N)