import random

# Graph with nodes A,B,C,D,E and their edge weights
graph = {
    ('A', 'B'): 3, ('B', 'A'): 3,
    ('A', 'C'): 6, ('C', 'A'): 6,
    ('A', 'E'): 1, ('E', 'A'): 1,
    ('B', 'C'): 2, ('C', 'B'): 2,
    ('B', 'D'): 5, ('D', 'B'): 5,
    ('B', 'E'): 4, ('E', 'B'): 4,
    ('C', 'D'): 6, ('D', 'C'): 6,
    ('C', 'E'): 5, ('E', 'C'): 5,
    ('D', 'E'): 4, ('E', 'D'): 4,
}

def path_distance(path):
    total = 0
    for i in range(len(path) - 1):
        edge = (path[i], path[i+1])
        if edge in graph:
            total += graph[edge]
        else:
            return float('inf')
    return total

def reconnect_3_pieces(path):
    n = len(path)
    splits = sorted(random.sample(range(1, n), 2))
    
    piece1 = path[:splits[0]]
    piece2 = path[splits[0]:splits[1]]
    piece3 = path[splits[1]:]
    
    print(f"Split into: {piece1} | {piece2} | {piece3}")
    
    permutations = [
        piece1 + piece2 + piece3,
        piece1 + piece3 + piece2,
        piece2 + piece1 + piece3,
        piece2 + piece3 + piece1,
        piece3 + piece1 + piece2,
        piece3 + piece2 + piece1,
    ]
    
    best_path = path
    best_dist = path_distance(path)
    
    for perm in permutations:
        dist = path_distance(perm)
        if dist < best_dist:
            best_dist = dist
            best_path = perm
            print(f"  Better: {perm} = {dist}")
    
    return best_path, best_dist

# Start with random path
current_path = ['D', 'B', 'C', 'A', 'E']
current_dist = path_distance(current_path)

print(f"Start: {current_path} = {current_dist}\n")

no_improvement = 0
iteration = 0

while no_improvement < 5:
    iteration += 1
    print(f"Iteration {iteration}:")
    
    new_path, new_dist = reconnect_3_pieces(current_path)
    
    if new_dist < current_dist:
        print(f"Improved from {current_dist} to {new_dist}\n")
        current_path = new_path
        current_dist = new_dist
        no_improvement = 0
    else:
        print("No improvement\n")
        no_improvement += 1

print(f"Final: {current_path} = {current_dist}")