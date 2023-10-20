arr = [2, 1, 2, 2]
finalArray = []
intermediateArray = []
for num in arr:
    if num not in intermediateArray:
        intermediateArray.append(num)
for n in intermediateArray:
    if n in arr:
        finalArray.append([n])
contagem = 0
for i in finalArray:
    number = i[0]
    count = arr.count(number)
    finalArray[contagem].insert(number, count)  
    contagem += 1
for w in finalArray:
    print(f"{w[0]} {w[1]}")   

    

