-- 보호소에 들어올 때는 중성화 X
-- 보호소를 나갈 때는 중성화
-- ANIMAL_ID, ANIMAL_TYPE, NAME
-- ID 오름차순

SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS AS I
JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE "%INTACT%" AND (O.SEX_UPON_OUTCOME LIKE "%NEUTERED%" OR O.SEX_UPON_OUTCOME LIKE "%SPAYED%")
ORDER BY ANIMAL_ID;