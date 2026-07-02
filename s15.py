


matrix = [[0,0],[0,0]]

def filler():
    # fill the matrix

    for i in range(2):
        for j in range(2):
            x = int(input(f'give me a number for {i},{j}'))
            matrix[i][j] = x

    mat2 = []
    for i in range(2):
        x = input(f'give two numbers ex:1,2')
        list1 = x.split(',')
        row = []
        for n in list1:
            row.append(int(n))
        mat2.append(row)

    print(matrix)
    print(mat2)

    for i in range(2):
        for j in range(2):
            print(matrix[i][j], end=" ")

    for l1 in mat2:
        for l2 in l1:
            print(l2, end=" ")


if __name__ == "__main__":
    filler()
    print(matrix)