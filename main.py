def quicksort(vec):
    N = len(vec)
    if N<=1: return vec
    indexL = -1
    pivot = vec[N-1]
    for i in range(N):
        if vec[i]> pivot:
            continue
        else:
            indexL +=1
            if vec[i]< vec[indexL]:
                temp = vec[i]
                vec[i]= vec[indexL]
                vec[indexL] = temp

    print(indexL)
    # if N == indexL +1:
    #     return vec
    vec1 = quicksort(vec[0:indexL:1])
    vec2 = quicksort(vec[indexL:N:1])
    return vec1 + vec2

arr = [1, 2, 4, 4]

print(quicksort(arr))
