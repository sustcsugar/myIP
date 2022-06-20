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

def dqt_flat(dqt):
    flat_dqt = dqt.flatten()
    return flat_dqt

def dqt_zigzag(dqt):
    
    return

if __name__ == '__main__':
    scaling_dqt = dqt_scaling(0.1)
    print(scaling_dqt)
    flat_dqt = dqt_flat(scaling_dqt)
    print(flat_dqt)