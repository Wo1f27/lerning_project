def longestCommonPrefix(strs) -> str:
    result = ''
    sort_strs = sorted(strs)
    first_word = sort_strs[0]
    last_word = sort_strs[-1]
    for i in range(min(len(first_word), len(last_word))):
        if first_word[i] != last_word[i]:
            return result
        else:
            result += first_word[i]
    return result

print(longestCommonPrefix(['aaa', 'aa', 'aaa']))