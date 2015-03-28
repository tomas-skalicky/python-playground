import sys


def compute_wanted_tuple_count(permutation):
    
    tuple_count = 0
    a_count = 0
    b_count = 0
    
    for char in permutation:
        if char == 'A':
            a_count += 1
        elif char == 'B':
            tuple_count += a_count
            b_count += 1
        elif char == 'C':
            tuple_count += a_count + b_count
    
    return tuple_count


# If a valid permutation exists, returns an array with any (e.g. ['A', 'B', 'B'] for arguments permutation_length=3 and target_tuple_count=2)
# Otherwise, returns an empty array.
def get_permutation(permutation_length, target_tuple_count):
    
    first_index = 0
    last_index = permutation_length - 1
    
    permutation = ['A'] * permutation_length
    
    change_count_in_last_iteration = 0
    
    previous_tuple_count = compute_wanted_tuple_count(permutation)
    previous_index = last_index
    previous_permutation_item_value = permutation[previous_index]
    
    current_index = last_index
    current_tuple_count = compute_wanted_tuple_count(permutation)
    
    iteration_counter = 0
    recalculation_counter = 0
    
    while True:
        iteration_counter += 1
#         print('target_tuple_count               ' + str(target_tuple_count))
#         print('previous_tuple_count             ' + str(previous_tuple_count))
#         print('current_tuple_count              ' + str(current_tuple_count))
#         print('previous_index                   ' + str(previous_index))
#         print('current_index                    ' + str(current_index))
#         print('previous_permutation_item_value  ' + str(previous_permutation_item_value))
#         print('permutation                      ' + ''.join(permutation))
#         print('change_count_in_last_iteration   ' + str(change_count_in_last_iteration))
        
        if (current_tuple_count == target_tuple_count):
#             print('iteration_counter         ' + str(iteration_counter))
#             print('recalculation_counter     ' + str(recalculation_counter))
            return permutation
        
        if current_index < first_index:
            if change_count_in_last_iteration == 0:
#                 print('iteration_counter         ' + str(iteration_counter))
#                 print('recalculation_counter     ' + str(recalculation_counter))
                return []
            else:
                change_count_in_last_iteration = 0
                current_index = last_index
         
        else:
            if current_tuple_count < previous_tuple_count or current_tuple_count > target_tuple_count:
                change_count_in_last_iteration -= 1
                permutation[previous_index] = previous_permutation_item_value
                current_tuple_count = previous_tuple_count
        
            elif (current_tuple_count < target_tuple_count):
                
                if permutation[current_index] == 'A' or permutation[current_index] == 'B':
                    previous_permutation_item_value = permutation[current_index]
                    previous_tuple_count = current_tuple_count
                    change_count_in_last_iteration += 1
                
                    if permutation[current_index] == 'A':
                        permutation[current_index] = 'B'
                    elif permutation[current_index] == 'B':
                        permutation[current_index] = 'C'
                
                    recalculation_counter += 1
                    current_tuple_count = compute_wanted_tuple_count(permutation)
#                     print('permutation                ' + ''.join(permutation))
                    
                previous_index = current_index
                current_index -= 1
            
                
def is_greater(a, b):
    return ord(a) < ord(b)


def construct_wanted_tuples(permutation):
    
    tuples = []
    
    for j in range(1, len(permutation)):
        for i in range(0, j):
            if is_greater(permutation[i], permutation[j]):
                tuples.append((str(i), str(j)))
            
    return tuples


permutation = get_permutation(permutation_length=int(sys.argv[1]), target_tuple_count=int(sys.argv[2]))
print('"{}"'.format(''.join(permutation)))
if len(permutation) > 0:
    print('[{}]'.format(', '.join(['({})'.format(','.join(my_tuple)) for my_tuple in construct_wanted_tuples(permutation)])))
