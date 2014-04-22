import pickle
import nester

new_man = []
new_woman = []

try:
    with open('man_data.txt', 'rb') as man_file, open('woman_data.txt', 'rb') as woman_file:
        new_man = pickle.load(man_file)
        new_woman = pickle.load(woman_file)
        nester.print_lol(new_man)
        nester.print_lol(new_woman)
        print(new_man[0])
        print(new_woman[-1])
except IOError as err:
    print("File error: " + str(err))

except pickle.PickleError as err:
    print("Pickle error: " + str(err))
