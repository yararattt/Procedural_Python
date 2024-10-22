numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index = 4
sum_before = sum(numbers[:index])
sum_after = sum(numbers[index + 1:])
cnt = len(numbers)
sum = sum_before + sum_after
average = round(sum / cnt, 2)
numbers[index] = average
print("Измененный список:", numbers)
