-- mysql --local-infile=1 -u prod -p

USE cutremure;

DROP TABLE italy;

CREATE TABLE italy (
    dateandtime DATETIME,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    depth DOUBLE PRECISION,
    magnitude DOUBLE PRECISION,
    magtype CHAR(1)
);

LOAD DATA LOCAL infile "japan.csv" INTO TABLE japan COLUMNS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;