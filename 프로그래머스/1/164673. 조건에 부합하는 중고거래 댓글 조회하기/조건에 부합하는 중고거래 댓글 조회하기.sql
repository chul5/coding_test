-- 코드를 입력하세요
SELECT ugb.title, ugb.board_id, ugr.reply_id, ugr.writer_id, ugr.contents, DATE_FORMAT(ugr.created_date, '%Y-%m-%d') AS created_date
FROM used_goods_board ugb
INNER JOIN used_goods_reply ugr
ON ugb.board_id = ugr.board_id
WHERE DATE_FORMAT(ugb.created_date, '%Y-%m') = '2022-10'
ORDER BY ugr.created_date ASC, ugb.title ASC

