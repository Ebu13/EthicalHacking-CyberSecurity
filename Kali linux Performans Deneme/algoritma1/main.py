import time


def lrt():
    result = 0
    for i in range(1, (10 ** 8)+1):
        if i % 2 == 0:
            result += i
        else:
            result -= i
    print(result)


def ortolcum(tekrar):
    surec = 0
    for i in range(tekrar):
        start = time.time()
        lrt()
        end = time.time()
        surec += (end - start)
    return surec / tekrar


print("lrt() fonksiyonunun ortalama calisma suresi ", ortolcum(50))
