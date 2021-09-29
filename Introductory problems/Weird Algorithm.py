def main():
    n = int(input())
    output = []
    while n != 1:
        if n % 2 == 0:
            n = n/2
            output.append(n)
        else:
            n = (n*3)+1
            output.append(n)
    print(output)
if __name__ == "__main__":
    main()