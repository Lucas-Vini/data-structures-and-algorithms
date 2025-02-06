def merge_sort(elements: list, start=0, end=None, reverse=False):
    if end is None:
        end = len(elements)

    if (end - start) > 1:
        middle = (start + end) // 2
        merge_sort(elements, start, middle, reverse)
        merge_sort(elements, middle, end, reverse)
        merge(elements, start, middle, end, reverse)


def merge(elements, start: int, middle: int, end: int, reverse: bool):
    first_half = elements[start:middle]
    second_half = elements[middle:end]
    
    i, j = 0, 0
    for k in range(start, end):
        if i == len(first_half):
            elements[k] = second_half[j]
            j += 1
        
        elif j == len(second_half):
            elements[k] = first_half[i]
            i += 1

        elif ((second_half[j] < first_half[i]) and not reverse) or ((second_half[j] > first_half[i]) and reverse):
            elements[k] = second_half[j]
            j += 1

        else:
            elements[k] = first_half[i]
            i += 1


