numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_num = sum(numbers[:4] + numbers[5:])
cnt = len(numbers)
average = round(sum_num / cnt, 2)
numbers[4] = average
print("Измененный список:", numbers)
