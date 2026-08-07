# Oracle DB Migration Utilities (MyUtils)

Oracle 데이터베이스의 데이터를 MySQL 및 PostgreSQL 등 이종 데이터베이스(Heterogeneous Database)
환경으로 효율적으로 이관(Migration)하기 위한 파이썬 마이그레이션 스크립트 및 SQL 

---

## 📌 주요 기능

1. **Oracle to MySQL Migration (`MigOacleToMysqlMain.py`)**
   - Oracle 데이터베이스에서 데이터를 조회하여 MySQL 데이터베이스로 대량(Batch/Bulk) 이관합니다.
   - 데이터 타입 매핑 처리 및 인코딩/세션 설정을 지원합니다.

2. **Oracle to PostgreSQL Migration (`MigOacleToPostgresqlMain.py`)**
   - Oracle 데이터베이스에서 데이터를 조회하여 PostgreSQL 데이터베이스로 이관합니다.
   - PostgreSQL 특화 타입 및 커밋 처리 옵션을 제공합니다.

3. **Oracle 추출 및 변환 DDL/DML SQL (`MigOracleToOtherDB.sql`)**
   - Oracle 내에서 타 DB로 마이그레이션하기 위해 필요한 사전 쿼리, 테이블 스키마/컬럼 추출, 데이터 타입 변환 및 매핑 조회용 SQL 스크립트입니다.

---

## 🏗 프로젝트 구조 (Project Structure)

```text
MyUtils/
├── app/
│   ├── Mains/                      # 실행 메인 모듈
│   │   ├── MigOacleToMysqlMain.py        # Oracle -> MySQL 마이그레이션 메인 파이썬 스크립트
│   │   └── MigOacleToPostgresqlMain.py     # Oracle -> PostgreSQL 마이그레이션 메인 파이썬 스크립트
│   │   └── MigOracleToOtherDB.sql        # Oracle 스키마/타입 변환 및 DDL/DML 자동 생성 SQL
│   └── PyClass/                    # 공통 모듈 및 DB 조작모듈
│       ├── MysqlClass.py           # MySQL Connection & CRUD Wrapper
│       ├── OracleClass.py          # Oracle Connection & CRUD Wrapper
│       ├── TimeClass.py            # Execution Time Tracker
│       └── LoggerClass.py          # System Logging Helper

```

---

## 🛠 Prerequisites & Requirements

### Python 환경
- **Python 3.8+**

### 필수 파이썬 패키지
```bash
pip install cx_Oracle psycopg2-binary pymysql sqlalchemy pandas
```
*(참고: Oracle Client 라이브러리가 설치되어 있거나 Instant Client 경로가 설정되어 있어야 합니다.)*

---

## 📁 파일 상세 설명

| 파일명 | 설명 | 주요 사용 라이브러리/기술 |
| :--- | :--- | :--- |
| `MigOacleToMysqlMain.py` | Oracle -> MySQL 데이터 마이그레이션 실행 파이썬 스크립트 | `cx_Oracle`, `pymysql` / `sqlalchemy` |
| `MigOacleToPostgresqlMain.py` | Oracle -> PostgreSQL 데이터 마이그레이션 실행 파이썬 스크립트 | `cx_Oracle`, `psycopg2` / `sqlalchemy` |
| `MigOracleToOtherDB.sql` | Oracle 데이터 dictionary(ALL_TAB_COLUMNS 등) 기반 스키마 추출 및 변환 쿼리 | Oracle SQL |

---

## 🚀 사용 방법

### 1. SQL 스크립트를 통한 사전 검증 (`MigOracleToOtherDB.sql`)
마이그레이션 수행 전, Oracle 데이터베이스에서 대상 테이블의 컬럼 정보, 데이터 타입, 행 수(Row count) 등을 추출하거나 이종 DB 타입 변환 구문을 확인합니다.

 주요 핵심 로직
자동 DDL 생성: XMLAGG/XMLELEMENT 구문을 활용해 컬럼 수가 많은 테이블도 길이 제한 없이 CLOB 형태의 CREATE TABLE 구문으로 추출합니다.
동적 바인딩 DML 생성: 파이썬 배치 이관 작업 시 필요한 바인드 플레이스홀더(? 및 %s) 기반의 INSERT 문을 자동 생성합니다.
행 크기 제한 필터링: SUM_DATA_LENGTH_BYTES < 65535 조건으로 MySQL의 Row Size Limit(65,535 bytes) 제한을 사전에 검증합니다.
시스템 객체 제외: 테이블명에 $, # 등이 포함된 Oracle 내부 관리용 테이블을 이관 대상에서 제외합니다.

```sql
-- MigOracleToOtherDB.sql 활용 예시: 대상 테이블 컬럼 정보 및 타입 매핑 확인
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, DATA_LENGTH
FROM ALL_TAB_COLUMNS
WHERE OWNER = 'YOUR_ORACLE_SCHEMA';
```

---

### 2. Oracle -> MySQL 마이그레이션 (`MigOacleToMysqlMain.py`)

1. 스크립트 내부의 Oracle 및 MySQL 접속 정보(Host, Port, User, Password, DB/Service Name)를 설정합니다.
2. 실행:
```bash
python MigOacleToMysqlMain.py
```

---

### 3. Oracle -> PostgreSQL 마이그레이션 (`MigOacleToPostgresqlMain.py`)

1. 스크립트 내부의 Oracle 및 PostgreSQL 접속 정보를 설정합니다.
2. 실행:
```bash
python MigOacleToPostgresqlMain.py
```

---

## ⚙️ 주요 설정 옵션 (Configuration)

스크립트 실행 시 공통적으로 설정해야 하는 항목:

```python
# Oracle 접속 정보 설정
ORACLE_CONFIG = {
    'user': 'oracle_user',
    'password': 'oracle_password',
    'dsn': 'localhost:1521/ORCLPDB1'
}

# Target DB 접속 정보 설정 (MySQL / PostgreSQL)
TARGET_CONFIG = {
    'host': 'localhost',
    'port': 3306,  # PostgreSQL의 경우 5432
    'user': 'target_user',
    'password': 'target_password',
    'database': 'target_db'
}

# 마이그레이션 대상 테이블 목록
TARGET_TABLES = ['TABLE_A', 'TABLE_B', 'TABLE_C']
BATCH_SIZE = 10000  # 배치 처리 단위
```

---

## 💡 주의사항 (Notes)

1. **Oracle Instant Client**: 파이썬에서 `cx_Oracle` 사용 시 시스템 환경변수에 Oracle Instant Client 경로가 등록되어 있거나 `cx_Oracle.init_oracle_client()` 설정이 필요합니다.
2. **데이터 타입 매핑**:
   - Oracle `NUMBER` -> Target `INT` / `BIGINT` / `DECIMAL`
   - Oracle `DATE` / `TIMESTAMP` -> Target `DATETIME` / `TIMESTAMP`
   - Oracle `VARCHAR2` -> Target `VARCHAR`
3. **대용량 데이터 처리**: 대용량 테이블의 경우 메모리 부족(OOM) 방지를 위해 `FETCHSIZE` 및 `BATCH_SIZE` 설정을 적절히 조정하여 분할 이관할 것을 권장합니다.
