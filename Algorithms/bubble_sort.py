from list_generator import list_generator

def bubble_sort(alist):
    '''bubble sort action generator'''
    for i in range(len(alist), 1, -1):
        for j in range(1, i):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                yield alist

if __name__ == "__main__":
    
    bubble_gen = bubble_sort(list_generator())
    
    for index, action in enumerate(bubble_gen):
        print(f'{index}: {action}')