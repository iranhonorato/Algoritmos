import sys


def main():
    input_data = sys.stdin.read().split()
    
    idx = 0 
    orders = int(input_data[idx])


    idx += 1
    orders_list = [0]*(orders+1)

    C = 0 
    V = 0  

    for i in range(1, orders+1):
        c = int(input_data[idx])
        v = int(input_data[idx+1])
        
        C += int(c)
        V += int(v)

        orders_list[i] = (C-V)/(C+V)
        idx +=2

    queries = int(input_data[idx])

    idx +=1

    output = []
    for _ in range(queries):
        curr = int(input_data[idx])
        idx += 1

        if orders_list[curr] > 0:
            output.append("COMPRA")
        elif orders_list[curr] < 0:
            output.append("VENDA")
        else:
            output.append("NEUTRO")

    print("\n".join(output))
    return

if __name__ == "__main__":
    main()



