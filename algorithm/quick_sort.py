def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data.pop(0)

    left_list = [i for i in data if i <= pivot]
    right_list = [i for i in data if i > pivot]

    left = quick_sort(left_list)
    right = quick_sort(right_list)

    return left + [pivot] + right
