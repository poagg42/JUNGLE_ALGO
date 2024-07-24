class Node:
    def __init__(self, data):
        self.data = data # data는 값을 가리키는 변수(속성, attribute)
        self.next = None # next는 다음 노드를 가리키는 변수

# 연결 리스트를 만드는 과정
# 1. 첫째 노드를 만들고 head라는 이름표를 붙인다.
# 2. 둘째 노드를 만들고 head의 next가 둘째 노드를 가리키도록 한다.
# 3. 셋째 노드를 만들고 head의 next의 next가 셋째 노드를 가리키도록 한다.

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

node = head 

while node.next: 
    node = node.next 

node.next = Node(4)


# 첫 노드(head) 앞에 0 추가
# node = Node(0)
# node.next = head 
# head = node







