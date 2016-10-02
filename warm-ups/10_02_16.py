# Prompt same as 10_01_16.js

def number_needed(a, b):
    map_a = {}
    map_b = {}
    delete_count = 0

    for letter in a:
        if letter in map_a:
            map_a[letter] += 1
        else:
            map_a[letter] = 1

    for letter in b:
        if letter in map_b:
            map_b[letter] += 1
    else:
        map_b[letter] = 1

    for key_a in map_a:
        if key_a in map_b:
            delete_count += abs(map_a[key_a] - map_b[key_a])
        else:
            delete_count += map_a[key_a]

    for key_b in map_b:
        if key_b not in map_a:
            delete_count += map_b[key_b]

    return delete_count

print("{} should equal 4".format(number_needed("abc", "cde")))
