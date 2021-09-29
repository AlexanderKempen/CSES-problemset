def main():
    n = int(input())
    list = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            list.append(n)
        else:
            n = int((n*3)+1)
            list.append(n)
    for lista in list:
        print(lista, end=" ")
if __name__ == "__main__":
    main()
