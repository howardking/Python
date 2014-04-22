import nester
man = []
woman = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'man':
                man.append(line_spoken)
            elif role == 'woman':
                woman.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

try:
#    with open('man_data.txt', 'w') as man_file:
#        print(man, file=man_file)
#    with open('woman_data.txt', 'w') as woman_file:
#        print(woman, file=woman_file)
    with open('man_data.txt', 'w') as man_file, open('woman_data.txt', 'w') as woman_file:
        nester.print_lol(man, fn=man_file)
        nester.print_lol(woman, fn=woman_file)
except IOError as err:
    print('File error: ' + str(err))
