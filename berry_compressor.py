def sum_for_position(i, berries, N):
    left = (i - 1 + N) % N
    right = (i + 1) % N
    return berries[left] + berries[i] + berries[right]

def find_max_sum(N, berries):
    max_sum = 0
    for i in range(N):
        current = sum_for_position(i, berries, N)
        if current > max_sum:
            max_sum = current
    return max_sum

def compress(berries):
    N = len(berries)
    return find_max_sum(N, berries)

if name == "main":
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        print("Нет входных данных")
        sys.exit(1)
    N = int(data[0])
    berries = list(map(int, data[1:1+N]))
    print(compress(berries))