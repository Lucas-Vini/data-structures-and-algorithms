def counting_sort(elements: list): 
    largest_value = max(elements)
    counter_values = [0] * (largest_value + 1)

    for i in range(len(elements)):
        counter_values[elements[i]] += 1

    elements_counter = 0
    for i in range(len(counter_values)):
        while counter_values[i] > 0:
            elements[elements_counter] = i
            counter_values[i] -= 1
            elements_counter += 1
    return elements
