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

a = [5, 9, 1, 8, 2, 7, 3, 6, 4, 10, 10, 191, 10, 0 , 0, 0, 0, 0, 0, 0, 0, 0]
print(counting_sort(a))
    