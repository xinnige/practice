def combine(supermatrix):
    finallist = []
    if len(supermatrix) == 0:
        return finallist
    sublen_matrix = [len(m) for m in supermatrix]
    print sublen_matrix
    exec('totalnum='+'*'.join(map(str,sublen_matrix)))
    print totalnum 
    for i in range(totalnum):
        t = i
        finallist.append([])
        for j in range(len(sublen_matrix)):
            finallist[i].append(supermatrix[j][t%sublen_matrix[j]])
            t//=sublen_matrix[j]
    return finallist


print combine([[1,2,3],[4,5],[6,7]])
