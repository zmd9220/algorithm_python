
def selection_sort(data, start_idx):

    if start_idx == len(data):
        return

    # if search_idx == len(data)-1:
    #     data[min_idx], data[change_idx] = data[change_idx], data[min_idx]
    #     return
    min_val = data[start_idx]
    min_idx = start_idx
    for i in range(start_idx+1, len(data)):
        if min_val > data[i]:
            min_idx = i
            min_val = data[i]
    data[min_idx], data[start_idx] = data[start_idx], data[min_idx]
    selection_sort(data, start_idx+1)
    return




arr = [5, 7, 2, 3, 6, 9, 8]

selection_sort(arr, 0)
print(arr)