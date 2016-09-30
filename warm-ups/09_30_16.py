# Arrays: Left Rotation
# A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].
#
# Given an array of n integers and a number, d, perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.
#
# Input Format
#
# The first line contains two space-separated integers denoting the respective values of n (the number of integers) and d (the number of left rotations you must perform). 
# The second line contains n space-separated integers describing the respective elements of the array's initial state.
#
# Constraints
#
# 1 <= n <= 10^5
# 1 <= d <= n
# 1 <= ai <= 10
#
# Output Format
#
# Print a single line of n space-separated integers denoting the final state of the array after performing d left rotations.
#
# Sample Input
#
# 5 4
# 1 2 3 4 5
# Sample Output
#
# 5 1 2 3 4
# Explanation
#
# When we perform d=4 left rotations, the array undergoes the following sequence of changes:
#
#     [1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2] -> [4,5,1,2,3] -> [5,1,2,3,4]
#
# Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4

def rot_left(input_str):
    constraint_a, num_list = input_str.split("\n")
    num_of_ints, rot_count = constraint_a.split(" ")
    num_list = num_list.split(" ")

    for i in range(0, int(rot_count)):
        popped_val = num_list.pop(0)
        num_list.append(popped_val)

    num_list = " ".join(num_list)
    return num_list

sample = "5 4\n1 2 3 4 5"

print("Expected: 5 1 2 3 4, Actual: {output}".format(output=rot_left(sample)))
