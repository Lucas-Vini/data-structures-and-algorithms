def k_th_largest_quick_selection(elements: list, k=1, start=0, end=None):
    if end is None:
        end = len(elements) - 1

    if start < end:
        pivot_index = partition(elements, start, end)
        if pivot_index == k:
            return elements[k]
        elif pivot_index > k:
            return k_th_largest_quick_selection(elements, k, start, pivot_index - 1)
        else:
            return k_th_largest_quick_selection(elements, k, pivot_index + 1, end)
    else:
        return elements[start]

def partition(elements, start, end):
    pivot = elements[end]
    i = start - 1
    for j in range(start, end):
        if elements[j] <= pivot:
            i += 1
            elements[i], elements[j] = elements[j], elements[i]
    elements[i+1], elements[end] = elements[end], elements[i+1]
    return i + 1
