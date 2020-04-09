import networkx as nx
import matplotlib.pyplot as plt
import queue, time, math, random, heapq

def gen_bfs_graph():

    # Plot Initialization
    plt.ion()                   # makes plot interactive
    plt.figure(figsize=(10,10))   # squares plot
    node_size = 500
    num_nodes = 10

    # Graph setup
    G = nx.erdos_renyi_graph(num_nodes, 2/num_nodes, directed=False)
    pos = nx.kamada_kawai_layout(G)
    # Note: many other types of layouts are supported, including
    #       kamada_kawai_layout
    
    d = []              # d[v] = num edges in shortest path from source to v
    p = []              # p[v] = predecessor in shortest path from source to v
    q = []
    l = G.number_of_nodes() # num nodes in G
    i = 0                   # frame number
    inf = 100000
    max_digits = math.ceil(math.log(1+2*num_nodes+len(list(G.edges)), 10))

    # Returns dictionary with nodes as keys and their distances as values
    def get_labels(nodes):
        labels = {}
        for v in nodes:
            if d[v] == inf:
                labels[v] = "∞"
            else:
                labels[v] = d[v]
        return labels
    
    def update_graph(nodes=[], edges=[], nodecolor='#d1f1ff', edgecolor='black'):
        labels=get_labels(nodes)
        G.update(nodes=nodes)
        nx.draw_networkx(G, nodelist=nodes, node_color=nodecolor, node_size=node_size, edgelist=edges, edge_color=edgecolor, pos=pos, with_labels=True, labels=labels)
        
    def save_image():
        nonlocal i
        plt.savefig("graph"+str(i).zfill(max_digits)+".png")
        i+=1

    # Ass ign graph edges weights
    for edge in G.edges:
        G[edge[0]][edge[1]]['weight'] = random.randint(1, num_nodes/2)

    # Initialization
    for node in G:
        d.append(inf)     # d[v] = infinity
        p.append(-1)    # p[v] = -1 means v has no predecessor
        q.append((d[node], node))
    d[0] = 0            # 0 is the specified starting node
    q[0] = (0,0)

    # Graphics

    # Initial graph drawing, all nodes undiscovered
    labels = get_labels(G.nodes)
    nx.draw(G, node_color='#d1f1ff', node_size=node_size, pos=pos, with_labels=True, labels=labels)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=nx.get_edge_attributes(G,'weight'))
    save_image()  

    # Run Dijkstra's
    while not q == []:
        u = heapq.heappop(q)[1]
        update_graph(nodes=[u], nodecolor='#69d1ff')
        save_image()
        
        for v in G[u]:
            if d[u] + G[u][v]['weight'] < d[v]:
                update_graph(edges=[(u,v)], edgecolor='#69d1ff')
                save_image()
                
                # Find index of v in q
                z = 0
                while z < len(q) and not q[z] == (d[v],v): # O(n) -> implementation needs to be fixed
                    z += 1

                d[v] = d[u] + G[u][v]['weight']
                p[v] = u
                q[z] = (d[v], v)
                heapq._siftdown(q, 0, z) # O(log n)
                
        update_graph(nodes=[u], nodecolor='#1e7da5')
        save_image()

def main():
    gen_bfs_graph()
