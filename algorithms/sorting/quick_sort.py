def quick_sort(elements: list, start=0, end=None, reverse=False) -> list:
    if end is None:
        end = len(elements) - 1

    if start < end:
        pivot = partition(elements, start, end, reverse=reverse)
        quick_sort(elements, start, pivot - 1, reverse=reverse)
        quick_sort(elements, pivot + 1, end, reverse=reverse)

def partition(elements, start, end, reverse):
    pivot = elements[end]
    i = start - 1
    for j in range(start, end):
        if (elements[j] <= pivot and reverse == False) or (elements[j] >= pivot and reverse):
            i += 1
            elements[i], elements[j] = elements[j], elements[i]
    elements[i+1], elements[end] = elements[end], elements[i+1]
    return i + 1
