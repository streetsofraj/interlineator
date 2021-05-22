


lines_list1 = open('raven.txt').read().split('\n')
lines_list2 = open('corvo.txt').read().split('\n')



#print(range(len(list(zipped))))

for x in range(len(list(zip(lines_list1,lines_list2)))):

    print(list(zip(lines_list1,lines_list2))[x][0])
    print(list(zip(lines_list1,lines_list2))[x][1])

    print('\n')
    print('\n')


"""
print(lines_list1)
print(lines_list2)
"""