function solution(s) {
  const nums = s.split(" ").map((n) => Number(n));
  const answer = [Math.min(...nums), Math.max(...nums)].join(" ");
  return answer;
}
