import operator
class priorityqueue:
    def __init__(self):
        self.data=[]
    def enqueue(self,key,value):
        self.data.append((key,value))
    def find_min(self):
        minkv=min(self.data, key=operator.itemgetter(0))[1]
        return minkv
    def dequeue(self):
        minv=float('inf')
        for i in range(len(self.data)):
            if(self.data[i][0]<minv):
                minv=self.data[i][0]
                mink=i
                minci=self.data[i][1]
        del(self.data[mink])
        return minci
    def __len__(self):
        return len(self.data)
