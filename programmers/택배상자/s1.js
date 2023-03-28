function solution(order) {
  let container_box = 1;
  const sub_container = { stack: [] };
  const truck = [];

  sub_container.push = function (n) {
    this.stack.push(n);
    this[n] = true;
  };

  sub_container.pop = function () {
    const n = this.stack.pop();
    delete this.n;
    return n;
  };

  sub_container.peek = function () {
    return this.stack[this.stack.length - 1];
  };

  sub_container.len = function () {
    return this.stack.length;
  };

  for (const o of order) {
    if (o in sub_container) {
      if (o === sub_container.peek()) {
        const n = sub_container.pop();
        truck.push(n);
      } else {
        break;
      }
    } else {
      while (o !== container_box) {
        sub_container.push(container_box);
        container_box++;
      }
      truck.push(container_box);
      container_box++;
    }
  }

  return truck.length;
}
