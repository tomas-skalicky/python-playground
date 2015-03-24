import sys



def compute_permutation_count(permutation_array):
    
    permutation_count = 0
    a_count = 0
    b_count = 0
    
    for char in permutation_array:
        if char == 'A':
            a_count += 1
        elif char == 'B':
            permutation_count += a_count
            b_count += 1
        elif char == 'C':
            permutation_count += a_count + b_count
    
    return permutation_count


# If a valid permutation exists, returns an array with any (e.g. ['A', 'B', 'B'] for arguments 3 and 2)
# Otherwise, returns an empty array.
def get_permutation_array(string_length, target_permutation_count):
    
    first_index = 0
    last_index = string_length - 1
    
    permutation_array = ['A'] * string_length
    
    change_count_in_last_iteration = 0
    
    previous_permutation_count = compute_permutation_count(permutation_array)
    previous_index = last_index
    previous_permutation_item_value = permutation_array[previous_index]
    
    current_index = last_index
    
    while True:
        current_permutation_count = compute_permutation_count(permutation_array)
#         print('target_permutation_count         ' + str(target_permutation_count))
#         print('previous_permutation_count       ' + str(previous_permutation_count))
#         print('current_permutation_count        ' + str(current_permutation_count))
#         print('previous_index                   ' + str(previous_index))
#         print('current_index                    ' + str(current_index))
#         print('previous_permutation_item_value  ' + str(previous_permutation_item_value))
#         print('permutation_array                ' + ''.join(permutation_array))
#         print('change_count_in_last_iteration   ' + str(change_count_in_last_iteration))
        
        if (current_permutation_count == target_permutation_count):
            return permutation_array
        
        if current_index < first_index:
            if change_count_in_last_iteration == 0:
                return []
            else:
                change_count_in_last_iteration = 0
                current_index = last_index
         
        else:
            if current_permutation_count < previous_permutation_count or current_permutation_count > target_permutation_count:
                change_count_in_last_iteration -= 1
                permutation_array[previous_index] = previous_permutation_item_value
        
            elif (current_permutation_count < target_permutation_count):
                
                if permutation_array[current_index] == 'A' or permutation_array[current_index] == 'B':
                    previous_permutation_item_value = permutation_array[current_index]
                    previous_permutation_count = current_permutation_count
                    change_count_in_last_iteration += 1
                
                if permutation_array[current_index] == 'A':
                    permutation_array[current_index] = 'B'
                elif permutation_array[current_index] == 'B':
                    permutation_array[current_index] = 'C'
                    
                previous_index = current_index
                current_index -= 1
                
def is_greater(a, b):
    return ord(a) < ord(b)


def get_permutations(permutation_array):
    
    permutations = []
    
    for j in range(1, len(permutation_array)):
        for i in range(0, j):
            if is_greater(permutation_array[i], permutation_array[j]):
                permutations.append((str(i), str(j)))
            
    return permutations


string_length = int(sys.argv[1])
permutation_count = int(sys.argv[2])

permutation_array = get_permutation_array(string_length, permutation_count)
print('"' + ''.join(permutation_array) + '"')
if len(permutation_array) > 0:
    print('[' + ', '.join(['(' + ','.join(permutation) + ')' for permutation in get_permutations(permutation_array)]) + ']')
