create database cw_project;
use cw_project;


-- Q: Find the top 10 richest billionaires.-- 
SELECT personName, finalWorth, country, industries
FROM cleaned_billionaires
ORDER BY finalWorth DESC
LIMIT 10;


-- Q: What is the average net worth by country?
SELECT country, AVG(finalWorth) AS avgWorth
FROM cleaned_billionaires
GROUP BY country
ORDER BY avgWorth DESC;


-- Q: How many billionaires are in each industry?
SELECT industries, COUNT(*) AS count
FROM cleaned_billionaires
GROUP BY industries
ORDER BY count DESC;


-- Q: Compare education enrollment vs GDP
SELECT country, gross_tertiary_education_enrollment, gdp_country
FROM cleaned_billionaires
WHERE gross_tertiary_education_enrollment IS NOT NULL
  AND gdp_country IS NOT NULL;
  
  
-- Q: Average final worth based on education enrollment per country
SELECT country, AVG(finalWorth) AS avgWorth, AVG(gross_tertiary_education_enrollment) AS avgEnrollment
FROM cleaned_billionaires
GROUP BY country
HAVING AVG(gross_tertiary_education_enrollment) IS NOT NULL;


-- Q: Top 3 Billionaires by Industry
SELECT personName, industries, finalWorth,
       RANK() OVER (PARTITION BY industries ORDER BY finalWorth DESC) AS rank_in_industry
FROM cleaned_billionaires
WHERE industries IS NOT NULL;


-- Q: Self-Made % by Country
SELECT country,
       ROUND(100.0 * SUM(CASE WHEN selfMade = 'True' THEN 1 ELSE 0 END) / COUNT(*), 2) AS self_made_percentage
FROM cleaned_billionaires
GROUP BY country
HAVING COUNT(*) > 5
ORDER BY self_made_percentage DESC;


-- Q: Wealth Category Tags
SELECT personName, finalWorth,
       CASE
           WHEN finalWorth >= 50000 THEN 'Ultra Rich'
           WHEN finalWorth >= 10000 THEN 'Super Rich'
           WHEN finalWorth >= 1000 THEN 'Rich'
           ELSE 'Millionaire'
       END AS wealth_category
FROM cleaned_billionaires;














