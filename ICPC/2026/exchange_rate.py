import sys 

def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return 

    t = int(input_data[0])
    c = int(input_data[1])
    k = int(input_data[2])

    print(min(c, t*k))
    
    return


if __name__ == "__main__":
    main()

