# 런타임 에러

import sys
sys.stdin = open('input.txt')


class Node:
    def __init__(self, id=None, w=None, prev=None, next=None):
        self.id = id
        self.w = w
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'<Node id: {self.id}, w: {self.w}>'


class DList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.dic = {}
        self.is_broken = False

    def break_belt(self):
        self.is_broken = True

    def is_empty(self):
        return self.head is None

    # O(1)
    def get_node(self, id):
        return self.dic[id] if id in self.dic else None

    # O(1)
    def append(self, id, w):
        new_node = Node(id, w)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
            self.dic[id] = new_node
        else:
            last_node = self.tail
            new_node.prev = last_node
            last_node.next = new_node
            self.tail = new_node
            self.dic[id] = new_node

    # O(1)
    def popleft(self):
        if self.is_empty():
            return None
        else:
            old_head = self.head
            new_head = old_head.next
            new_head.prev = None
            self.head = new_head
            self.dic.pop(old_head.id)
            return old_head

    # O(1)
    # 300 물건 제거
    def pop(self, id):
        target = self.get_node(id)
        if target:
            if target is self.head:
                self.head = target.next
                self.head.prev = None
            elif target is self.tail:
                self.tail = target.prev
                self.tail.next = None
            else:
                target.prev.next = target.next
                target.next.prev = target.prev
            self.dic.pop(id)
            return target
        else:
            return None

    # O(1)
    # 200 물건 하차
    def drop_box(self, w_max):
        if self.head.w <= w_max:
            node = self.popleft()
            return node.w
        else:
            old_head = self.popleft()
            self.append(old_head.id, old_head.w)
            return 0

    # O(1)
    # 400 물건 확인
    def find_box(self, f_id):
        target = self.get_node(f_id)
        old_head = self.head
        old_tail = self.tail
        if target:
            # 기존 head와 tail 연결
            old_head.prev = old_tail
            old_tail.next = old_head
            # 새로운 tail 설정
            self.tail = target.prev
            self.tail.next = None
            # 새로운 head 설정
            self.head = target
            self.head.prev = None
            return target
        else:
            return None

    def print_nodes(self):
        curr = self.head
        while curr.next is not None:
            print(curr.id, curr.w)
            curr = curr.next
        print(curr.id, curr.w)

    def print_dic(self):
        print(self.dic)

    def get_nodes(self):
        result = []
        curr = self.head
        while True:
            result.append(curr)
            if curr is self.tail:
                break
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
# 출력
for belt in belts:
    if not belt.is_broken:
        nodes = belt.get_nodes()
        print(nodes)
print()

job_name = {
    200: '물건 하차',
    300: '물건 제거',
    400: '물건 확인',
    500: '벨트 고장'
}
for job_num in range(1, q):
    job_code, val = map(int, input().split())
    print(f'job code: {job_name[job_code]}, val: {val}')

    if job_code == 200:
        total_w = 0
        for belt in belts:
            if not belt.is_broken:
                w = belt.drop_box(val)
                if w:
                    total_w += w
        print(total_w)

    elif job_code == 300:
        for belt in belts:
            if not belt.is_broken:
                node = belt.pop(val)
                if node:
                    print(node.id)
                    break
        else:
            print(-1)

    elif job_code == 400:
        for idx, belt in enumerate(belts):
            if not belt.is_broken:
                node = belt.find_box(val)
                if node:
                    print(idx + 1)
                    break
        else:
            print(-1)
    else:
        target_belt = belts[val-1]
        if target_belt.is_broken:
            print(-1)
        else:
            # 벨트 멈추기
            target_belt.break_belt()
            # 새로 연결할 벨트 찾기
            new_belt_idx = val % len(belts)
            while belts[new_belt_idx].is_broken:
                new_belt_idx += 1
            new_belt = belts[new_belt_idx]
            # 새로운 벨트에 연결하기
            new_belt.tail.next = target_belt.head
            new_belt.tail = target_belt.tail
            new_belt.dic.update(target_belt.dic)
            print(val)

    # 출력
    for belt in belts:
        if not belt.is_broken:
            nodes = belt.get_nodes()
            print(nodes)
    print()