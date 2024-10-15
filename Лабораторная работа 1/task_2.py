import math

disketa_byt = 1.44 * 1024 * 1024
mem_book = 4 * 25 * 50 * 100
cnt = math.floor(disketa_byt / mem_book)
print("Количество книг, помещающихся на дискету:", cnt)
