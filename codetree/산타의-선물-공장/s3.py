# 최종 코드
class Node:
    def __init__(self, id, w, prev=None, next=None):
        self.id = id
        self.w = w
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'<Node id: {self.id}, w: {self.w}>'


def connect(node1, node2):
    node1.next = node2
    node2.prev = node1


class DList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.dic = {}
        self.is_broken = False

    def get_len(self):
        return len(self.dic)

    def is_empty(self):
        return not bool(self.dic)

    def disconnect(self, node):
        node.next = None
        node.prev = None
        if node.id in self.dic:
            self.dic.pop(node.id)

    def append(self, id, w):
        node = Node(id, w)
        if self.is_empty():
            connect(self.head, node)
            connect(node, self.tail)
        else:
            last_node = self.tail.prev
            connect(last_node, node)
            connect(node, self.tail)
        self.dic[id] = node

    def popleft(self):
        if self.is_empty():
            return None
        else:
            first_node = self.head.next
            second_node = first_node.next
            connect(self.head, second_node)
            self.disconnect(first_node)
            return first_node

    # 300
    def pop(self, r_id):
        if r_id not in self.dic:
            return None
        else:
            target = self.dic[r_id]
            if target:
                connect(target.prev, target.next)
                self.disconnect(target)
                return target

    # 200
    def drop_box(self, w_max):
        if self.is_empty():
            return None
        else:
            first_node = self.head.next
            if first_node.w <= w_max:
                return self.popleft().w
            # 원소가 하나만 남을 경우, else문의 로직으로 빠지면 head와 tail이 연결되어 빈 배열이 되어버린다!
            elif len(self.dic) == 1:
                pass
            else:
                second_node = first_node.next
                last_node = self.tail.prev
                connect(last_node, first_node)
                connect(first_node, self.tail)
                connect(self.head, second_node)

    # 400
    def find_box(self, f_id):
        if f_id not in self.dic:
            return None
        else:
            start = self.dic[f_id]
            end = self.tail.prev

            connect(start.prev, self.tail)
            connect(end, self.head.next)
            connect(self.head, start)
            return start

    # 500
    def break_belt(self):
        if self.is_broken:
            return -1
        else:
            self.is_broken = True

    def get_nodes(self):
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append(curr)
            curr = curr.next
        return result


q = int(input())
jc, n, m, *vals = map(int, input().split())
belts = [DList() for _ in range(m)]
box_len = n // m
for i in range(m):
    start = i * box_len
    for j in range(box_len):
        id, w = vals[start + j], vals[start + j + n]
        belts[i].append(id, w)


for job_num in range(1, q):
    job_code, val = map(int, input().split())

    if job_code == 200:
        total = 0
        for belt in belts:
            if not belt.is_broken:
                weight = belt.drop_box(val)
                if weight:
                    total += weight
        print(total)

    elif job_code == 300:
        for belt in belts:
            node = belt.pop(val)
            if node:
                print(node.id)
                break
        else:
            print(-1)

    elif job_code == 400:
        for idx, belt in enumerate(belts):
            node = belt.find_box(val)
            if node:
                print(idx + 1)
                break
        else:
            print(-1)

    else:
        # 벨트 멈추기
        belt_idx = val - 1
        if belts[belt_idx].is_broken:
            print(-1)
        else:
            belts[belt_idx].break_belt()
            # 정상 가동 벨트 찾기
            while belts[belt_idx].is_broken:
                belt_idx = (belt_idx + 1) % len(belts)

            # 벨트 연결하기
            old_belt = belts[val - 1]
            new_belt = belts[belt_idx]

            connect(new_belt.tail.prev, old_belt.head.next)
            connect(old_belt.tail.prev, new_belt.tail)
            old_belt.disconnect(old_belt.head)
            old_belt.disconnect(old_belt.tail)

            # 딕셔너리 업데이트
            new_belt.dic.update(old_belt.dic)
            old_belt.dic = {}

            print(val)
