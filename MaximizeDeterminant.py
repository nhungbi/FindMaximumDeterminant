
from itertools import permutations
#for a 3x3 matrix with entries 1 to 9, want to find the maximum determinant
# matrix= [ a,b,c, d, e, f, g, h, i]
def find_determinant(matrix):
    """
    Given a 3x3 matrix in the form ( a,b,c, d, e, f, g, h, i ) containing only integers,
    return the determinant.
    """
    # det = a(ei - hf) + b(gf - di) + c(dh - eg)
    a = matrix[0]
    b = matrix[1]
    c = matrix[2]
    d = matrix[3]
    e = matrix[4]
    f = matrix[5]
    g = matrix[6]
    h = matrix[7]
    i = matrix[8]
    return a*(e*i - h*f) + b*(g*f - d*i) + c*(d*h - e*g)

all_possible_values = [i for i in range(1,10)]
def find_all_combinations(all_values):
    """
    Given a list of all values, return a list of of all permutations of the list.
    """
    return list(permutations(all_values))

def find_maximum_determinant(all_combos):
    """
    Given a list of all combinations of the matrix, return the determinant and matrix that
    will produce the maximum determinant.
    """
    current_max_determinant = -99999999999
    current_max_matrix = []
    for matrix in all_combos:
        current_det = find_determinant(matrix)
        if current_det > current_max_determinant:
            current_max_determinant = current_det
            current_max_matrix = matrix
    
    return {"determinant": current_max_determinant, "matrix": current_max_matrix}

all_combos = find_all_combinations(all_possible_values)
print(find_maximum_determinant(all_combos)) # {'determinant': 412, 'matrix': (1, 4, 8, 7, 2, 6, 5, 9, 3)}


