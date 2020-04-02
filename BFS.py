import networkx as nx
import matplotlib.pyplot as plt
import queue
import time

def gen_bfs_graph():

    plt.ion()
    plt.figure(figsize=(5,5))

    node_size = 1000
    G = nx.erdos_renyi_graph(10, 0.15, directed=True)
    pos = nx.circular_layout(G)
    # Note: many other types of layouts are supported, including
    #       kamada_kawai_layout
    
    d = [] # d[v] = num edges in shortest path from source to v
    p = [] # p[v] = predecessor in shortest path from source to v
    x = [] # x[v] = [u | u in G.nodes, d[u] = v]
    l = len(list(G)) # num nodes in G
    i = 0  # frame number
    
    def update_graph(color, nodes):
        nx.draw_networkx_nodes(G, nodelist=nodes, node_color=color, node_size=node_size, pos=pos, with_labels=True)

    def save_image():
        plt.savefig("graph"+str(i)+".png")

    for node in G:
        d.append(l)
        # max len of shortest path in G is l-1
        # d[v] = l means v isn't reachable from source
        p.append(-1)
        # -1 is used to specify that a node doesn't have a predecessor
        x.append([])
        
    # 0 is the specified starting node
    d[0] = 0     
    nx.draw(G, node_color='#d1f1ff', node_size=node_size, pos=pos, with_labels=True)
    save_image()  

    q = queue.Queue(0)
    q.put(0) # start from node 0
    while not q.empty():
        u = q.get()
        x[d[u]].append(u)
        
        for v in G[u]:
            if d[v] == l:
                d[v] = d[u] + 1
                p[v] = u
                q.put(v)

    lastnodes = []
    for nodes in x:
        if not nodes == []:
            i+=1
            update_graph('#69d1ff', nodes)
            save_image()
        lastnodes = nodes
        update_graph('#1e7da5', lastnodes)
    save_image()  

def main():
    gen_bfs_graph()
