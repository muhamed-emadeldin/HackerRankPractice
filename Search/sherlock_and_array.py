def balancedSums(arr):
    #-->defense function
    assert(isinstance(arr, list)), "arr Should be a list"
    
    #-->basic variables
    total = sum(arr)
    add   = 0
    
    for elm in arr:
        if add == total - elm - add:
            return "YES"
        add += elm
        
    return "NO"