# 오답
SELECT FOOD_TYPE, REST_ID, REST_NAME, MAX(FAVORITES) AS FAVORITES
FROM REST_INFO
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC;

# 왜 오답일까?
# https://school.programmers.co.kr/questions/38703
# GROUP BY 구의 기준이 되는 필드가 아니거나 집계 함수를 통해 어떤 값을 반환해야 할 지 결정해주지 않은 필드를 SELECT 구에 사용할 경우 문법적으로 틀린 SQL 구문입니다.