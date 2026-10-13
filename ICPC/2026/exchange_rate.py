import sys 

def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return 

    t, c, k = input_data[0].split()
    print(min(int(c), int(t)*int(k)))
    
    return


if __name__ == "__main__":
    main()

    