def selection_sort(elements: list, reverse=False) -> list:
    for i in range(len(elements)):
        reference = i
        
        for j in range(i+1, len(elements)):
            if (elements[j] < elements[reference]) and reverse == False:
                reference = j
            
            if (elements[j] > elements[reference]) and reverse == True:
                reference = j
        
        if (elements[reference] < elements[i]) and reverse == False:
            elements[reference], elements[i] = elements[i], elements[reference]

        if (elements[reference] > elements[i]) and reverse == True:
            elements[reference], elements[i] = elements[i], elements[reference]
        
    return elements