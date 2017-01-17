def cluster():
    trump_tweets = load_file('trump_tweets.txt')
    hillary_tweets = load_file('hillary_tweets.txt')
    
    trump_tweets1 = [t for t in trump_tweets if 'user' in t]
    hillary_tweets1 = [t for t in hillary_tweets if 'user' in t]
    
    for t in trump_tweets1:
        G.add_node(t['user']['screen_name'])
    for h in hillary_tweets1:
        G.add_node(h['user']['screen_name'])
        
    nx.draw()
    plt.savefig('graph.png')
    
    
def girvan_newman(G, most_valuable_edge=None):
    if G.number_of_edges() == 0:
        yield tuple(nx.connected_components(G))
        return
    if most_valuable_edge is None:
        def most_valuable_edge(G):
            betweenness = nx.edge_betweenness_centrality(G)
            return max(betweenness, key=betweenness.get)
    g = G.copy().to_undirected()
    g.remove_edges_from(g.selfloop_edges())
    while g.number_of_edges() > 0:
        yield _without_most_central_edges(g, most_valuable_edge)
        
        
def _without_most_central_edges(G, most_valuable_edge):
    original_num_components = nx.number_connected_components(G)
    num_new_components = original_num_components
    while num_new_components <= original_num_components:
        edge = most_valuable_edge(G)
        G.remove_edge(*edge)
        new_components = tuple(nx.connected_components(G))
        num_new_components = len(new_components)
    return new_components