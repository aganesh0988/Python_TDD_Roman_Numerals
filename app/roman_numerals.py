def parse(rn):
    count = 0
    for i in rn:
        if i == "I":
            count += 1
        elif i == "V" and count % 5 == 0:
            count += 5
        elif i == "V" and count % 5 == 1:
            count += 3
        elif i == "X" and count % 10 == 1:
            count += 8
        elif i == "X" and count % 10 == 0:
            count += 10
        elif i == "L" and count % 50 == 0:
            count += 50
        elif i == "L" and count % 50 == 10:
            count += 30
        elif i == "C" and count % 100 == 0:
            count += 100
        elif i == "C" and count % 100 == 10:
            count += 80
        elif i == "D" and count % 500 == 0:
            count += 500
        elif i == "D" and count % 500 == 100:
            count += 300
        elif i == "M" and count % 1000 == 0:
            count += 1000
        elif i == "M" and count % 1000 == 100:
            count += 800
    return count
