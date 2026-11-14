CREATE TABLE mumbai_houses (
    bhk INT,
    type TEXT,
    locality TEXT,
    area NUMERIC,
    price NUMERIC,
    price_unit TEXT,
    region TEXT,
    status TEXT,
    age TEXT,
    price_in_lakh NUMERIC,
    price_per_sq_ft NUMERIC,
    check_flag TEXT
);

SELECT COUNT(*) FROM mumbai_houses;
SELECT * FROM mumbai_houses LIMIT 10;

SELECT region, AVG(price_per_sq_ft) As avg_price_per_sqft, COUNT (*) AS total_listings
FROM mumbai_houses
GROUP BY region
ORDER BY avg_price_per_sqft DESC;

SELECT region, AVG(price_per_sq_ft) As avg_price_per_sqft, COUNT (*) AS total_listings
FROM mumbai_houses
GROUP BY region
HAVING COUNT(*) >= 30
ORDER BY avg_price_per_sqft DESC;

SELECT bhk, AVG(price_per_sq_ft) AS avg_price_per_sqft, COUNT(*) AS total_listings
FROM mumbai_houses
GROUP BY bhk
ORDER BY bhk;

SELECT status, AVG(price_per_sq_ft) AS avg_price_per_sqft, COUNT(*) AS total_listings
FROM mumbai_houses
GROUP BY status;

SELECT age, AVG(price_per_sq_ft) AS avg_price_per_sqft, COUNT(*) AS total_listings
FROM mumbai_houses
GROUP BY age;

SELECT status, AVG(price_per_sq_ft) AS avg_price_per_sqft, COUNT(*) AS total_listings
FROM mumbai_houses
WHERE region = 'Andheri West'
GROUP BY status;

SELECT status, AVG(price_per_sq_ft) AS avg_price_per_sqft, COUNT(*) AS total_listings
FROM mumbai_houses
WHERE region = 'Thane West'
GROUP BY status;

SELECT type, AVG(price_per_sq_ft) AS avg_price_per_sqft, COUNT(*) AS total_listings
FROM mumbai_houses
GROUP BY type;