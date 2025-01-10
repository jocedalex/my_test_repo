def my_bubble(element_list):
    n = len(element_list) #O(1)

    for i in range(n-1): #O(n-1)
        changes=False #O(1)
        for j in range(0, n-i-1): #O(n-1)*(n-i-1)
            if element_list[j] > element_list[j+1]:#O(1)
                element_list[j], element_list[j+1] = element_list[j+1], element_list[j]#O(1)
                changes=True#O(1)

        if not changes:#O(1)
            break#O(1)

    return element_list#O(1)

##############O(n-1)*(n-i-1)#############


#2.a
def print_numbers_times_2(numbers_list):
	for number in numbers_list: #O(len(numbers_list))
		print(number * 2) #O(1)
		
##############O(len(numbers_list))#############
          
#2.b
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: #O(len(list_a))
		for element_b in list_b: #O(len(list_a)*len(list_b))
			if element_a == element_b:#O(1)
				return True#O(1)
				
	return False#O(1)

##############O(len(list_a)*len(list_b))#############

#2.c
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print) #O(1)
	for index in range(min(list_len, 10)): #O(min(list_len, 10))
		print(list_to_print[index]) #O(1)

##############O(min(list_len, 10))#############
		
#2.d
def generate_list_trios(list_a, list_b, list_c):
	result_list = [] #O(1)
	for element_a in list_a: #O(len(list_a))
		for element_b in list_b: #O(len(list_b)*len(list_a))
			for element_c in list_c: #O(len(list_c)*len(list_b)*len(list_a))
				result_list.append(f'{element_a} {element_b} {element_c}') #O(1)
				
	return result_list #O(1)

##############O(len(list_c)*len(list_b)*len(list_a))#############