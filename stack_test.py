def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    print("스택 초기화 완료: 크기=" + str(size))


def push(data):
    global top
    if is_stack_full():
        return print("스택이 가득 찼습니다.")
    
    else:
        top += 1
        stack[top] = data
        return print("현재 top:" + str(top))

def pop():
    global top
    if is_stack_empty():
        return print("스택이 비어있습니다.")
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
    return print("Pop된 데이터:" + str(data) + ", 현재 top:" + str(top))

def peek():
    global top
    if is_stack_empty():
        return print("스택이 비어있습니다.")
    else:
        data = stack[top]
    return print("Peek된 데이터:" + str(data) + ", 현재 top:" + str(top))

def is_stack_full():
    global top
    if top == len(stack) - 1:
        return True
    else:
        return False



init_stack(7)

push("커피")
push("녹차")
push("꿀물")
push("레몬차")
push("오렌지주스")
push("밀크티")
push("아이스티")

print("콜라")

print_stack()

peek()

pop()
pop()
pop()
pop()
pop()
pop()
pop()

pop()

peek()

print_stack()