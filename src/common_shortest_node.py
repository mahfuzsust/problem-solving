from heapq import heappush, heappop

def __get_adjacency_list(edges):
    ls = {}
    for source, dest, weight in edges:
        if(source not in ls):
            ls[source] = [(dest, weight)]
        else:
            ls[source].append((dest, weight))
        
        if(dest not in ls):
            ls[dest] = [(source, weight)]
        else:
            ls[dest].append((source, weight))
    return ls

def __get_shortest_path(edges, source, dest):
    adj = __get_adjacency_list(edges)

    q = [(0, source, [], 0)]
    visited = set()
    minimums = {source : 0}

    while(q):
        (cost, node, path, own_weight) = heappop(q)
        if(node not in visited):
            visited.add(node)
            path = path[:]
            path.append((node, own_weight))

            if(node == dest):
                return path
            
            for connected_node, weight in adj.get(node):
                if(connected_node in visited):
                    continue
                
                previous_weight = minimums.get(connected_node)
                updated_weight = cost + weight

                if(previous_weight == None or updated_weight < previous_weight):
                    minimums[connected_node] = updated_weight
                    heappush(q, (updated_weight, connected_node, path, weight))
    return None

def get_common_node(edges, source, dest):
    if(edges is None or isinstance(edges, list) == False or len(edges) == 0 or \
        source is None or isinstance(source, str) == False or \
        dest is None or isinstance(dest, str) == False):
            return None

    path = __get_shortest_path(edges, source, dest)

    if(path is None or len(path) == 0):
        return None
    
    i, j = 0, len(path) - 1
    first = path[i][1]
    last = path[j][1]
    item = path[0]
    while(i < j):
        if(first < last):
            i = i + 1
            first = first + path[i][1]
            item = path[i]
        if(first > last):
            j = j - 1
            last = last + path[j][1]
            item = path[j]
        if(first == last):
            break
    return item[0]
