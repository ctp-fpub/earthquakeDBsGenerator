-- mysql --local-infile=1 -u prod -p

USE cutremure;

DROP TABLE romplus;

CREATE TABLE romplus (
    dateandtime DATETIME,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    depth DOUBLE PRECISION,
    magnitude DOUBLE PRECISION,
);

LOAD DATA LOCAL infile "romplus.csv" INTO TABLE italy COLUMNS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;