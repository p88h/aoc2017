ofs = 366
pos = 0
arr = [ 0 ]
las = 2017
for step in range(1,las+1):
    pos = (pos + ofs) % step
    arr.append(0)
    for k in range(step, pos + 1, -1):
        arr[k] = arr[k-1]
    arr[pos + 1] = step
    pos += 1
print(arr[pos + 1])
rv = arr[1]
for step in range(las+1,50000000):
    pos = (pos + ofs) % step
    if pos == 0:
        rv = step
    pos += 1
print(rv)