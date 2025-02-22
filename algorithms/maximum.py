def maximum(elements: list | tuple) -> int | float:
    if not elements:
        return None
    max = elements[0]
    for i in range(1, len(elements)):
        if elements[i] > max:
            max = elements[i]
    return max
