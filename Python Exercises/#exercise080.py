# exercise080
create_list = []
for c in range(1, 6):
    n = int(input((f'Enter {c} value: ')))
    if c == 0 or n > len[create_list-1]:
        create_list.append(n)
    else:
        pos = 0
        while pos < len(create_list):
            if n <= create_list[pos]:
                create_list.insert(pos, n)
                break
            pos += 1
print(create_list)