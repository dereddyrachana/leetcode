# Write your MySQL query statement below
select c.name as Customers
from Customers c
where c.id not in (
           select c.id
from Customers c, Orders O
where c.id = o.customerId )
