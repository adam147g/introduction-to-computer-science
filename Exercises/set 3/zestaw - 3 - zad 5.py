def value_sequence(number):
    strnumber = str(number)
    sequenceList = list()
    scoreList = list()
    i = 0
    for element in strnumber:
        sequenceList.append(element)
    sequenceList.sort()
    sequenceList.reverse()
    while i < 10:
        scoreList.append(sequenceList[i])
        i += 1
    return scoreList, scoreList[-1]


while True:
    number = str(input("Podaj ciąg liczb zakończonych zerem (powyżej 10 znaków): "))
    if len(number) > 9:
        intNumber = int(number)
        if number[-1] == "0":
            print(value_sequence(intNumber))
            break
        else:
            continue
