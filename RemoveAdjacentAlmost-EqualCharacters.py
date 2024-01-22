def remove_alomst_adjecent_chars(word):
    word_arr = list(word)
    res = 0

    for i in range(1, len(word_arr)):
        if abs(ord(word_arr[i]) - ord(word_arr[i- 1])) < 2:
            res += 1
            word_arr[i] = "?"
    return res

    


print(remove_alomst_adjecent_chars("zyxyxyz"))