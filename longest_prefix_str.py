def longestCommonPrefix(strs) -> str:
    general_arr = []
    if len(strs) < 2:
        return strs[0]
    first_word = strs[0]
    strs = strs[1:]
    for word in strs:
        for i in range(len(word)+1):
            if word.startswith(first_word[:i+1]):
                continue
            else:
                general_arr.append(first_word[:i])
        else:
            general_arr.append(first_word)
    min_gen_arr = min(general_arr)
    if len(min_gen_arr) > 0:
        return ''.join(min_gen_arr)
    else:
        return ''


print(longestCommonPrefix(["", "ba", "bb"]))