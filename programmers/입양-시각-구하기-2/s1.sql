WITH RECURSIVE CTE AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1
    FROM CTE
    WHERE HOUR < 23
),
HOURDATA AS (
    SELECT HOUR(DATETIME) AS HOUR
    FROM ANIMAL_OUTS
),
OUTDATA AS (
    SELECT HOUR, COUNT(*) AS COUNT
    FROM HOURDATA
    GROUP BY HOUR
)

SELECT CTE.HOUR, IFNULL(OUTDATA.COUNT, 0) AS COUNT
FROM CTE
LEFT JOIN OUTDATA
ON CTE.HOUR = OUTDATA.HOUR
ORDER BY HOUR