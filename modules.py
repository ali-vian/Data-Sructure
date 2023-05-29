   
def stack():
    s=[]
    return (s)
def push(s,data):
    s.append(data)
def pop(s):
    data = s.pop()
    return (data)
def peek(s):
    return (s[len(s)-1])
def isEmpty(s):
    return (s == [])
def size(s):
    return (len(s))

def createQueue():
    q=[]
    return q
def enqueue(q,data):
    q.insert(0,data)
    return(q)
def dequeue(q):
    data=q.pop()
    return(data)
def isEmpty(q):
    return (q==[])
def size(q):
    return (len(q))


def createDeque():
    d=[]
    return d
def addFront(d,data):
    d.insert(0,data)
    return d
def addRear(d,data):
    d.append(data)
    return d
def removeRear(d):
    data=d.pop()
    return data
def removeFront(d):
    data=d.pop(0)
    return data
def isEmpty(d):
    return d == []
def size(d):
    return len(d)