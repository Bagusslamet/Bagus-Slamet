def bfs (graph, source):
    visited =set() # to keep track of already visited nodes
    bfs_traversal = list()  # the BFS traversal result
    queue = list()#queue

    # pudh the root node to the queue and mark it as visited
    queue.append(source)
    visited.add(source)

    # loop until the queue is empty
    while queue:
        # pop the front node of the queue and add it to bfs_traversal
        current_node = queue.pop(0)
        bfs_traversal.append(current_node)

        # check all the neighbour_node in 
        for neighbour_node in graph[current_node]:
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)
    return bfs_traversal

def main():
    graph = {
        'A' : ['B', 'C'],
        'B' : ['A', 'D', 'E'],
        'C' :['A', 'F', 'G'],
        'D' :['B'],
        'E' :['B'],
        'F' :['C'],
        'G' :['C'],

    }
    bfs_traversal = bfs(graph, 'A')
    print(f"BFS: {bfs_traversal}")
    
main()