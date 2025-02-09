def merge_sort(alist, start, end):
    if (end-start > 1):
        mid = (start+end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)


def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    i, j, k = 0, 0, start
    while (start+i < mid and mid+j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
        k += 1
    if (start+i < mid):
        while k < end:
            alist[k] = left[i]
            i += 1
            k += 1
    else:
        while k < end:
            alist[k] = right[j]
            j += 1
            k += 1


alist = input('Enter the list of numbers : ').split()
alist = [int(x) for x in alist]
merge_sort(alist, 0, len(alist))
print('Sorted list :', end='')
print(alist)
