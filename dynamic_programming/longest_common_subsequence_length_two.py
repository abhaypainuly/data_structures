def longest_common_subsequence_length(lst1,lst2):
    def longest_common_Helper(low1,low2,lst1,lst2,dt):
        if (low1,low2) not in dt:
            if low1 == len(lst1):
                dt[(low1,low2)] = 0
            elif low2 == len(lst2):
                dt[(low1,low2)] = 0
            else:
                if lst1[low1] == lst2[low2]:
                    dt[(low1,low2)] = longest_common_Helper(low1+1,low2+1,lst1,lst2,dt)+1
                else:
                    dt[(low1,low2)] = max(longest_common_Helper(low1,low2+1,lst1,lst2,dt),longest_common_Helper(low1+1,low2,lst1,lst2,dt))
        return dt[(low1,low2)]    
    dt = {(len(lst1),len(lst2)):0}
    return longest_common_Helper(0,0,lst1,lst2,dt)


#BOTTOM UP APPROACH
n1 = int(input())
lst1 = list(map(int,input().split(' ')))
n2 = int(input())
lst2 = list(map(int,input().split(' ')))

arr = [[0]*(len(lst2)+1)]*(len(lst1)+1)

i = len(lst1)-1
while i>=0:
    arr[i][len(lst2)] = 0
    i -= 1
    
i = len(lst2)-1
while i>=0:
    arr[len(lst1)][i] = 0
    i -= 1

i = len(lst1)-1
while i>=0:
    j =len(lst2)-1
    while j>=0:
        if lst1[i]==lst2[j]:
            arr[i][j] = arr[i+1][j+1]+1
        else:
            arr[i][j] = max(arr[i][j+1],arr[i+1][j])
        j -= 1
    i -= 1
print(arr[0][0])