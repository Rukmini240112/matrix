def matrix_addition(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return "Insufficient no.of inputs,enter valid no.of inputs"
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

# Multiplication of two matrices
def matrix_multiplication(a, b):
    if len(a[0]) != len(b):
        return "Insufficient no.of inputs,enter valid no.of inputs"
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(b)):
                sum += a[i][k] * b[k][j]
            row.append(sum)
        result.append(row)
    return result

# Determinant of a matrix
def matrix_determinant(a):
    if len(a) != len(a[0]):
        return "Determinant is only possible for square matrix"
    n = len(a)
    if n == 1:
        return a[0][0]
    elif n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    else:
        det = 0
        for j in range(n):
            sign = (-1) ** j
            sub_det = matrix_determinant([row[:j] + row[j+1:] for row in a[1:]])
            det += sign * a[0][j] * sub_det
        return det

# Inverse of a matrix
def matrix_inverse(a):
    if len(a) != len(a[0]):
        return "Inverse is only possible for sparse matrix"
    n = len(a)
    if n == 1:
        return [[1 / a[0][0]]]
    elif n == 2:
        det = matrix_determinant(a)
        if det == 0:
            return "Inverse is only possible for sparse matrix"
        else:
            return [[a[1][1] / det, -a[0][1] / det], [-a[1][0] / det, a[0][0] / det]]
    else:
        det = matrix_determinant(a)
        if det == 0:
            return "det be came 0"
        else:
            adjugate = []
            for i in range(n):
                row = []
                for j in range(n):
                    sign = (-1) ** (i + j)
                    sub_det = matrix_determinant([row[:j] + row[j+1:] for row in a[:i] + a[i+1:]])
                    row.append(sign * sub_det)
                adjugate.append(row)
            inverse = []
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(adjugate[j][i] / det)
                inverse.append(row)
            return inverse
def matrix_to_sparse(a):
    sparse = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != 0:
                sparse.append([i, j, a[i][j]])
    return sparse


# Example usage
n = int(input("Enter the number of rows of matrix A: "))
m = int(input("Enter the number of columns of matrix A: "))
a = []
print("Enter the elements of matrix A: ")
for i in range(n):
    row = []
    for j in range(m):
        element = float(input(f"Element ({i+1},{j+1}): "))
        row.append(element)
    a.append(row)

p = int(input("Enter the number of rows of matrix B: "))
q = int(input("Enter the number of columns of matrix B: "))
b = []
print("Enter the elements of matrix B:")
for i in range(p):
    row = []
    for j in range(q):
        element = float(input(f"Element ({i+1},{j+1}): "))
        row.append(element)
    b.append(row)

c = matrix_addition(a, b)
print("Addition of matrices A and B: \n", c)
d = matrix_multiplication(a, b)
print("Multiplication of matrices A and B: \n", d)
det_a = matrix_determinant(a)
print("Determinant of m1:",det_a)
det_b = matrix_determinant(b)
print("Determinant of m2:",det_b)
x=matrix_inverse(a)
print("inverse m1:",x)
y=matrix_inverse(b)
print("inverse m2",y)
print("matrix to sparse")
q=matrix_to_sparse(a)
print("sparse matrices A : \n", q)
w=matrix_to_sparse(b)
print("sparse matrices A : \n", w)

c1 = matrix_addition(q, w)
print("Addition of matrices A and B: \n", c1)
d1 = matrix_multiplication(q, w)
print("Multiplication of matrices A and B: \n", d1)
det_a1 = matrix_determinant(q)
print("Determinant of m1:",det_a1)
det_b1 = matrix_determinant(w)
print("Determinant of m2:",det_b1)
x1=matrix_inverse(q)
print("inverse m1:",x1)
y1=matrix_inverse(w)
print("inverse m2",y1)
