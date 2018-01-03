class roller:
    def __init__(self,message=""):
        total=0
        for elem in message:
            total+=ord(elem)
        total= total % 1000000007
        self.value=total
    def adding(self,element):
        self.value=(self.value+ord(element))%1000000007
    def deleting(self,element):
        self.value=(self.value-ord(element))%1000000007
    def get_value(self):
        return self.value


t = input()
s = input()
rs = roller(s)
rt = roller(t[0:len(s)])
if(rs.get_value()==rt.get_value()):
    print("Found")
for i in range(len(s),len(t)):
    rt.deleting(t[i-len(s)])
    rt.adding(t[i])
    if(rs.get_value()==rt.get_value()):
        if(s==t[i-len(s)+1:i+1]):
            print("found")
