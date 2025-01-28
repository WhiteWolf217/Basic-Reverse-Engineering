rev_content = "_hacks_{w1{1wq8]8lle<,T}"   #cat rev_this

flag = list(rev_content[:8])  # First 8 characters are unchanged

for i in range(8, 23):
    if i < len(rev_content):
        c = rev_content[i]
        if i % 2 == 0:
            flag_char = chr(ord(rev_content[i]) - 5)
        else:
            flag_char = chr(ord(rev_content[i]) + 2)
        flag.append(flag_char)

if len(rev_content) > 23:
    flag.append(rev_content[23])

flag = ''.join(flag)
print(flag)

