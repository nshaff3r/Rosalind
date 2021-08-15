from collections import defaultdict


# Iterates recursively through the adjacency list,
# finding the separate branches that don't connect.
def is_branch(node):
    # If we've already iterated over that node
    if node in processed:
        return True
    # Add that node to a list so we don't iterate over it again
    processed.append(node)
    # Go through that node's connecting nodes
    for i in range(len(dataset[node])):
        is_branch(dataset[node][i])


with open("C:/input.txt", 'r') as file:
    data = file.readlines()

dataset = defaultdict(list)

# Each node is in a dictionary whose values are a list of the nodes it connects to
for i in range(1, len(data), 1):
    val = data[i].rstrip().split(' ')
    dataset[val[0]].append(val[1])
    dataset[val[1]].append(val[0])

# So that we don't iterate twice over a node
processed = []
# Stores the number of branches we find
branches = 0

for val in dataset:
    if is_branch(val) is None:  # None is returned when a branch is found
        branches += 1

# The edges needed are the amount of nodes minus the amount of edges
# (to incorporate "singleton" nodes) plus the amount of branches,
# minus 1, since 3 branches only requires 2 edges
print(int(data[0]) - len(dataset) + branches - 1)

