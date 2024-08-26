import random
def quik_sort(array):
    length=len(array)
    
    if length<=1:
        return array
    
    else:
        pivot=array.pop()

    item_lower=[]
    item_greater=[]

    for i in array:
        if i<pivot:
            item_lower.append(i)
        else:
            item_greater.append(i)
    
    return quik_sort(item_lower) + [pivot] + quik_sort(item_greater)

array=[random.randint(35,99) for x in range(1,50)]
sorted=quik_sort(array)
print(quik_sort(array))
print("Top student- ",sorted[-5:])
