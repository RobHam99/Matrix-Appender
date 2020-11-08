import numpy as np

def matrix(matlist):

    n = len(matlist[0])

    Aarr = np.array(matlist)
    block = np.zeros((n ** 2, n ** 2))

    nextmatcol = 0
    nextmatrow = 0

    endpoint = n
    colendpoint = n

    for i in range((len(Aarr))):

        if i != 0 and i % n == 0:
            nextmatrow += n
            endpoint += n

        if i % n == 0:
            nextmatcol = 0
            colendpoint = n

        elif i % n != 0:
            nextmatcol += n
            colendpoint += n

        Amat = Aarr[i]

        for j, p in zip(range(nextmatrow, endpoint), range(0, n)):
            for k, q in zip(range(nextmatcol, colendpoint), range(0, n)):
                block[j, k] = Amat[p, q]

    print(block)

    return block

matlist = [np.array([[1, 0], [2, 2]]), np.array([[4, 6], [7, 5]]), np.array([[19, 22], [6, 16]]), np.array([[5, 4], [7, 7]])]

x = matrix(matlist)
