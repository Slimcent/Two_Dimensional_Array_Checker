def is_two_dimensional_array(arr):
    if isinstance(arr, list) and len(arr) > 0:
        if all(isinstance(row, list) for row in arr):
            # Additional check: Ensure that all rows have the same number of columns
            column_lengths = set(len(row) for row in arr)
            if len(column_lengths) == 1:
                return True
    return False


two_dim_array = [[1, 2], [3, 4], [5, 6]]
one_dim_array = [1, 2, 3]
not_array = 42


print(is_two_dimensional_array(one_dim_array))
