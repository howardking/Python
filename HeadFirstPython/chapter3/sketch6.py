try:
    with open('missing.txt') as data:
        print("It's...", file=data)
except IOError as err:
    print('File error: ' + str(err))
