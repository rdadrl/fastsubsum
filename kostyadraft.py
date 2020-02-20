inp = [2,5,6,8]
goal = 17

def exists_higher(test_list, k):
    
    for i in test_list : 
        if i > k:
            return i
    
    return 10000000000000000000

def get_lower(test_list, k):
    
    test_list.reverse()
    
    for i in test_list : 
        if i < k:
            return i
    
    return -1000000000000000000

#keep track to have the diff value smallest absolute value : either negative or equal to zero
def cancelout(curlist, diff):
    
    curlist.sort()
    
    #if the exact number exists in the list - remove it and return - rare case
    if diff in inp:
        curlist.remove(diff)
        diff = 0
        return curlist, diff
    
    #if there is an element higher value than current difference:     
    elif exists_higher(curlist, diff) - diff < diff - get_lower(curlist, diff):
        
        toremove = exists_higher(curlist, diff)
        curlist.remove( toremove )
        diff = diff - toremove
        
        return curlist, diff
    
    else:
        
        lwr = get_lower(curlist, diff)
        currlist.remove( lwr )
        diff = diff - lwr
        
        if diff > 0 and not curlist.empty():
            cancelout(currlist, diff)
        

def method1(inp, goal):
    sumlist = sum(inp)
    diffsum = sumlist - goal
    
    print( cancelout(inp, diffsum))

method1(inp, goal)   
    