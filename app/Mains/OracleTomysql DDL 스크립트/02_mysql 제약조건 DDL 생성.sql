
--pk 제약조건 생성
SELECT 'ALTER TABLE ' || LOWER(table_name) ||
       ' ADD PRIMARY KEY (' || LOWER(LISTAGG(column_name, ', ') WITHIN GROUP (ORDER BY position)) || ');' AS mysql_ddl
FROM user_constraints
JOIN user_cons_columns USING (constraint_name, table_name)
WHERE constraint_type = 'P'
GROUP BY table_name, constraint_name
ORDER BY table_name;
