def merge_sort(alist):

    def ms_rec(start, end):
        if end - start > 1:
            mid = (start + end) // 2

            yield from ms_rec(start, mid)
            yield from ms_rec(mid, end)
            left = alist[start:mid]
            right = alist[mid:end]
        
            left_index = 0
            right_index = 0
            main_index = start

            while left_index < len(left) and right_index < len(right):
                bufor = alist[:]
                if right[right_index] < left[left_index]:
                    alist[main_index] = right[right_index]
                    right_index += 1
                else:
                    alist[main_index] = left[left_index]
                    left_index += 1
                main_index += 1
                if bufor != alist: yield alist
            
            while left_index < len(left):
                bufor = alist[:]
                alist[main_index] = left[left_index]
                left_index += 1
                main_index += 1
                if bufor != alist: yield alist

            while right_index < len(right):
                bufor = alist[:]
                alist[main_index] = right[right_index]
                right_index += 1
                main_index += 1
                if bufor != alist: yield alist
            

    yield from ms_rec(0, len(alist))

if __name__ == "__main__":

    from list_generator import list_generator
    list = list_generator()
    print(list)
    merge_gen = merge_sort(list)

    #for index, action in enumerate(merge_gen):
     #       print(f'{index}: {action}')

    for _ in range(100):
        print(next(merge_gen))