def bubblesort(list_of_problems):
    for indiv_lines in list_of_problems:
        temp_lst = [int(x) for x in indiv_lines.replace(',','')]
        print(temp_lst)
        #algo starts here
        length = len(temp_lst)
        for outer_counter in range(length):
            for inner_counter in range(0, length - 1 - outer_counter):
                if temp_lst[inner_counter] > temp_lst[inner_counter + 1]:
                    temp_lst[inner_counter], temp_lst[inner_counter + 1] =  temp_lst[inner_counter + 1], temp_lst[inner_counter]

        print(temp_lst)
        print()


