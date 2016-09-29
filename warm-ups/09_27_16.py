# Description:
#
# You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
#
# Example:
#
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
#
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strarr, k):
    longest = ""
    if k > len(strarr) or k <= 0 or len(strarr) == 0:
        return longest
    idx_a = 0
    idx_b = k

    while idx_b < len(strarr)+1:
        current_slice = "".join(strarr[idx_a : idx_b])
        if len(longest) < len(current_slice):
            longest = current_slice
        idx_a += 1
        idx_b += 1

    return longest

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
