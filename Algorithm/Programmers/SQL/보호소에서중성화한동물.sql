-- 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 
-- 보호소에 들어올 당시에는 중성화1되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.

SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS INS LEFT OUTER JOIN ANIMAL_OUTS OUTS
 ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE != OUTS.SEX_UPON_OUTCOME
ORDER BY INS.ANIMAL_ID;