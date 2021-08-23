def climbStairs(num:int):
    f = []
    f.append(1)
    f.append(2)

    for i in range(2, num):
        f.append(f[i-1] +f[i-2])
    
    return f[num - 1]

print(climbStairs(5))
