-- 인덱스 생성(func 인덱스 포함)
WITH ind_cols AS (
    SELECT
        ic.table_name,
        ic.index_name,
        ic.column_position,
        ic.column_name,
        -- SYS_NC로 시작하는 컬럼(함수 인덱스)은 user_ind_expressions에서 LONG 표현식을 추출
        CASE
            WHEN ic.column_name LIKE 'SYS_NC%' THEN
                REPLACE(
                    UTL_I18N.UNESCAPE_REFERENCE(
                        DBMS_XMLGEN.GETXMLTYPE(
                            'SELECT column_expression FROM user_ind_expressions ' ||
                            'WHERE table_name = ''' || ic.table_name || ''' ' ||
                            '  AND index_name = ''' || ic.index_name || ''' ' ||
                            '  AND column_position = ' || ic.column_position
                        ).EXTRACT('//COLUMN_EXPRESSION/text()').GETSTRINGVAL()
                    ),
                    '"', ''
                )
            ELSE
                ic.column_name
        END AS expr_text,
        CASE WHEN ic.column_name LIKE 'SYS_NC%' THEN 1 ELSE 0 END AS is_function
    FROM user_ind_columns ic
)
SELECT 'CREATE ' || CASE WHEN i.uniqueness = 'UNIQUE' THEN 'UNIQUE ' ELSE '' END ||
       'INDEX ' || LOWER(i.index_name) ||
       ' ON ' || LOWER(i.table_name) ||
       ' (' || LISTAGG(
                   CASE
                       -- MySQL 8.0 규격: 함수 표현식은 괄호 () 로 감싸야함
                       WHEN c.is_function = 1 THEN '(' || LOWER(c.expr_text) || ')'
                       ELSE LOWER(c.expr_text)
                   END, ', '
               ) WITHIN GROUP (ORDER BY c.column_position) || ');' AS mysql_ddl
FROM user_indexes i
JOIN ind_cols c ON i.index_name = c.index_name AND i.table_name = c.table_name
LEFT JOIN user_constraints u ON i.index_name = u.constraint_name
WHERE u.constraint_name IS NULL
  AND i.generated = 'N'
GROUP BY i.table_name, i.index_name, i.uniqueness
ORDER BY i.table_name;


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
