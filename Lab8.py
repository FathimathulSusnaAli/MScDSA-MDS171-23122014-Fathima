def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Matrix dimensions are not feasible for multiplication.")
        return None

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

def enter_matrix():
    matrix = []

    num_rows = int(input("Enter the number of rows: "))
    num_cols = int(input("Enter the number of columns: "))

    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            element = float(input("Enter the element for row {}, column {}: ".format(i + 1, j + 1)))
            row.append(element)
        matrix.append(row)

    return matrix

A = None
B = None

while True:
    print("\nMenu:")
    print("1. Enter Matrix A")
    print("2. Enter Matrix B")
    print("3. Calculate Product")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        A = enter_matrix()
    elif choice == '2':
        B = enter_matrix()
    elif choice == '3':
        if A is not None and B is not None:
            result = matrix_multiply(A, B)
            if result is not None:
                print("Matrix multiplication completed.")
                for row in result:
                    print(row)
        else:
            print("Please enter both Matrix A and Matrix B before calculating.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")
