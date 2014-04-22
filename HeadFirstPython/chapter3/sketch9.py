import nester,pickle
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
    with open('man_data.txt', 'wb') as man_file, open('woman_data.txt', 'wb') as woman_file:
        pickle.dump(man, man_file)
        pickle.dump(woman, woman_file)
except IOError as err:
    print("File error: " + str(err))
except pickle.PickleError as err:
    print('Pickling error: ' + str(err))
