"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]"""
def move_zeros(array):
    result = []
    for i in array:
        if i == 0 and i is not False:
            continue
        else:
            result.append(i)
    if len(result) < len(array):
        k = len(result)
        while k <len(array):
            result.append(0)
            k += 1
    return result