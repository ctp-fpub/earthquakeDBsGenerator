-- mysql --local-infile=1 -u prod -p

USE cutremure;

DROP TABLE california;

CREATE TABLE california (
    year INT,
    month INT,
    day INT,
    hour INT,
    minute INT,
    second DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    depth DOUBLE PRECISION,
    magnitude DOUBLE PRECISION,
    magtype CHAR(1)
);

LOAD DATA LOCAL infile "california.csv" INTO TABLE california COLUMNS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;