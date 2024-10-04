def encontra_indices(v,s):
    indices = []
    for i,item in enumerate(s):
        if item == v:
            indices.append(i)
    return indices

l = [12,45,55,64,88,45]

x = encontra_indices(45,l)

print(x)