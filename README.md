# Oracle to MySQL Migration Utilities

Oracle 데이터베이스에서 MySQL(및 PostgreSQL)로의 데이터 및 스키마 이관 작업을 체계적이고 효율적으로 수행하기 위한 마이그레이션 유틸리티 프로젝트입니다.

---

## 📋 목차
1. [프로젝트 개요](#-프로젝트-개요)
2. [마이그레이션 주요 흐름](#-마이그레이션-주요-흐름)
3. [프로젝트 폴더 구조](#-프로젝트-폴더-구조)
4. [선행 조건 및 환경 설정](#-선행-조건-및-환경-설정)
5. [사용 방법](#-사용-방법)
6. [주요 고려사항 및 트러블슈팅](#-주요-고려사항-및-트러블슈팅)

---

## 💡 프로젝트 개요
본 유틸리티는 Oracle DB 내의 스키마, 데이터 타입, 제약조건, 인덱스 및 테이블 데이터를 MySQL 표준 구조로 자동 변환 및 고속 이관(Bulk Insert)할 수 있도록 지원하는 스크립트 및 파이썬 모듈 모음입니다.

---

## 🔄 마이그레이션 주요 흐름

### 1. 정책 설정
* **계정 및 권한**: 보안 정책에 따른 DB 유저 생성 및 권한 차등 적용
* **데이터베이스 구조**: Oracle 스키마와 MySQL 데이터베이스 간 `1:1 매핑` 또는 `단일 데이터베이스 통합` 구현 방안 확정

### 2. 이관 물량 및 스펙 파악
* **대상 산정**: 이관 대상 테이블, 총 건수, 데이터 용량 파악
* **특수 칼럼 분석**: LOB(CLOB/BLOB) 칼럼, 함수 적용 칼럼 등 사전 확인
* **시퀀스 전략**: `AUTO_INCREMENT` 적용 또는 `시퀀스 전용 테이블` 생성 방식 결정
* **배치 파악**: Shell Script 내 존재하는 기존 배치 및 SQL 파악

### 3. Oracle 딕셔너리 기반 DDL 스크립트 추출
* Oracle Data Dictionary를 조회하여 MySQL 용 DDL 자동 추출
* **포함 요소**:
  * 테이블 DDL (Oracle $
ightarrow$ MySQL 데이터 타입 변환 규칙 반영)
  * 시퀀스 구조 변환 테이블 DDL
  * Primary Key, Foreign Key, Index, Default 제약조건
  * 테이블 및 칼럼 주석(Comment) 적용

### 4. MySQL DDL 적용
* 이관 전용 최적화 MySQL 파라미터(Session/Global) 적용
* DDL 실행 및 실패 물량 파악, 보완 작업 수행

### 5. Python 기반 데이터 고속 이관 (Bulk Insert)
* Python 스크립트를 통한 Oracle $
ightarrow$ MySQL Bulk Insert 수행
* **주요 작업 내용**:
  * 테이블별 소요시간 체크 (본 이행 작업 시간 예측)
  * 오류 발생 테이블 원인 분석, 데이터 정제 및 재실행
  * DB 서버 부하(CPU/IO/Network) 모니터링
  *(별도 이관 솔루션이 존재하는 경우 이를 보완/병행하여 활용 가능)*

### 6. 매뉴얼 마이그레이션 (기타 오브젝트)
* **대상**: Function, Stored Procedure, Job, Trigger 등
* Oracle과 MySQL 문법 매핑 정의서 작성 후 수동/반자동 변환 진행

### 7. 기타 고려사항
* **암호화 데이터**: 내부 DB 암호화 솔루션 활용 시 복호화 및 재암호화 전략 수립 필요
* **DBMS 제약 조건**: Row 당 최대 길이나 오브젝트 명칭 길이 제약 등으로 인한 표준 예외 발생 시 고객사 협의 필요
* **Shell 배치 구현**: 기존 Shell 스크립트 기반 배치 작업 재구현 및 검증

---

## 📁 프로젝트 폴더 구조

```text
MyUtils/
├── app/
│   ├── Mains/                             # 실행 메인 모듈
│   │   ├── MigOacleToMysqlMain.py         # Oracle -> MySQL 마이그레이션 메인 파이썬 스크립트
│   │   ├── MigOacleToPostgresqlMain.py    # Oracle -> PostgreSQL 마이그레이션 메인 파이썬 스크립트
│   │   ├── MigOracleToOtherDB.sql         # Oracle 스키마/타입 변환 및 DDL/DML 자동 생성 SQL
│   │   └── OracleTomysql DDL 스크립트/
│   │       ├── 01_mysql 테이블 생성.sql
│   │       ├── 02_mysql 제약조건 DDL 생성.sql
│   │       ├── 03_mysql 인덱스 DDL 생성.sql
│   │       └── 04_mysql 시퀀스 테이블 생성.sql
│   └── PyClass/                           # 공통 모듈 및 DB 조작 모듈
│       ├── MysqlClass.py                  # MySQL Connection & CRUD Wrapper
│       ├── OracleClass.py                 # Oracle Connection & CRUD Wrapper
│       ├── TimeClass.py                   # Execution Time Tracker
│       └── LoggerClass.py                 # System Logging Helper
```

---

## 🛠️ 선행 조건 및 환경 설정

### Requirements
* Python 3.8+
* Oracle Client Library (instantclient)
* Python Packages:
  ```bash
  pip install cx_Oracle PyMySQL mysql-connector-python
  ```

---

## 🚀 사용 방법

1. **Oracle 딕셔너리 기반 DDL 추출**
   `app/Mains/MigOracleToOtherDB.sql`을 Oracle DB에서 실행하여 MySQL용 DDL 생성

2. **MySQL DDL 적용**
   `app/Mains/OracleTomysql DDL 스크립트/` 내 순서대로 `.sql` 파일 실행:
   * `01_mysql 테이블 생성.sql`
   * `02_mysql 제약조건 DDL 생성.sql`
   * `03_mysql 인덱스 DDL 생성.sql`
   * `04_mysql 시퀀스 테이블 생성.sql`

3. **데이터 이관 실행 (Python Bulk Insert)**
   ```bash
   python app/Mains/MigOacleToMysqlMain.py
   ```

---

## 📌 주요 고려사항 및 트러블슈팅
* **LOB 데이터 처리**: 대용량 TEXT/BLOB 칼럼의 경우 Chunk 단위 읽기/쓰기 처리 권장
* **대용량 이관 시 성능 최적화**:
  * `SET FOREIGN_KEY_CHECKS = 0;`
  * `SET UNIQUE_CHECKS = 0;`
  * `SET AUTOCOMMIT = 0;` 후 커밋 주기 최적화
