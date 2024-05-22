def filter_list(ls):
    res = []
    for word in ls:
        if len(word) >= 3:
            res.append(word)
    return res


print(filter_list(['Hello', '2', 'world', ':-)']))
# ['Hello', 'world', ':-)']
print(filter_list(['1234', '1567', '-2', 'computer science']))
# ['1234', '1567', 'computer science']
print(filter_list(['Russia', 'Denmark', 'Kazan']))
# ['Russia', 'Denmark', 'Kazan']
