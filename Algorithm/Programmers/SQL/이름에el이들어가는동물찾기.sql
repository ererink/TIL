-- 보호소에 돌아가신 할머니가 기르던 개를 찾는 사람이 찾아왔습니다. 
-- 이 사람이 말하길 할머니가 기르던 개는 이름에 'el'이 들어간다고 합니다. 
-- 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS 
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME;