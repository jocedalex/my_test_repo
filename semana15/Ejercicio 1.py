def my_bubble(element_list):
    n = len(element_list)

    for i in range(n-1):
        changes=False
        for j in range(0, n-i-1):
            if element_list[j] > element_list[j+1]:
                element_list[j], element_list[j+1] = element_list[j+1], element_list[j]
                changes=True

        if not changes:
            break

    return element_list

def my_reverse(element_list):
    n = len(element_list)

    for i in range(n-1):
        changes=False
        for j in range(0, n-i-1):
            if element_list[j] < element_list[j+1]:
                element_list[j], element_list[j+1] = element_list[j+1], element_list[j]
                changes=True

        if not changes:
            break
        
    return element_list


print(my_bubble([64, 34, 25, 12, 22, 11, 90]))

print(my_reverse([64, 34, 25, 12, 22, 11, 90]))