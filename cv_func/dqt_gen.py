import numpy as np

def dqt_scaling(factor):
    std_dqt = np.array([
                        [ 16, 11, 10, 16, 24,  40,   51, 61 ],
                        [ 12, 12, 14, 19, 26,  58,   60, 55 ],
                        [ 14, 13, 16, 24, 40,  57,   69, 56 ],
                        [ 14, 17, 22, 29, 51,  87,   80, 62 ],
                        [ 18, 22, 37, 56, 68,  109, 103, 77 ],
                        [ 24, 35, 55, 64, 81,  104, 113, 92 ],
                        [ 49, 64, 78, 87, 103, 121, 120, 101],
                        [ 72, 92, 95, 98, 112, 100, 103, 99 ]
                       ])
    scaling_dqt = std_dqt * factor
    scaling_dqt = np.around(scaling_dqt)
    return scaling_dqt

def flat(matrix):
    flat_matrix = matrix.flatten()
    return flat_matrix

def zigzag(matrix):
    i=0
    j=0
    zigzag_matrix= []
    for x in range(matrix.size):
        zigzag_matrix.append(matrix[i][j])
        if (i == 0 or i == matrix.shape[0]-1) and j%2==0:
            j = j + 1
        elif (j==0 or j==matrix.shape[1]-1) and i%2==1:
            i = i + 1
        elif (i+j)%2 == 1 :
            i = i + 1
            j = j - 1
        elif (i+j)%2 == 0 :
            i = i - 1
            j = j + 1

    return zigzag_matrix

if __name__ == '__main__':
    scaling_dqt = dqt_scaling(1)
    print(scaling_dqt)
    flat_dqt = flat(scaling_dqt)
    print(10*'*'+'flat dqt'+10*'*')
    print(flat_dqt)
    zigzag_dqt = zigzag(scaling_dqt)
    print(10*'*'+'zigzag dqt'+10*'*')
    print(zigzag_dqt)