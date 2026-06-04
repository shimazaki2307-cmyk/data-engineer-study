create table people (
    name TEXT,
    age INTEGER
    );

INSERT INTO people VALUES ('Akira',25);
INSERT INTO people VALUES ('Yamada',30);
INSERT INTO people VALUES ('Suzuki',28);

SELECT *
FROM people;

SELECT *
FROM people
WHERE age >= 30;
