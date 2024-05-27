CREATE SCHEMA IF NOT EXISTS job_searcher;

CREATE TABLE IF NOT EXISTS job_searcher.profession
(
    id             SERIAL PRIMARY KEY,
    professionName VARCHAR(256),
    payrollFrom    INTEGER,
    payrollTo      INTEGER
);

CREATE TABLE IF NOT EXISTS job_searcher.users
(
    id          SERIAL PRIMARY KEY,
    firstName   VARCHAR(256) not null,
    lastName    VARCHAR(256) not null,
    patronymic  VARCHAR(256),
    age         INTEGER,
    email       VARCHAR(256) UNIQUE,
    phone       VARCHAR(256) UNIQUE,
    password    VARCHAR(256),
    dateOfBirth DATE,
    living      VARCHAR(256),
    profession_id INTEGER,
    FOREIGN KEY (profession_id) REFERENCES job_searcher.profession (id)
);
