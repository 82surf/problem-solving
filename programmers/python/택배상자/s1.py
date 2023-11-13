def solution(order):
    container_box = 1
    sub_container = {'stack': []}
    truck = []

    def push_box(n):
        sub_container['stack'].append(n)
        sub_container[n] = True

    def pop_box():
        n = sub_container['stack'].pop()
        sub_container.pop(n)
        return n

    for o in order:
        if o in sub_container:
            if sub_container['stack'][-1] == o:
                box = pop_box()
                truck.append(box)
            else:
                break
        else:
            while o != container_box:
                push_box(container_box)
                container_box += 1
            truck.append(container_box)
            container_box += 1

    return len(truck)