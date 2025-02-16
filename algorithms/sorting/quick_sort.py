def quick_sort(elements: list, start=0, end=None) -> list:
    if end is None:
        end = len(elements) - 1

    if start < end:
        middle = partition(elements, start, end)
        quick_sort(elements, start, middle - 1)
        quick_sort(elements, middle + 1, end)

def partition(elements, start, end):
    pivot = elements[end]
    i = start - 1
    for j in range(start, end):
        if elements[j] <= pivot:
            i += 1
            elements[i], elements[j] = elements[j], elements[i]
    elements[i+1], elements[end] = elements[end], elements[i+1]
    return i + 1
