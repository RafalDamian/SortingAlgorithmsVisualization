def insertion_sort(alist):
    '''insertion sort action generator'''
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                yield alist
            else:
                break

if __name__ == "__main__":

    from list_generator import list_generator
    
    insertion_gen = insertion_sort(list_generator())
    
    for index, action in enumerate(insertion_gen):
        print(f'{index}: {action}')