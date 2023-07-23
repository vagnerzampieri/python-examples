# 1. Graph with weights on each edge
graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'end': 1
    },
    'b': {
        'a': 3,
        'end': 5
    },
    'end': {}
}

# 2. Hash table for the costs of each node
costs = {
    'a': 6,
    'b': 2,
    'end': float('inf')
}

# 3. Hash table for the parents of each node
parents = {
    'a': 'start',
    'b': 'start',
    'end': None
}

processed = []

# 4. Function to find the lowest cost node
def find_lower_cost(costs):
    # 5. Set the initial lower cost to infinity
    lower_cost = float('inf')
    # 6. Set the initial node with the lower cost to None
    node_lower_cost = None
    # 7. Loop through each node
    for node in costs:
        # 8. Get the cost of the node
        cost = costs[node]
        # print(f'cost: {cost}')
        # print(f'processed: {processed}')
        # 9. If it is lower than the current lower cost and has not been processed yet
        if cost < lower_cost and node not in processed:
            # 10. Set it as the new lower cost
            lower_cost = cost
            # print(f'lower_cost: {lower_cost}')
            # 11. Set it as the new node with the lower cost
            node_lower_cost = node
            # print(f'node_lower_cost: {node_lower_cost}')
    # 12. Return the node with the lower cost
    return node_lower_cost

# Algorithm Dijkstra
# 1. Find the node with the lowest cost that you have not processed yet
node = find_lower_cost(costs)
# 2. If you have processed all the nodes, this algorithm is done
while node is not None:
    # 3. Otherwise, update the costs for the neighbors of this node
    cost = costs[node]
    # 4. If any of the neighbors' costs were updated, update their parents too
    neighbors = graph[node]
    # 5. Repeat until you have processed every node in the graph
    for n in neighbors.keys():
        # 6. If it is cheaper to get to this neighbor by going through this node
        new_cost = cost + neighbors[n]
        # 7. Update the cost of this node
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    # 8. Mark this node as processed
    processed.append(node)
    # 9. Find the next node to process, and loop
    node = find_lower_cost(costs)

print(costs)
print(parents)

# order parents by start sequence
def order_parents(parents):
    # 1. Set the initial parent
    parent = 'end'
    # 2. Set the initial sequence
    sequence = [parent]
    # 3. Loop until you reach the start
    while parent != 'start':
        # 4. Get the next parent
        # print(f'before parent: {parent}')
        parent = parents[parent]
        # print(f'parent: {parent}')
        # 5. Add it to the sequence
        sequence.insert(0, parent)
        # print(f'sequence: {sequence}')
    # 6. Return the sequence
    return sequence

print(order_parents(parents))
# order_parents(parents)