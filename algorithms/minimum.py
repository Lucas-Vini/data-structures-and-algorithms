def minimum(elements: list | tuple) -> int | float:
    if not elements:
        return None
    min = elements[0]
    for i in range(1, len(elements)):
        if elements[i] < min:
            min = elements[i]
    return min
 