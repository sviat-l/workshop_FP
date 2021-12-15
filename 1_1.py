def write(d1, d2):
    for key in d1:
        with open('tracker.csv', 'a') as file:
            if d1[key] == d2[key]:
                for line in file:
                    if line[0] == key:
                        line[2] = '*'
            else:
                for line in file:
                    if line[0] == key:
                        line[3] = '*'