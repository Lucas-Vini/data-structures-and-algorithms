def bubble_sort(elements: list, reverse=False) -> list:
    for i in range(len(elements)):
        for j in range(len(elements) - i - 1):
            not_in_order = elements[j] > elements[j+1]
            
            if reverse:
                not_in_order = elements[j] < elements[j+1]

            if not_in_order:
                elements[j], elements[j+1] = elements[j+1], elements[j]

    return elements

