DELETE FROM Person WHERE id NOT IN (
    SELECT A.id FROM
    (SELECT MIN(id)AS id FROM Person GROUP BY Email) as A);
