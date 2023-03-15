function solution(s) {
  arr = s
    .slice(2, -2)
    .split("},{")
    .map((nums) => nums.split(",").map((num) => Number(num)))
    .sort((a, b) => a.length - b.length);

  let answer = [];
  arr.forEach((li, idx) => {
    if (idx === 0) {
      answer.push(li[0]);
    } else {
      diff = arr[idx].filter((x) => !arr[idx - 1].includes(x));
      answer = [...answer, ...diff];
    }
  });

  return answer;
}
