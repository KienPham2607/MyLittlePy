def print_formatted(number):
    for i in range(1, number + 1):
        print(f"{i}\t{oct(i)}\t{hex(i)}\t{bin(i)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)