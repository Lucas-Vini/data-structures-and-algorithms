def insertion_sort(elements: list, reverse=False) -> list:
    for i in range(1, len(elements)):
        element_value = elements[i]
        for j in range(i):
            switch_elements = element_value < elements[i-1-j]
            if reverse:
                switch_elements = element_value > elements[i-1-j]
            
            if switch_elements:
                elements[i-1-j], elements[i-j] = element_value, elements[i-1-j]
            else:
                break
    return elements

