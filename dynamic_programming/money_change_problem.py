
def money_change(n,dt):
    if n not in dt:
        if n-1>0:
            mini = money_change(n-1,dt)
        if n-3>0:
            mini = min(mini,money_change(n-3,dt))
        if n-4>0:
            mini = min(mini,money_change(n-4,dt))
        dt[n] = mini+1
    return dt[n]



#BOTTOM UP APPROACH
dt = {0:0,1:1,3:1,4:1}
k = int(input('Enter Money:')) 
for n in range(2,k+1):
    if n-1>0:
        mini = dt[n-1]
    if n-3>0:
        mini = min(mini,dt[n-3])
    if n-4>0:
        mini = min(mini,dt[n-4])
    if n not in [1,3,4]:
        dt[n] = mini + 1
print(dt[k])