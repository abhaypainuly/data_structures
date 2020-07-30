#Knapsack with repetitions
def Knapsack(w,weights,dit):
    #if len(weights) == 0:
     #   return 0
    maxi = 0
    for val in weights:
        if w-val>=0:
            updated_weight = weights[:]
            updated_weight.remove(val)
            maxi = max(maxi,Knapsack(w-val,updated_weight,dit)+val)
    return maxi


#BOTTOM UP APPROACH
lst = [[0]*(w+1)]*(len(weights)+1)
for i in range(1,len(weights)):
    for j in range(1,w+1):
        if j-weights[i-1]>=0:
            lst[i][j] = max(lst[i-1][j-weights[i-1]],lst[i-1][j])
        else:
            lst[i][j] = lst[i-1][j]
print(lst[-1][-1])
print(lst)