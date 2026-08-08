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
