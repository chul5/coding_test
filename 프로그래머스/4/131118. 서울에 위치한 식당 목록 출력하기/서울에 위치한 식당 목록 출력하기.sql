-- 코드를 입력하세요
SELECT rest_id, rest_name, food_type, favorites, address, ROUND(AVG(review_score), 2) AS SCORE
FROM rest_info
NATURAL JOIN rest_review
WHERE address LIKE '서울%'
GROUP By rest_id, rest_name, food_type, favorites, address
ORDER BY score desc, favorites desc