
-- 시퀀스 테이블
CREATE TABLE sys_sequences (
    sequence_name VARCHAR(64) NOT NULL COMMENT '시퀀스명',
    current_val BIGINT NOT NULL DEFAULT 0 COMMENT '현재값',
    increment_by INT NOT NULL DEFAULT 1 COMMENT '증가값',
    PRIMARY KEY (sequence_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



-- 오라클 딕셔너리에서 mysql 시퀀스테이블 데이터 일괄입력
SELECT
    'INSERT INTO sys_sequences (sequence_name, current_val, increment_by) VALUES ('''
    || sequence_name || ''', '
    || (last_number - increment_by) || ', '
    || increment_by || ');' AS mysql_insert_script
FROM user_sequences;





DELIMITER //

CREATE FUNCTION NEXTVAL(p_seq_name VARCHAR(64))
RETURNS BIGINT
DETERMINISTIC
BEGIN
    DECLARE v_val BIGINT;

    -- 동시성 및 원자성을 보장하면서 값 증가
    UPDATE sys_sequences
    SET current_val = LAST_INSERT_ID(current_val + increment_by)
    WHERE sequence_name = p_seq_name;

    RETURN LAST_INSERT_ID();
END //

DELIMITER ;

/*
Oracle: SELECT SEQ_BOARD_ID.NEXTVAL FROM DUAL;
MySQL: SELECT NEXTVAL('SEQ_BOARD_ID');

 */