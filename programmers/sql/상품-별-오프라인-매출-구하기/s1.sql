SELECT B.PRODUCT_CODE, A.SUM_AMOUNT * B.PRICE AS SALES
FROM (
    SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS SUM_AMOUNT
    FROM OFFLINE_SALE
    GROUP BY PRODUCT_ID
) AS A
JOIN PRODUCT B
ON A.PRODUCT_ID = B.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE;