import math

def list_intersection(lst1: list, lst2: list) -> list:
    return list(set(lst1) & set(lst2))

# Breaks an array into sections with as even
# sizes as possible. It will favor placing
# larger lists earlier in results and smaller
# lists at the end.
def list_partition(lst: list, num_partitions: int) -> list:
    chunk_size = len(lst)/num_partitions
    if chunk_size.is_integer():
        chunk_size = math.floor(chunk_size) # convert to int
    else:
        fractional_digits = chunk_size - math.floor(chunk_size)
        if fractional_digits >= .5:
            chunk_size = math.ceil(chunk_size)
        else:
            chunk_size = math.floor(chunk_size)

    index = 0
    break_point = (num_partitions - 1) * chunk_size
    while index < break_point:
        yield lst[index:(index + chunk_size)]
        index += chunk_size
    yield lst[index:len(lst)]
