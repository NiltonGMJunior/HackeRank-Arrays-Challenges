def hourglassSum(arr):
    best_sum = -float("inf")
    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) - 2):
            sub_matrix = []
            curr_sum = 0
            for a in range(3):
                row = []
                for b in range(3):
                    row.append(arr[i + a][j + b])
                    if (a == 1) and (b == 0 or b == 2):
                        pass
                    else:
                        curr_sum += row[-1]
                sub_matrix.append(row)
            if curr_sum > best_sum:
                best_sum = curr_sum

    return best_sum

def main():
    return

if __name__ == '__main__':
    main()
