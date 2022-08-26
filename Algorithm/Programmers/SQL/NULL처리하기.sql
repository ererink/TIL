-- 입양 게시판에 동물 정보를 게시하려 합니다. 
-- 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 
-- 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.


SELECT ANIMAL_TYPE,  
    CASE 
        WHEN NAME IS NULL THEN 'No name'
        ELSE NAME
    END AS NAME
    , SEX_UPON_INTAKE
FROM ANIMAL_INS;