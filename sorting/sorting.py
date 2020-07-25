def selection_sort(items):
    '''Sorts the elements of a given list in ascending order'''
    length = len(items)
    for i in range(length-1):
        least = i        
        for j in range(i+1, length):
            if items[least] > items[j]:
                least = j
        if i != least:
            items[least], items[i] = items[i], items[least]

def merge_sort(items, start=0, stop=None):
    '''Sorts the elements of a given list in ascending order'''
    if stop is None:
        stop = len(items)    
    if (stop - start) > 1:
        middle = start + ((stop-start)//2)
        a = merge_sort(items, start, middle)
        b = merge_sort(items, middle, stop)
        return merge(a,b)
    else:
        return items[start:stop]

def merge(items1, items2):
    '''Assist the merge_sort() funtion'''
    items = []
    while items1 and items2:
        if items1[0] <= items2[0]:
            items.append(items1.pop(0))
        else:
            items.append(items2.pop(0))
    if len(items1) == 0:
        while items2:
            items.append(items2.pop(0))
    else:
        while items1:
            items.append(items1.pop(0))        
    return items

def quick_sort(items, start=0, stop=None):
    '''Sorts the elements of a given list in ascending order'''
    if stop is None:
        stop = len(items) - 1
    if (stop - start) > 0:
        pivot_index = partition(items, start, stop)
        quick_sort(items, start, pivot_index-1)
        quick_sort(items, pivot_index+1, stop)

def partition(items, start, stop):
    '''Assist the quick_sort() funtion'''
    pivot = items[stop]
    pivot_index = start
    for i in range(start,stop):
        if items[i] < pivot:
            items[i], items[pivot_index] = items[pivot_index], items[i]
            pivot_index += 1

    items[pivot_index], items[stop] = items[stop], items[pivot_index]
    return pivot_index

def bubble_sort(items):
    '''Sorts the elements of a given list in ascending order'''
    length = len(items)
    control = 0
    while control < length - 1:
        control = 0
        for i in range(length-1):
            if items[i] > items [i+1]:
                items[i], items[i+1] = items[i+1], items[i]
            else:
                control += 1

def insertion_sort(items):
    '''Sorts the elements of a given list in ascending order'''
    length =  len(items)
    for i in range(1,length):
        insert_item = items[i]
        j = i - 1
        while j >= 0 and items[j] > insert_item:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = insert_item
