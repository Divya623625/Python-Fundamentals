CREATE DATABASE College;
USE college;

CREATE TABLE student(
	roll_no INT,
    name VARCHAR(30),
	age int
);

INSERT INTO student
VALUES
(101, "Adam", 12),
(102, "Bob", 15);

SELECT * FROM student;

