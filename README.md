# 김성완 202630106

## 11월 19일

## 그래프(Graph)의 기본 구조와 인접 행렬을 이용한 그래프 생성 및 출력

## 그래프 클래스 선언

class graph():
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 그래프 출력

def print_graph(graph):
    print("=== 그래프 정보 출력 ===")
    for row in range(graph.size):
        for col in range(graph.size):
            print(graph.graph[row][col], end="")
        print()

## 전역 변수 선언

G1, G3 = None, None

## G1 그래프 생성 및 데이터 삽입

G1 = graph(4)
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1

## G1 무방향 그래프 출력

print("=== G1 무방향 그래프 ==")
for row in range(G1.size):
    for col in range(G1.size):
        print(G1.graph[row][col], end='')
    print()

## G3 그래프 생성 및 데이터 삽입

G3 = graph(4)
G3.graph[0][1] = 1
G3.graph[0][2] = 1
G3.graph[3][0] = 1
G3.graph[3][2] = 1

## G3 그래프 출력

print("=== G3 무방향 그래프 ===")
for row in range(G3.size):
    for col in range(G3.size):
        print(G3.graph[row][col], end='')

## 11월 12일

## 이진 트리의 기본 구조와 데이터 연결

## 노드 클래스 생성 tree_node()

class tree_node:
    def __init__(self):
        self.data = data
        self.left = None
        self.right = None
    
## 첫 번째 노드 생성 

node1 = tree_node()
node1.data = "커피"

## 두 번째 세 번째 노드 연결

node2 = tree_node()
node2.data = "우유"
node1.left = node2

node3 = tree_node()
node3.data = "주스"
node1.right = node3

node2에 "우유" 저장 후 첫 번째 노드의 왼쪽에 연결함
node3에 "주스" 저장 후 첫 번째 노드의 오른쪽에 연결함


## 네 번째 다섯 번째 노드 연결

node4 = tree_node()
node4.data = "물"
node2.left = node4

node5 = tree_node()
node5.data = "콜라"
node2.right = node5

node4에 "물"을 저장하고 두 번째 노드의 왼쪽에 연결함
node5에 "콜라"를 저장하고 두 번째 노드의 오른쪽에 연결함

## 여섯 번째 노드 연결

node6 = tree_node()
node6.data = "사이다"
node3.left = node6

node6에 "사이다"를 저장하고 세 번째 노드의 왼쪽 자식 노드로 연결함

## 이진 트리 구조 출력

print("=== 이진 트리 구조 ===")
print(node1.data,end=" ")
print()
print(node1.left.data, node1.right.data,end=" ")
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)

##  이진 트리 구조 결과

=== 이진 트리 구조 ===
커피
우유 주스
물 콜라 사이다

## 11월 5일

## 큐(Queue)의 기본 구조와 데이터 삽입 및 삭제

## 큐 초기화 init_queue()

def init_queue(size):
    global print_q, front, rear
    print_q = [None] * size
    front = -1
    rear = -1
    return print("큐 초기화 완료: 크기=" + str(size))

## 큐 데이터 삽입 enqueue()

def enqueue(data):
    global rear
    rear += 1
    print_q[rear] = data
    return print("현재 rear:" + str(rear))

## 큐 데이터 삭제 dequeue()

def dequeue():
    global front, temp
    if is_queue_empty():
        return print("큐가 비어있습니다! 삭제할 데이터가 없습니다.")
    front += 1
    temp = print_q[front]
    print_q[front] = None
    return temp

## 큐 데이터 확인 peek()

def peek():
    global front
    if is_queue_empty():
        return print("큐가 비어있습니다! peek 불가!")
    else:
        temp = print_q[front + 1]
        return temp

## 큐가 비어 있는지 확인 is_queue_empty()

def is_queue_empty():
    global front, rear
    if front == rear:
        return True
    else:
        return False

## 큐가 가득 찼는지 확인 is_queue_full()

def is_queue_full():
    global rear
    if rear == len(print_q) - 1:
        return True
    else:
        return False

## 큐 전체 상태 출력 print_queue()

def print_queue():
    print("=== 큐 상태 ===")
    print("큐의 크기:" + str(len(print_q)))
    for i in range(len(print_q)):
        print(print_q[i])
    print("현재 front:" + str(front))
    print("현재 rear:" + str(rear))
    print("================")

## 큐 초기화

init_queue(5)

## 큐에 데이터 삽입

enqueue("커피")
enqueue("우유")
enqueue("주스")
enqueue("물")
enqueue("콜라")
enqueue("사이다")

## 현재 큐 출력

print_queue()

## 큐의 첫 번째 데이터 삭제

dequeue()
print_queue()

## 큐 데이터 삭제 및 반환값 출력

print(dequeue())
dequeue()

## 10월 29일

## 스택의 개념

## 스택 초기화 init_stack()

def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    print("스택 초기화 완료: 크기=" + str(size))

## 스택 데이터 삽입 push()

def push(data):
    global top
    if is_stack_full():
        return print("스택이 가득 찼습니다.")

    else:
        top += 1
        stack[top] = data
        return print("현재 top:" + str(top))

## 스택 데이터 삭제 pop()

def pop():
    global top
    if is_stack_empty():
        return print("스택이 비어있습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
    return print("Pop된 데이터:" + str(data) + ", 현재 top:" + str(top))

## 스택 데이터 확인 peek()

def peek():
    global top
    if is_stack_empty():
        return print("스택이 비어있습니다.")
    else:
        data = stack[top]
    return print("Peek된 데이터:" + str(data) + ", 현재 top:" + str(top))

## 스택이 가득 찼는지 확인 is_stack_full()

def is_stack_full():
    global top
    if top == len(stack) - 1:
        return True
    else:
        return False

## 스택이 비어 있는지 확인 is_stack_empty()

def is_stack_empty():
    global top
    if top == -1:
        return True
    else:
        return False

## 스택 데이터 출력 print_stack()

def print_stack():
    print("현재 스택:", stack)
    print("현재 top:", top)

## 스택 초기화

init_stack(7)

## 스택에 데이터 삽입

push("커피")
push("녹차")
push("꿀물")
push("레몬차")
push("오렌지주스")
push("밀크티")
push("아이스티")

## 현재 스택 출력

print_stack()

## 스택의 가장 위 데이터 확인

peek()

## 스택 데이터 삭제

pop()
pop()
pop()
pop()
pop()
pop()
pop()

## 10월 15일 (6주차)

## 연결 리스트를 만들기 위한 전역변수 선언

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 첫 번째 노드 생성 및 head 지정

if __name__ == "__main__":
    node = Node() #첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

## 두 번째 이후 노드 생성 및 연결

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

## 연결 리스트의 데이터 삽입 (첫 번째 위치)

insertNode("다현", "화사")
printNodes(head)

## 연결 리스트의 데이터 삽입 (중간 위치)

insertNode("사나", "솔라")
printNodes(head)

## 연결 리스트의 데이터 삽입 (찾는 데이터가 없는 경우)

insertNode("재남", "문별")
printNodes(head)

## 연결 리스트의 수동 생성과 연결

## 첫 번째 노드 생성

node1 = Node()
node1.data = "다현"

## 두 번째 노드 생성 및 연결

node2 = Node()
node2.data = "정연"
node1.link = node2

## 세 번째 노드 생성 및 연결

node3 = Node()
node3.data = "쯔위"
node2.link = node3

## 네 번째 노드 생성 및 연결

node4 = Node()
node4.data = "사나"
node3.link = node4

## 다섯 번째 노드 생성 및 연결

node5 = Node()
node5.data = "지효"
node4.link = node5

## 연결 리스트의 데이터 출력 (link 이용)

print(node1.data, end=', ')
print(node1.link.data, end=', ')
print(node1.link.link.data, end=', ')
print(node1.link.link.link.data, end=', ')
print(node1.link.link.link.link.data, end=' ')

## 새로운 노드 생성 및 중간 삽입

new_node = Node()
new_node.data = "재남"
new_node.link = node3
node2.link = new_node

## 연결 리스트의 데이터 순차 출력 (while문)

current = node1
print(current.data, end=', ')

while current.link is not None:
    current = current.link
    print(current.data, end=', ')

## 10월 08일 (5주차)

## 연결 리스트의 기본 구조와 삽입

class Node:
    def __init__(self):
        self.data = None
        self.link = None

## 연결 리스트의 데이터 출력

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=', ')
    while current.link != None:
        current = current.link
        print(current.data, end=', ')
    print()

## 연결 리스트의 데이터 삽입(첫 번째 노드)

if current.data == findData:
    node = Node()
    node.data = insertData
    node.link = head
    head = node
    return

## 연결 리스트의 데이터 삽입 (중간 노드)

while current.link != None:
    pre = current
    current = current.link
    if current.data == findData:
        node = Node()
        node.data = insertData
        node.link = current
        pre.link = node
        return

## 연결 리스트의 데이터 삽입 (마지막 노드)

node = Node()
node.data = insertData
current.link = node

## 10월 1일 (4주차)

## 선형 리스트 활용

## 데이터 Swap temp를 이용한 리스트의 두 데이터 위치 교환

kakao = ["가나", "다리", "마비","시아","치치"]
temp = kakao[4]
print(kakao)
kakao.append("삽입")
print(kakao)
kakao[4] = kakao[5]
kakao[5] = temp
temp = kakao[3]
print(kakao)
kakao[3] = kakao[4]
kakao[4] = temp
print(kakao)

## append(), for(), len(), range()를 이용한 리스트 생성

kakao = []
kakao_len = len(kakao)
kakao.append ("다현")
kakao.append ("정연")
kakao.append ("쯔위")
kakao.append ("사나")
kakao.append ("지효")

## 연결 리스트의 기본 구조와 삽입과 삭제

for i in range(len(kakao)):
    print(kakao[i], end=', ')

## 9월 17일 (3주차)

## 파이썬 기본 출력과 리스트 인덱싱, 임시 변수를 활용한 데이터 삽입 및 스왑 실습

kakao = ["가나", "다리", "마비","시아","치치"]
print(kakao)
print(kakao[0])
print(kakao[4])
kakao.append(None)
print(kakao)
kakao[5] = kakao[4]
kakao[4] = None
print(kakao)
kakao[4] = kakao[3]
kakao[3] = None
print(kakao)
kakao[3] = "삽입"
print(kakao)
kakao[3] = None
print(kakao)
kakao[3] = kakao[4]
kakao[4] = None
print(kakao)
kakao[4] = kakao[5]
kakao[5] = None
print(kakao)

kakao = ["가나", "다리", "마비","시아","치치"]
temp = kakao[4]
print(kakao)
kakao.append("삽입")
print(kakao)
kakao[4] = kakao[5]
kakao[5] = temp
temp = kakao[3]
print(kakao)
kakao[3] = kakao[4]
kakao[4] = temp
print(kakao)

## 11월 5일

## 큐(Queue)의 기본 구조와 데이터 삽입 및 삭제

## 큐 초기화 init_queue()

def init_queue(size):
    global print_q, front, rear
    print_q = [None] * size
    front = -1
    rear = -1
    return print("큐 초기화 완료: 크기=" + str(size))

## 큐 데이터 삽입 enqueue()

def enqueue(data):
    global rear
    rear += 1
    print_q[rear] = data
    return print("현재 rear:" + str(rear))

## 큐 데이터 삭제 dequeue()

def dequeue():
    global front, temp
    if is_queue_empty():
        return print("큐가 비어있습니다! 삭제할 데이터가 없습니다.")
    front += 1
    temp = print_q[front]
    print_q[front] = None
    return temp

## 큐 데이터 확인 peek()

def peek():
    global front
    if is_queue_empty():
        return print("큐가 비어있습니다! peek 불가!")
    else:
        temp = print_q[front + 1]
        return temp

## 큐가 비어 있는지 확인 is_queue_empty()

def is_queue_empty():
    global front, rear
    if front == rear:
        return True
    else:
        return False

## 큐가 가득 찼는지 확인 is_queue_full()

def is_queue_full():
    global rear
    if rear == len(print_q) - 1:
        return True
    else:
        return False

## 큐 전체 상태 출력 print_queue()

def print_queue():
    print("=== 큐 상태 ===")
    print("큐의 크기:" + str(len(print_q)))
    for i in range(len(print_q)):
        print(print_q[i])
    print("현재 front:" + str(front))
    print("현재 rear:" + str(rear))
    print("================")

## 큐 초기화

init_queue(5)

## 큐에 데이터 삽입

enqueue("커피")
enqueue("우유")
enqueue("주스")
enqueue("물")
enqueue("콜라")
enqueue("사이다")

## 현재 큐 출력

print_queue()

## 큐의 첫 번째 데이터 삭제

dequeue()
print_queue()

## 큐 데이터 삭제 및 반환값 출력

print(dequeue())
dequeue()

## 10월 29일

## 스택의 개념

## 스택 초기화 init_stack()

def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    print("스택 초기화 완료: 크기=" + str(size))

## 스택 데이터 삽입 push()

def push(data):
    global top
    if is_stack_full():
        return print("스택이 가득 찼습니다.")

    else:
        top += 1
        stack[top] = data
        return print("현재 top:" + str(top))

## 스택 데이터 삭제 pop()

def pop():
    global top
    if is_stack_empty():
        return print("스택이 비어있습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
    return print("Pop된 데이터:" + str(data) + ", 현재 top:" + str(top))

## 스택 데이터 확인 peek()

def peek():
    global top
    if is_stack_empty():
        return print("스택이 비어있습니다.")
    else:
        data = stack[top]
    return print("Peek된 데이터:" + str(data) + ", 현재 top:" + str(top))

## 스택이 가득 찼는지 확인 is_stack_full()

def is_stack_full():
    global top
    if top == len(stack) - 1:
        return True
    else:
        return False

## 스택이 비어 있는지 확인 is_stack_empty()

def is_stack_empty():
    global top
    if top == -1:
        return True
    else:
        return False

## 스택 데이터 출력 print_stack()

def print_stack():
    print("현재 스택:", stack)
    print("현재 top:", top)

## 스택 초기화

init_stack(7)

## 스택에 데이터 삽입

push("커피")
push("녹차")
push("꿀물")
push("레몬차")
push("오렌지주스")
push("밀크티")
push("아이스티")

## 현재 스택 출력

print_stack()

## 스택의 가장 위 데이터 확인

peek()

## 스택 데이터 삭제

pop()
pop()
pop()
pop()
pop()
pop()
pop()

## 10월 15일 (6주차)

## 연결 리스트를 만들기 위한 전역변수 선언

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 첫 번째 노드 생성 및 head 지정

if __name__ == "__main__":
    node = Node() #첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

## 두 번째 이후 노드 생성 및 연결

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

## 연결 리스트의 데이터 삽입 (첫 번째 위치)

insertNode("다현", "화사")
printNodes(head)

## 연결 리스트의 데이터 삽입 (중간 위치)

insertNode("사나", "솔라")
printNodes(head)

## 연결 리스트의 데이터 삽입 (찾는 데이터가 없는 경우)

insertNode("재남", "문별")
printNodes(head)

## 연결 리스트의 수동 생성과 연결

## 첫 번째 노드 생성

node1 = Node()
node1.data = "다현"

## 두 번째 노드 생성 및 연결

node2 = Node()
node2.data = "정연"
node1.link = node2

## 세 번째 노드 생성 및 연결

node3 = Node()
node3.data = "쯔위"
node2.link = node3

## 네 번째 노드 생성 및 연결

node4 = Node()
node4.data = "사나"
node3.link = node4

## 다섯 번째 노드 생성 및 연결

node5 = Node()
node5.data = "지효"
node4.link = node5

## 연결 리스트의 데이터 출력 (link 이용)

print(node1.data, end=', ')
print(node1.link.data, end=', ')
print(node1.link.link.data, end=', ')
print(node1.link.link.link.data, end=', ')
print(node1.link.link.link.link.data, end=' ')

## 새로운 노드 생성 및 중간 삽입

new_node = Node()
new_node.data = "재남"
new_node.link = node3
node2.link = new_node

## 연결 리스트의 데이터 순차 출력 (while문)

current = node1
print(current.data, end=', ')

while current.link is not None:
    current = current.link
    print(current.data, end=', ')

## 10월 08일 (5주차)

## 연결 리스트의 기본 구조와 삽입

class Node:
    def __init__(self):
        self.data = None
        self.link = None

## 연결 리스트의 데이터 출력

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=', ')
    while current.link != None:
        current = current.link
        print(current.data, end=', ')
    print()

## 연결 리스트의 데이터 삽입(첫 번째 노드)

if current.data == findData:
    node = Node()
    node.data = insertData
    node.link = head
    head = node
    return

## 연결 리스트의 데이터 삽입 (중간 노드)

while current.link != None:
    pre = current
    current = current.link
    if current.data == findData:
        node = Node()
        node.data = insertData
        node.link = current
        pre.link = node
        return

## 연결 리스트의 데이터 삽입 (마지막 노드)

node = Node()
node.data = insertData
current.link = node

## 10월 1일 (4주차)

## 선형 리스트 활용

## 데이터 Swap temp를 이용한 리스트의 두 데이터 위치 교환

kakao = ["가나", "다리", "마비","시아","치치"]
temp = kakao[4]
print(kakao)
kakao.append("삽입")
print(kakao)
kakao[4] = kakao[5]
kakao[5] = temp
temp = kakao[3]
print(kakao)
kakao[3] = kakao[4]
kakao[4] = temp
print(kakao)

## append(), for(), len(), range()를 이용한 리스트 생성

kakao = []
kakao_len = len(kakao)
kakao.append ("다현")
kakao.append ("정연")
kakao.append ("쯔위")
kakao.append ("사나")
kakao.append ("지효")

## 연결 리스트의 기본 구조와 삽입과 삭제

for i in range(len(kakao)):
    print(kakao[i], end=', ')

## 9월 17일 (3주차)

## 파이썬 기본 출력과 리스트 인덱싱, 임시 변수를 활용한 데이터 삽입 및 스왑 실습

kakao = ["가나", "다리", "마비","시아","치치"]
print(kakao)
print(kakao[0])
print(kakao[4])
kakao.append(None)
print(kakao)
kakao[5] = kakao[4]
kakao[4] = None
print(kakao)
kakao[4] = kakao[3]
kakao[3] = None
print(kakao)
kakao[3] = "삽입"
print(kakao)
kakao[3] = None
print(kakao)
kakao[3] = kakao[4]
kakao[4] = None
print(kakao)
kakao[4] = kakao[5]
kakao[5] = None
print(kakao)

kakao = ["가나", "다리", "마비","시아","치치"]
temp = kakao[4]
print(kakao)
kakao.append("삽입")
print(kakao)
kakao[4] = kakao[5]
kakao[5] = temp
temp = kakao[3]
print(kakao)
kakao[3] = kakao[4]
kakao[4] = temp
print(kakao)

## 9월10일(2주차)

### 마크다운 문법

# h1 테그
## h2 테그
### h3 테그
#### h4 테그
##### h5 테그
###### h6 테그

*이텔릭체*

**볼드체**

***이텔릭+볼드체***

~~취소선~~

밑줄
---

1. 감자
2. 고구마
3. 옥수수
4. 배추

    * 감자
    * 옥수수
    * 배추
        * 배추 김치
            * 신김치

### 코드 블럭

```py
# 쉼표(,)로 구분하면 공백이 하나 추가되어 출력됩니다
print("오늘은", "일요일")
```

복사는  `Ctrl + C` 입니다.

### 링크

[깃허브 바로가기] (https://github.com/chan114/my-project)

[코드블럭](#코드-블럭 "코드블럭 예제")

![헨드 쉐이크]("C:\Users\user\Downloads\gnutls-handshake-sequence.png")

수평선
***
