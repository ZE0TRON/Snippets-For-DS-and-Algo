from collections import defaultdict
import operator
class Partition:
    class Position:
        slots = '_container' , '_element' , '_size' , '_parent'
        def __init__(self,container,e):
            self._container = container
            self._element = e
            self._size = 1
            self._parent = self
        def element(self):
            return self._element
    def make_group(self,e):
        return self.Position(self,e)
    def find(self,p):
        if p._parent!=p:
            p._parent = self.find(p._parent)
        return p._parent
    def union(self,p,q):
        a = self.find(p)
        b = self.find(q)
        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size
class PriorityQueue:

    def __init__(self):
        self.data=[]
    def enqueue(self,key,value):
        self.data.append((key,value))
    def find_min(self):
        minkv=min(self.data, key=operator.itemgetter(0))[1]
        return minkv
    def dequeue(self):
        minv=999999999999999
        for i in range(len(self.data)):
            if(self.data[i][0]<minv):
                minv=self.data[i][0]
                mink=i
                minci=self.data[i][1]
        del(self.data[mink])
        return minv,minci
    def __len__(self):
        return len(self.data)


def arrayer():
    return []



def Kruskalk_MST(graph,weigths,N,E):
    tree=defaultdict(arrayer)
    pq=PriorityQueue()
    forest=Partition()
    positions={}
    counter=0
    for key,value in graph.items():
        positions[key]=forest.make_group(key)

    for key,value in weigths.items():
        pq.enqueue(value,key)
    print("N : ",N)
    while counter!=N-1 and len(pq)!=0:
        weight,edge=pq.dequeue()
        u,v=edge[0],edge[1]
        #if partitions[u]!=partitions[v]
        a=forest.find(positions[u])
        b=forest.find(positions[v])
        if(a!=b):
            counter+=1
            tree[u].append(v)
            tree[v].append(u)
            forest.union(a,b)
        print("Tree Length : ",len(tree.keys()))
        print("Len pq : ",len(pq))
    print("Tree : ",tree)
    return tree

graph=defaultdict(arrayer)
weigths={}
N,E=map(int,input().split())
for i in range(E):
    a,b,w=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    weigths[(a,b)]=w
MST=Kruskalk_MST(graph,weigths,N,E)
for i in range(1,N+1):
    for vertex in MST[i]:
        try:
            w=weigths[(i,vertex)]
        except:
            w=weigths[(vertex,i)]
        print(i," --- ",vertex," ----->",w)
