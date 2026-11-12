# None 클래스 정의
class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=', ')
    while current.link !     = None: #is no None = ! = None
        current = current.link
        print(current.data, end=', ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node
        
# 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node() #첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]: #두 번째 이후 노트
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head) #연결리스트 출력

    insertNode("다현", "화사")
    printNodes(head)
    insertNode("사나", "솔라")
    printNodes(head)
    insertNode("재남", "문별")
    printNodes(head)

node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5

print(node1.data, end=', ')
print(node1.link.data, end=', ')
print(node1.link.link.data, end=', ')
print(node1.link.link.link.data, end=', ')
print(node1.link.link.link.link.data, end=' ')

new_node = Node()
new_node.data = "재남"
new_node.link = node3
node2.link = new_node

current = node1
print(current.data, end=', ')

while current.link is not None:
    current = current.link
    print(current.data, end=', ')

node2.link = node3
del new_node