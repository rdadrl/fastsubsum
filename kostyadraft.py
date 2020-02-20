print('max slices ' , goal)
inp = [2,5,6,8]
goal = 17

def exists_higher(test_list, k):
    
    test_list.sort()
    for i in test_list : 
        if i > k:
            return i
    
    return -1

def get_lower(test_list, k):
    
    test_list.reverse()
    
    for i in test_list : 
        if i < k:
            test_list.sort()
            return i
        
    
    test_list.sort()
    return -1

#keep track to have the diff value smallest absolute value : either negative or equal to zero
def cancelout(curlist, diff, goal):
    
    curlist.sort()
    print('it! ')
    
    #if the exact number exists in the list - remove it and return - rare case
    if diff in inp:
        curlist.remove(diff)
        diff = 0
        return curlist, diff
    
    #if there is an element higher value than current difference:     
    elif abs(exists_higher(curlist, diff) - diff) < abs(get_lower(curlist, diff) - diff) and exists_higher(curlist, diff) != -1 and get_lower(curlist, diff) != -1:
        
#         print('higher than ', diff , ' is ' , exists_higher(curlist, diff))
#         print('lower than ', diff , ' is ' , get_lower(curlist, diff))
        
        print('c ', curlist)
        toremove = exists_higher(curlist, diff)
        curlist.remove( toremove )
        diff = diff - toremove
        
        return curlist, diff
    
    #edge of the list...
    elif get_lower(curlist, diff) == -1 and exists_higher(curlist, diff) != -1:
        
        print('c2 ', curlist)
        toremove = exists_higher(curlist, diff)
        print('torem ', toremove)
        curlist.remove( toremove )
        print('c22 ' , curlist)
        diff = diff - toremove
        
        return curlist, diff
    
    else:
        print('c3 ' , curlist)
        lwr = get_lower(curlist, diff)
        print('lwr ', lwr)
        curlist.remove( lwr )
        diff = diff - lwr
        
        print('lst2 ' , curlist, ' diff ', diff)
        
        
        if diff > 0 and sum(curlist) > goal:
            cancelout(curlist, diff, goal)
        

def method1(inp, goal, goal2):
    sumlist = sum(inp)
    diffsum = sumlist - goal
    
    if diffsum == 0:
        return inp
    else:
        print( cancelout(inp, diffsum, goal2))


method1(inp, goal, goal2)