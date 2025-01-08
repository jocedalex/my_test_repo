def my_bubble(element_list):
    try:
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
    
    except:
        raise TypeError("The input must be a list")
