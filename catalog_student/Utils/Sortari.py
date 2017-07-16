'''
Created on Dec 19, 2016

@author: Ursu
'''
def sort(array,reverse,sortmethod):
    '''
    Functie generala pentru a sorta lista array - crescator sau descrescator - utizilizand
    algoritmul de sortare sortmethod
    reverse = {0 - crescator , 1 - descrescator}
    sortmethod - functie de sortare 
    '''
    if reverse==0:
        return sortmethod(array)
    elif reverse==1:
        return list(reversed(sortmethod(array)))

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)  
    else:  
        return array
def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(array):
    if len(array) < 2:
        return array
    middle = len(array) // 2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    return merge(left, right)
def testQuick():
    l=[1,2,3,4,5,6,0]
    assert sort(l,0,quickSort)==[0,1,2,3,4,5,6]
    assert sort(l,1,quickSort)==[6,5,4,3,2,1,0]
def testMerge():
    l=[0,3,5,4,2,1]
    assert sort(l,1,mergeSort)==[5,4,3,2,1,0]
    assert sort(l,0,mergeSort)==[0,1,2,3,4,5]
def teste():
    testQuick()
    testMerge()
teste()
