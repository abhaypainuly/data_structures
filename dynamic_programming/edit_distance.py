def edit_distance(str1,str2):    
    def edit_distance_helper(low1,low2,l1,l2,dt):
        if (low1,low2) not in dt:
            if low1 == len(l1):
                dt[(low1,low2)] = len(l2)-low2
            elif low2 == len(l2):
                dt[(low1,low2)] = len(l1)-low1
            else:
                if l1[low1] == l2[low2]:
                    dt[(low1,low2)] = edit_distance_helper(low1+1,low2+1,l1,l2,dt)
                else:
                    dt[(low1,low2)] = min(edit_distance_helper(low1+1,low2,l1,l2,dt),edit_distance_helper(low1,low2+1,l1,l2,dt),edit_distance_helper(low1+1,low2+1,l1,l2,dt))+1
        return dt[(low1,low2)]
        
    dt = {(len(str1),len(str2)):0}
    return edit_distance_helper(0,0,list(str1),list(str2),dt)


edit_distance('editing','distance')