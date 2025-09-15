-- 🟩 Core Clauses
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT        -- or TOP (SQL Server)
OFFSET
DISTINCT

-- 🟦 Join Types
JOIN             -- or INNER JOIN
LEFT JOIN        -- or LEFT OUTER JOIN
RIGHT JOIN       -- or RIGHT OUTER JOIN
FULL JOIN        -- or FULL OUTER JOIN
CROSS JOIN
SELF JOIN
NATURAL JOIN

-- 🟨 Operators & Conditions
=, !=, <>, <, >, <=, >=
IN
NOT IN
BETWEEN
LIKE
NOT LIKE
IS NULL
IS NOT NULL
AND
OR
NOT
EXISTS
NOT EXISTS
CASE WHEN THEN ELSE END

-- 🟧 Subqueries & Set Operations
EXISTS
IN (subquery)
ANY, ALL, SOME
UNION
UNION ALL
INTERSECT
EXCEPT         -- or MINUS in Oracle

-- 🟫 DDL (Data Definition Language)
CREATE DATABASE
CREATE TABLE
CREATE INDEX
CREATE VIEW
ALTER TABLE
DROP TABLE
DROP DATABASE
DROP INDEX
TRUNCATE TABLE

-- 🟥 DML (Data Manipulation Language)
INSERT INTO
VALUES
UPDATE
SET
DELETE FROM

-- ⬛ Transaction Control
BEGIN
COMMIT
ROLLBACK
SAVEPOINT
SET TRANSACTION

-- ⬜ Other Keywords & Clauses
AS                 -- alias
WITH               -- CTE (Common Table Expression)
DEFAULT
AUTO_INCREMENT     -- MySQL
IDENTITY           -- SQL Server
CHECK
PRIMARY KEY
FOREIGN KEY
REFERENCES
INDEX
VIEW
CAST()
CONVERT()
PARTITION BY       -- for window functions
OVER()             -- used with RANK, ROW_NUMBER, etc.
RANK()
ROW_NUMBER()
DENSE_RANK()
