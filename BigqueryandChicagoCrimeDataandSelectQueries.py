## Working with SELECT, FROM, ORDER BY, GROUP BY, HAVING, DISTINCT in bigquery
## dataset is chicago_crime

SELECT *
FROM `bigquery-public-data`.chicago_crime.crime;

-- simple select
SELECT
  primary_type, district
FROM
  `bigquery-public-data`.chicago_crime.crime
LIMIT 5;

-- Aliasing column names
SELECT
  primary_type, district AS district_of_crime
FROM
  `bigquery-public-data`.chicago_crime.crime
LIMIT 5;


SELECT
  primary_type,description,year,district,
FROM
  `bigquery-public-data`.chicago_crime.crime
LIMIT 5;

SELECT
  primary_type,description,year,district,
FROM
  `bigquery-public-data`.chicago_crime.crime
LIMIT 10;

SELECT
  primary_type,description,year,district
FROM
  `bigquery-public-data`.chicago_crime.crime
WHERE year >= 2014 AND year < 2016 AND primary_type = 'DECEPTIVE PRACTICE'
LIMIT 5;

SELECT
  *
FROM
  `bigquery-public-data`.chicago_crime.crime
WHERE primary_type LIKE '%PRACTICE%';

SELECT
  * EXCEPT(unique_key, updated_on)
FROM
  `bigquery-public-data`.chicago_crime.crime
WHERE primary_type LIKE '%PRACTICE%';

WITH all_crimes AS (
  SELECT
     primary_type,description,year,district
   FROM
     `bigquery-public-data`.chicago_crime.crime
)
SELECT * from all_crimes
WHERE year < 2015
LIMIT 10;

SELECT
  primary_type,description,year,district,
FROM
  `bigquery-public-data`.chicago_crime.crime
order by year desc
LIMIT 10;

SELECT
  primary_type, count(arrest) as cnt_arrest
FROM
  `bigquery-public-data`.chicago_crime.crime
WHERE location IS NOT NULL and year>2016
GROUP BY
  primary_type
HAVING cnt_arrest > 100
ORDER BY
  cnt_arrest desc;


SELECT
  DISTINCT primary_type
FROM
  `bigquery-public-data`.chicago_crime.crime;

  WITH robbery AS (
  SELECT primary_type , description
  FROM `bigquery-public-data`.chicago_crime.crime
  WHERE year=2020 and primary_type="ROBBERY"
)
SELECT primary_type, description
FROM robbery;