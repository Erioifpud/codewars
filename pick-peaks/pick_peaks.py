def pick_peaks(arr):
    #your code here
    pos, peaks = [], []
    for i, v in enumerate(arr[1:-1]):
        if v > arr[i]:
            for vv in arr[i + 2:]:
                if v > vv:
                    pos.append(i + 1)
                    peaks.append(v)
                    break
                elif v < vv:
                    break
    return {'pos': pos, 'peaks': peaks}
