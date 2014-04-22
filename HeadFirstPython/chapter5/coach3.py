def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

try:
    with open('james.txt') as jaf:
        data = jaf.readline()
        james = data.strip().split(',')
    with open('julie.txt') as juf:
        data = juf.readline()
        julie = data.strip().split(',')
    with open('mikey.txt') as mif:
        data = mif.readline()
        mikey = data.strip().split(',')
    with open('sarah.txt') as saf:
        data = saf.readline()
        sarah = data.strip().split(',')
    clean_james = [sanitize(each_t) for each_t in james]
    clean_julie = [sanitize(each_t) for each_t in julie]
    clean_mikey = [sanitize(each_t) for each_t in mikey]
    clean_sarah = [sanitize(each_t) for each_t in sarah]
    unique_james = []
    for each_t in clean_james:
        if each_t not in unique_james:
            unique_james.append(each_t)

    unique_julie = []
    for each_t in clean_julie:
        if each_t not in unique_julie:
            unique_julie.append(each_t)

    unique_mikey = []
    for each_t in clean_mikey:
        if each_t not in unique_mikey:
            unique_mikey.append(each_t)

    unique_sarah = []
    for each_t in clean_sarah:
        if each_t not in unique_sarah:
            unique_sarah.append(each_t)

    print(sorted(unique_james))
    print(sorted(unique_julie))
    print(sorted(unique_mikey))
    print(sorted(unique_sarah))

    print(sorted(unique_james)[0:3])
    print(sorted(unique_julie)[0:3])
    print(sorted(unique_mikey)[0:3])
    print(sorted(unique_sarah)[0:3])

except IOError as err:
    print("File error: " + str(err))
