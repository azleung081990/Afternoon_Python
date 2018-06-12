with open("read_write.txt",'w+',encoding = 'utf-8') as f:
    for number in range(1, 10):
        f.write("{0}\n".format(number))

    letters = ['a', 'b', 'c', 'd', 'e']
    for letter in letters:
            f.write("{0}\n".format(letter))
            f.seek(0)

with open("output.txt",'w+', encoding= 'utf-8') as g:
    for number in range(1, 10):
        g.write("{0}\n".format(number))

    letters = ['a', 'b', 'c', 'd', 'e']
    for letter in letters:
            g.write("{0}\n".format(letter))
            g.seek(0)
    for line in g:
        g.print("Line: {0}".format(line)
        