mat = []
   for i in range(locimage.size[0]):
        lol = []
        for j in range(locimage.size[1]):
            lol.append(locimage.pixels[i*locimage.size[1]+j])
        mat.append(lol)

    N = locimage.size[0]
    for x in range(0, int(N/2)):
        for y in range(x, N-x-1):
            temp = mat[x][y]
            mat[x][y] = mat[y][N-1-x]
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
            mat[N-1-y][x] = temp

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            locimage.set(i, j, mat[i][j])

    locimage.save("images/degrees90.png")
    degrees180(locimage)
    locimage.show()
