def Shortest_Path(G,start,end,travelled,weights):
    D={}
    for vertex in G.keys():
        D[vertex]=999999999
    D[start]=0
    qu=[]
    qu.append(start)
    while len(qu)!=0:
        current=qu.pop(0)
        for vertex in G[current]:
            if(D[current]+weights[(current,vertex)]<D[vertex]):
                D[vertex]=D[current]+weights[(current,vertex)]
            if vertex not in travelled:
                travelled.append(vertex)
                qu.append(vertex)
    #return D[end]
    return D
