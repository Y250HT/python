def merge_sort(li):
    n = len(li)
    if n == 1:
        return li
    # 把数据分成左右两部分
    mid = n // 2
    left = li[:mid]
    right = li[mid:]

    # 递归拆分
    left_res = merge_sort(left)
    right_res = merge_sort(right)
    # 把下层返回上来的数据，组成有序序列
    result = merge(left_res, right_res)
    # 合并
    return result


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # while循环结束后，把剩下的数据添加进来
    result += right[right_index:]
    result += left[left_index:]
    return result


if __name__ == '__main__':
    list_demo = [6, 5, 7, 4, 3, 1]
    print(merge_sort(list_demo))




