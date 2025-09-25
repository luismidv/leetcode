def isValid(s: str) -> bool:
    res_list = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping.values():
            res_list.append(char)
        else:
            if not res_list or res_list[-1] != mapping[char]:
                return False
            else:
                res_list.pop()
    return True