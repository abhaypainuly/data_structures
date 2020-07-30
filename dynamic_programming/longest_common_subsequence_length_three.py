def longest_common_subsequence_length_three(lst1,lst2,lst3):
    def longest_common_Helper(low1,low2,low3,lst1,lst2,lst3,dt):
        if (low1,low2,low3) not in dt:
            if low1 == len(lst1):
                dt[(low1,low2,low3)] = 0
            elif low2 == len(lst2):
                dt[(low1,low2,low3)] = 0
            elif low3 == len(lst3):
                dt[(low1,low2,low3)] = 0
            else:
                if lst1[low1] == lst2[low2] == lst3[low3]:
                    dt[(low1,low2,low3)] = longest_common_Helper(low1+1,low2+1,low3+1,lst1,lst2,lst3,dt)+1
                else:
                    dt[(low1,low2,low3)] = max(longest_common_Helper(low1,low2+1,low3,lst1,lst2,lst3,dt),longest_common_Helper(low1+1,low2,low3,lst1,lst2,lst3,dt),longest_common_Helper(low1,low2,low3+1,lst1,lst2,lst3,dt))
        return dt[(low1,low2,low3)]    
    dt = {(len(lst1),len(lst2),len(lst3)):0}
    return longest_common_Helper(0,0,0,lst1,lst2,lst3,dt)


#BOTTOM UP APPROACH
n1 = 5
lst1 = [8,3,2,1,7]
n2 = 7
lst2 = [8,2,1,3,8,10,7]
n3 = 6
lst3 = [6,8,3,1,4,7]

arr = [[[0 for i in range(n3+1)] for j in range(n2+1)] for k in range(n1+1)] 
for i in range(n1+1):
    for j in range(n2+1):
        for k in range(n3+1):
            if (i==0 or j==0 or k==0):
                arr[i][j][k] = 0
            elif (lst1[i-1] == lst2[j-1] and lst1[i-1]==lst3[k-1]):
                arr[i][j][k] = arr[i-1][j-1][k-1]+1
            else:
                arr[i][j][k] = max(arr[i-1][j][k],arr[i][j-1][k],arr[i][j][k-1])
print(arr[][][])