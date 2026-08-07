# 🔄 Oracle to MySQL/PostgreSQL Heterogeneous DB Migration Engine

> **Oracle 데이터베이스의 스키마 및 데이터를 MySQL 및 PostgreSQL로 자동 변환하고 이관하는 Python 기반 ETL 파이프라인 엔진입니다.**

---

## 📌 Key Features (주요 기능)

* **Dynamic DDL & DML Generation**: Oracle Data Dictionary(`DBA_TABLES`, `DBA_TAB_COLUMNS`)를 분석하여 Target DB(MySQL/PostgreSQL)용 `CREATE TABLE` DDL 및 Bind Parameter `INSERT` 쿼리를 자동 생성합니다.
* **Automated Type Mapping**: `NUMBER`, `DATE`, `CLOB` 등 DBMS 간 미스매치되는 데이터 타입을 Target DB 규격에 맞춰 자동 매핑합니다.
* **Chunk-based Bulk Insert**: Application 메모리 부하(OOM) 방지 및 네트워크 I/O 최적화를 위해 `fetchmany` 기반 Bulk Chunking(기본 5,000건 단위)을 적용했습니다.
* **Fault Tolerance & Logging**: 이관 중 에러 발생 시 트랜잭션을 안전하게 Rollback하고, 실패 원인 데이터와 스택 트레이스를 `mig_tbl_failed` 테이블에 자동 격리 저장합니다.

---

## 🏗️ Architecture & Workflow

```
[Oracle DB] ────────► [1. Meta SQL Execution] ───► Create mig_tbl_list & DDL/DML
                                                              │
                                                              ▼
[MySQL DB]  ◄──────── [2. Python Migration Engine] ◄──────────┘
 (Target)     Bulk Insert / Type Conversion / Logging
```

1. **Meta Data Analysis**: Oracle 메타데이터 쿼리를 실행하여 마이그레이션 대상 테이블 목록과 동적 DDL/DML을 담은 `mig_tbl_list` 테이블을 생성합니다.
2. **Data Extraction & Transformation**: Python 스크립트가 Chunk 단위로 데이터를 Fetch한 뒤, Python 객체 및 날짜/LOB 타입을 Target DB 호환 타입으로 변환합니다.
3. **Bulk Loading**: MySQL/PostgreSQL Target DB에 `executemany` 방식으로 Bulk Insert 및 Commit을 수행합니다.
4. **Audit & Logging**: 성공/실패 여부를 `mig_tbl_list`에 업데이트하고, 실패 건은 `mig_tbl_failed`에 이력을 기록합니다.

---

## 📊 Data Type Mapping Rules

| Oracle Source Type | MySQL Target Type | PostgreSQL Target Type | Note |
| :--- | :--- | :--- | :--- |
| `VARCHAR2(n)` / `CHAR(n)` | `VARCHAR(n)` / `CHAR(n)` | `VARCHAR(n)` / `CHAR(n)` | |
| `NUMBER` (Scale Null) | `DOUBLE` | `DECIMAL(p, 0)` | 정수/실수 유연 처리 |
| `NUMBER(p, s)` | `DECIMAL(p, s)` | `DECIMAL(p, s)` | 고정 소수점 |
| `DATE` | `DATETIME` | `TIMESTAMP` | ISO Format 변환 |
| `CLOB` | `LONGBLOB` | `TEXT` | String 캐스팅 변환 |

---

## 📂 Project Structure

```
├── app/
│   └── PyClass/
│       ├── MysqlClass.py     # MySQL Connection & CRUD Wrapper
│       ├── OracleClass.py    # Oracle Connection & CRUD Wrapper
│       ├── TimeClass.py      # Execution Time & Duration Tracker
│       └── LoggerClass.py    # System Logging Helper
├── sql/
│   └── generate_meta.sql     # Data Dictionary 분석 및 메타 테이블 생성 SQL
├── migration_engine.py       # Main Migration ETL Pipeline Script
└── README.md
```

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.8+
* `cx_Oracle` or `oracledb`
* `pymysql` or `mysql-connector-python`

### 2. Setup Meta Tables (Oracle)
Oracle DB 접속 후 `sql/generate_meta.sql` 구문을 실행하여 데이터 이관 정보 테이블(`mig_tbl_list`) 및 에러 로그 테이블(`mig_tbl_failed`)을 준비합니다.

```sql
-- Oracle DB에서 실행
@sql/generate_meta.sql
```

### 3. Run Migration Engine
DB 접속 정보를 설정한 후 마이그레이션 스크립트를 실행합니다.

```bash
python migration_engine.py
```

---

## 🛡️ Exception Handling & Audit Log

이관 실패 시 메타 데이터의 `target_yn` 값이 유지되며, `mig_tbl_failed` 테이블에 에러 원인이 세부 기록되어 재시도(Retry) 파이프라인 구성이 용이합니다.

```sql
-- 실패 이력 조회 예시
SELECT table_name, failed_desc, exception_desc, creat_dt 
FROM eduoracle.mig_tbl_failed;
```
