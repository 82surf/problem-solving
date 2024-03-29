-- 완료된 게시글에서
-- 작성자 ID로 GROUP => 총 판매 금액 70만원 이상인 경우만 조회
-- USER TABLE과 JOIN

SELECT A.USER_ID, A.NICKNAME, B.TOTAL_SALES
FROM USED_GOODS_USER AS A
JOIN (
    SELECT WRITER_ID, SUM(PRICE) AS TOTAL_SALES
    FROM USED_GOODS_BOARD
    WHERE STATUS = 'DONE'
    GROUP BY WRITER_ID
    HAVING TOTAL_SALES >= 700000
) AS B
ON A.USER_ID = B.WRITER_ID
ORDER BY TOTAL_SALES;