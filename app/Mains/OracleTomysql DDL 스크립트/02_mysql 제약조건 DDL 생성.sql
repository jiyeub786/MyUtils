
--pk 제약조건 생성
SELECT 'ALTER TABLE ' || LOWER(table_name) ||
       ' ADD PRIMARY KEY (' || LOWER(LISTAGG(column_name, ', ') WITHIN GROUP (ORDER BY position)) || ');' AS mysql_ddl
FROM user_constraints
JOIN user_cons_columns USING (constraint_name, table_name)
WHERE constraint_type = 'P'
GROUP BY table_name, constraint_name
ORDER BY table_name;

--fk 제약조건
SELECT 'ALTER TABLE ' || LOWER(c.table_name) ||
       ' ADD CONSTRAINT ' || LOWER(c.constraint_name) ||
       ' FOREIGN KEY (' || LOWER(LISTAGG(cc.column_name, ', ') WITHIN GROUP (ORDER BY cc.position)) || ')' ||
       ' REFERENCES ' || LOWER(r.table_name) ||
       ' (' || LOWER(LISTAGG(rc.column_name, ', ') WITHIN GROUP (ORDER BY rc.position)) || ');' AS mysql_ddl
FROM user_constraints c
JOIN user_cons_columns cc ON c.constraint_name = cc.constraint_name AND c.owner = cc.owner
JOIN user_constraints r ON c.r_constraint_name = r.constraint_name AND c.owner = r.owner
JOIN user_cons_columns rc ON r.constraint_name = rc.constraint_name AND cc.position = rc.position AND r.owner = rc.owner
WHERE c.constraint_type = 'R'
GROUP BY c.table_name, c.constraint_name, r.table_name
ORDER BY c.table_name


--default 제약조건 생성
sET SERVEROUTPUT ON SIZE UNLIMITED;

DECLARE
    v_default VARCHAR2(4000);
BEGIN
    FOR r IN (
        SELECT table_name, column_name, data_default
        FROM user_tab_cols
        WHERE data_default IS NOT NULL
          AND table_name NOT LIKE 'BIN$%' -- 삭제된 테이블(휴지통) 제외
        ORDER BY table_name, column_id
    ) LOOP
        -- LONG 타입 데이터를 VARCHAR2 변수에 할당하여 처리
        v_default := TRIM(r.data_default);

        -- 오라클 SYSDATE를 MySQL 표준 함수로 변환
        IF UPPER(v_default) LIKE '%SYSDATE%' THEN
            v_default := '(CURRENT_TIMESTAMP)';
        END IF;

        -- MySQL DDL 출력 (ALTER COLUMN ... SET DEFAULT 구문)
        DBMS_OUTPUT.PUT_LINE(
            'ALTER TABLE ' || LOWER(r.table_name) ||
            ' ALTER COLUMN ' || LOWER(r.column_name) ||
            ' SET DEFAULT ' || v_default || ';'
        );
    END LOOP;
END;
/
