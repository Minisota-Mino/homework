def single_root_words(root_word, *other_words):
    same_words = []
    new_root_word = root_word.lower()
    for j in other_words:
        new_other_words = j.lower()
        if new_root_word in new_other_words or new_other_words in new_root_word:
            same_words.append(j)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
    