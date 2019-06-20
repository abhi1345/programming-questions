# Write your MySQL query statement below
Select Email from 
(
Select email, Count(Id) as count
From Person
Group By email 
) as tab
Where Count > 1;
