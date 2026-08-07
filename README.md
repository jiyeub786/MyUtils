# 🔄 Oracle to MySQL/PostgreSQL Heterogeneous DB Migration Engine

> **Oracle 데이터베이스의 스키마 및 데이터를 MySQL 및 PostgreSQL로 자동 변환하고 이관하는 Python 기반 ETL 파이프라인 엔진입니다.**

---

## 📌 Key Features (주요 기능)

* **Dynamic DDL & DML Generation**: Oracle Data Dictionary(`DBA_TABLES`, `DBA_TAB_COLUMNS`)를 분석하여 Target DB(MySQL/PostgreSQL)용 `CREATE TABLE` DDL 및 Bind Parameter `INSERT` 쿼리를 자동 생성합니다.
* **Multi-Target DB Support**: 단일 메타 구조에서 MySQL(`MigOacleToMysqlMain.py`) 및 PostgreSQL(`MigOacleToPostgresqlMain.py`) 대상의 개별 실행 엔트리포인트를 독립 제공합니다.
* **Automated Type Mapping**: `NUMBER`, `DATE`, `CLOB` 등 DBMS 간 미스매치되는 데이터 타입을 Target DB 규격에 맞춰 자동 매핑합니다.
* **Chunk-based Bulk Insert**: Application 메모리 부하(OOM) 방지 및 네트워크 I/O 최적화를 위해 `fetchmany` 기반 Bulk Chunking을 적용했습니다.
* **Fault Tolerance & Logging**: 이관 중 에러 발생 시 트랜잭션을 안전하게 Rollback하고, 실패 원인 데이터와 스택 트레이스를 `mig_tbl_failed` 테이블에 자동 격리 저장합니다.

---

## 🏗️ Architecture & Workflow

```
[Oracle DB] ────────► [1. Meta Table (mig_tbl_list)] ───► Dynamic DDL / DML
                                                                │
                                                                ▼
[MySQL / Postgres] ◄── [2. Main Migration Scripts] ◄────────────┘
  (Target DBs)         Bulk Insert / Type Conversion / Logging
```

1. **Meta Data Analysis**: Oracle Data Dictionary 기반 메타 쿼리를 실행하여 마이그레이션 대상 테이블 목록과 동적 DDL/DML을 담은 `mig_tbl_list` 테이블을 생성합니다.
2. **Data Extraction & Transformation**: Python 스크립트가 Chunk 단위로 데이터를 Fetch한 뒤, Python 객체 및 날짜/LOB 타입을 Target DB 호환 타입으로 변환합니다.
3. **Bulk Loading**: 타깃 DB 호환 메인 스크립트(`MigOacleToMysqlMain.py` / `MigOacleToPostgresqlMain.py`)를 통해 Bulk Insert 및 Commit을 수행합니다.
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
.
├── app/
│   ├── Mains/                      # 실행 메인 모듈
│   │   ├── DQ/                     # Data Quality (데이터 정합성 검증)
│   │   ├── MigOacleToMysqlMain.py  # Oracle -> MySQL 이관 실행 파일
│   │   └── MigOacleToPostgresqlMain.py # Oracle -> PostgreSQL 이관 실행 파일
│   └── PyClass/                    # 공통 모듈 및 DB Wrapper
│       ├── MysqlClass.py           # MySQL Connection & CRUD Wrapper
│       ├── OracleClass.py          # Oracle Connection & CRUD Wrapper
│       ├── TimeClass.py            # Execution Time Tracker
│       └── LoggerClass.py          # System Logging Helper
└── README.md
```

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.8+
* `cx_Oracle` / `oracledb`
* `pymysql` / `psycopg2`

### 2. Setup Meta Tables (Oracle)
Oracle DB 접속 후 메타데이터 생성 DDL/DML 쿼리를 실행하여 `mig_tbl_list` 및 `mig_tbl_failed` 테이블을 사전에 생성합니다.

### 3. Run Migration Main Scripts

타깃 DB 환경에 맞는 실행 파일 경로를 지정하여 마이그레이션을 진행합니다.

```bash
# Oracle -> MySQL 이관 실행
python app/Mains/MigOacleToMysqlMain.py

# Oracle -> PostgreSQL 이관 실행
python app/Mains/MigOacleToPostgresqlMain.py
```

---

## 🛡️ Exception Handling & Audit Log

이관 실패 시 메타 데이터의 `target_yn` 값이 유지되며, `mig_tbl_failed` 테이블에 에러 원인이 세부 기록되어 재시도(Retry) 파이프라인 구성이 용이합니다.

```sql
-- 실패 이력 조회 예시
SELECT table_name, failed_desc, exception_desc, creat_dt 
FROM eduoracle.mig_tbl_failed;
```
