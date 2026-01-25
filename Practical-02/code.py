from collections import deque
from math import gcd

def solve_jug_puzzle(max_vol_a, max_vol_b, desired_amount):

    if desired_amount > max(max_vol_a, max_vol_b) or desired_amount % gcd(max_vol_a, max_vol_b) != 0:
        return None

    explored = set()
    bfs_queue = deque()
    bfs_queue.append((0, 0, []))

    while bfs_queue:
        vol_a, vol_b, trace = bfs_queue.popleft()

        if (vol_a, vol_b) in explored:
            continue

        explored.add((vol_a, vol_b))
        trace = trace + [(vol_a, vol_b)]

        if vol_a == desired_amount or vol_b == desired_amount:
            return trace

        next_configs = []

        next_configs.append((max_vol_a, vol_b))
        next_configs.append((vol_a, max_vol_b))

        next_configs.append((0, vol_b))
        next_configs.append((vol_a, 0))

        transfer = min(vol_a, max_vol_b - vol_b)
        next_configs.append((vol_a - transfer, vol_b + transfer))

        transfer = min(vol_b, max_vol_a - vol_a)
        next_configs.append((vol_a + transfer, vol_b - transfer))

        for cfg in next_configs:
            if cfg not in explored:
                bfs_queue.append((cfg[0], cfg[1], trace))

    return None


max_vol_a = int(input("Enter capacity of jug 1: "))
max_vol_b = int(input("Enter capacity of jug 2: "))
desired_amount = int(input("Enter target amount: "))

result_path = solve_jug_puzzle(max_vol_a, max_vol_b, desired_amount)

if result_path:
    print("\nSolution Found:")
    for step in result_path:
        print(step)
else:
    print("No solution exists")
