/**
 * 소수 여부를 판별하는 함수
 * @params {number} n
 * @returns {boolean}
 */
function isPrime(n) {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= n ** 0.5; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

function solution(n, k) {
  const kNum = n.toString(k);

  let answer = 0;
  let idx = 0;
  let numStr = "";
  while (idx < kNum.length) {
    if (kNum[idx] === "0" && numStr !== "") {
      if (isPrime(Number(numStr))) {
        answer++;
      }
      numStr = "";
    } else {
      if (kNum[idx] !== "0") {
        numStr += kNum[idx];
      }
    }
    idx++;
  }
  if (isPrime(numStr)) {
    answer++;
  }
  return answer;
}
