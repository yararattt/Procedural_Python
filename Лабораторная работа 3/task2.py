def find_common_participants(str1, str2, splitter=","):
    str1 = str1.split(splitter)
    str2 = str2.split(splitter)
    common = list(set(str1).intersection(str2))
    return common.sort()


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, '|'))
