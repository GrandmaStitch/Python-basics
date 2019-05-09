import urllib.request

connection = urllib.request.urlopen('https://www.baidu.com/')
output = connection.read()
print(output)
connection.close()

aset = {80, 62, 63, 62, 73, 94, 56}
print(aset)

alist = [80, 62, 63, 62, 73, 94, 56]
def greater_than(list):
    m = len(list)
    n = 0
    num = list[n]
    while n < m:
        if num > list[n+1]:
            num = list[n+1]
        n += 1

def selectionSort(nb):
    print(nb)
    for i in range(len(nb)):
        for j in range(i, len(nb)):
            if nb[i] > nb[j]:
                nb[j], nb[i] = nb[i], nb[j]
                print(nb)
    return nb

print(selectionSort(alist))





