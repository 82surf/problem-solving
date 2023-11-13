// 문자열이 알파벳인지 확인하는 함수
function isAlpha(s) {
  return /^[a-zA-Z]*$/.test(s);
}

// 문자열을 다중집합으로 변환하는 함수
function strToSet(s) {
  const result = {};
  for (let i = 0; i < s.length - 1; i++) {
    const key = s.slice(i, i + 2);
    if (isAlpha(key)) {
      const upperKey = key.toUpperCase();
      if (result.hasOwnProperty(upperKey)) {
        result[upperKey] += 1;
      } else {
        result[upperKey] = 1;
      }
    }
  }
  return result;
}

// 다중집합의 교집합을 구하는 함수
function getIntersection(set1, set2) {
  const result = { size: 0 };
  for (const [key1, val1] of Object.entries(set1)) {
    if (set2.hasOwnProperty(key1)) {
      const val2 = set2[key1];
      const minVal = Math.min(val1, val2);
      result.size += minVal;
      result[key1] = minVal;
    }
  }
  return result;
}

// 다중집합의 합집합을 구하는 함수
function getUnion(set1, set2) {
  const result = { size: 0 };

  for (const [key1, val1] of Object.entries(set1)) {
    result[key1] = val1;
    result.size += val1;
  }

  for (const [key2, val2] of Object.entries(set2)) {
    if (result.hasOwnProperty(key2)) {
      const resultVal = result[key2];
      const maxVal = Math.max(resultVal, val2);
      result.size += resultVal !== maxVal ? maxVal - resultVal : 0;
      result[key2] = maxVal;
    } else {
      result[key2] = val2;
      result.size += val2;
    }
  }
  return result;
}

function solution(str1, str2) {
  // 다중집합 변환
  const set1 = strToSet(str1);
  const set2 = strToSet(str2);

  // 교집합, 합집합 구하기
  const intersection = getIntersection(set1, set2);
  const union = getUnion(set1, set2);

  // 자카드 유사도 구하기
  const answer = parseInt(
    union.size === 0 ? 65536 : (intersection.size / union.size) * 65536
  );

  return answer;
}
