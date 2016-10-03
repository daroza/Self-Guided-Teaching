def ransom_note(magazine, ransom):
    magazine_map = {}
    ransom_map = {}

    for word in magazine:
        if word in magazine_map:
            magazine_map[word] += 1
        else:
            magazine_map[word] = 1

    for word in ransom:
        if word in ransom_map:
            ransom_map[word] += 1
        else:
            ransom_map[word] = 1

    for word in ransom_map:
        if word not in magazine_map or magazine_map[word] < ransom_map[word]:
            return False

    return True

print("Should be True: {}".format(ransom_note(["give", "me", "one", "grand", "today", "night"], ["give", "me", "one", "grand", "today"])))

