def parse(rn):
    count = 0
    for i in rn:
        if i == "I":
            count += 1
        elif i == "V" and count == 0:
            count += 5
        elif i == "V" and count == 1:
            count = 4
    return count
