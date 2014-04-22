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
    man_file = open("man_data.txt", 'w');
    woman_file = open("woman_data.txt", 'w');

    print(man, file=man_file)
    print(woman, file=woman_file)

#    man_file.close()
#    woman_file.close()
except IOError:
    print('File Error')
finally:
    man_file.close()
    woman_file.close()
