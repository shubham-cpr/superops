/*
            SQL stands for Structured Query Language.
            Databases that use sql are: 
                SQL server 
                Mysql 
                Postgresql 
                Oracle 
                SQLite 
*/
---- CREATE
create database customer 
create database <database-name> 

---- USE 
use customer 
use <database-name> 

---- CREATE TABLE
create table customer_table  
( 
    FirstName varcha(50), 
    LastName varchar(50), 
    Age int 
) 

create table customer_table  
( 
    [First Name] varcha(50),  - To keep space between column names, use []
    [Last Name] varchar(50),  - To keep space between column names, use []
    Age int 
) 

create table <table-name>  
( 
    <column-name>  <type>, 
    <column-name>  <type> 
) 

---- INSERT
insert into customer_table (FirstName,LastName,Age)
values ('Shubham','Kumar',27);

insert into customer_table ([First Name],[Last Name],Age)
values  ('Shubham','Kumar',21),
        ('Anjali', 'Sharma', 31),
        ('Rahul', 'Verma', 25),
        ('Priya', 'Singh', 29),
        ('Aman', 'Jain', 35),
        ('Neha', 'Gupta', 24),
        ('Vikram', 'Rao', 40),
        ('Sneha', 'Mehta', 28),
        ('Rohit', 'Kapoor', 32),
        ('Kiran', 'Patel', 30);


---- SELECT
select * from customer_table                                -- To get everything inside table use "*"
select [First Name],[Last Name] from customer_table         -- To get particular coulmns, mention column names

---- WHERE
select [First Name],[Last Name] from customer_table where [Last Name]='Kumar'       -- Filter using fixed values inside columns
select [First Name],[Last Name] from customer_table where Age=30

select [First Name],[Last Name] from customer_table where [Last Name] like 'Kum%'   -- use 'LIKE' clause to get all values thorugh wildcard(%)
select [First Name],[Last Name] from customer_table where [First Name]='Shubham' and [Last Name]='Kumar'  -- use 'AND' clause for filtering with multiple values
select [First Name],[Last Name] from customer_table where [First Name]='Shubham' and [Last Name] like 'kum%'
select [First Name],[Last Name] from customer_table where Age>=25

---- UPDATE
update <table-name>
set <column-name>=<value>
where <put you where clause>;   -- make sure to use 'WHERE' clause while updating or deleting, otherwise the action will be performed on all rows

update customer_table
set age=30
where [First Name]='Shubham' and [Last Name]='Kumar';

update customer_table
set age=30
where [First Name] like 'sh%' and [Last Name]='Kumar';

---- DELETE
delete customer_table
delete <table-name>     -- This delete all the rows in table and not the table itself.

delete customer_table
where [Last Name]='Kumar';

delete customer_table
where [First Name] like 'sh%' and [Last Name]='Kumar';

---- ALTER
alter table customer_table
add City varchar(50),
    Country varchar(50)

update customer_table
set City='Hyderabad',
    Country='India'

---- DROP
drop table shubh_table_1

---- PRIMARY KEY
alter table customer_table
add Id int PRIMARY KEY IDENTITY (1,1);

---- CREATE another tables
create table products_table
(
    ProductId int PRIMARY KEY IDENTITY (0001,1),
    ProductName varchar(50),
    Price float
)
insert into products_table
(ProductName,Price)
values ('Bat',15000),
        ('Boxing Gloves',2500),
        ('Ball',400),
        ('Football',2800);

---- FOREIGN KEY
alter table orders_table
add foreign key (CustomerId) REFERENCES customer_table(CustomerId)
/*
A foreign key in SQL is a column (or a group of columns) used to establish a relationship between two tables. 
It enforces referential integrity, meaning it ensures that the value in one table corresponds to a valid record in another table.

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

*/
---- JOINS
/*
In SQL, joins are used to combine rows from two or more tables based on a related column between them—typically a foreign key relationship. 
This is essential for querying relational data spread across multiple tables.
Types of Joins:-
    INNER JOIN: Returns only the rows with matching values in both tables.
        SELECT Orders.OrderID, Customers.Name
        FROM Orders
        INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
    LEFT JOIN: Returns all rows from the left table, and matched rows from the right table. If no match, returns NULLs from the right.
        SELECT Customers.Name, Orders.OrderID
        FROM Customers
        LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
    RIGHT JOIN: Returns all rows from the right table and matched rows from the left table.
        SELECT Orders.OrderID, Customers.Name
        FROM Orders
        RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
    FULL JOIN: Returns all rows when there is a match in either left or right table. NULLs are used when there is no match.
        SELECT Customers.Name, Orders.OrderID
        FROM Customers
        FULL OUTER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
*/

select * from customer_table
inner join orders_table on orders_table.CustomerId=customer_table.Id

select * from orders_table
inner join products_table on orders_table.ProductId=products_table.ProductId
inner join customer_table on orders_table.CustomerId=customer_table.Id

select orders_table.OrderId, products_table.ProductName,products_table.Price,customer_table.[First Name],customer_table.[Last Name] from orders_table
inner join products_table on orders_table.ProductId=products_table.ProductId
inner join customer_table on orders_table.CustomerId=customer_table.Id

select orders_table.OrderId,orders_table.ProductId, products_table.ProductName,products_table.Price,customer_table.[First Name],customer_table.[Last Name] from customer_table
inner join orders_table on orders_table.CustomerId=customer_table.Id
inner join products_table on orders_table.ProductId=products_table.ProductId

--Create table Customer
CREATE TABLE Customer
(
	[CustomerId] [int] NOT NULL,
	[CityId] [int] NULL,
	[CustomerName] [varchar](50) NOT NULL
) ON [PRIMARY]

--Insert Customer Records
INSERT [dbo].[Customer] ([CustomerId], [CityId], [CustomerName]) 
VALUES (1, 1, N'Bob Smith'),
(2, 1, N'Sally Smith'),
(3, 2, N'Tom Smith'),
(4, NULL, N'Mary Smith')

--Create table City
CREATE TABLE City
(
	[CityId] [int] NOT NULL,
	[CityName] [varchar](50) NOT NULL
) ON [PRIMARY]

--Insert City Records
INSERT [dbo].[City] ([CityId], [CityName]) VALUES (1, N'Kansas City'),
(2, N'New York'),
(3, N'Houston')

select * from Customer inner join City on Customer.CityId=City.CityId

select * from Customer left join City on Customer.CityId=City.CityId

select * from Customer right join City on Customer.CityId=City.CityId

select * from Customer full join City on Customer.CityId=City.CityId

---- FUNCTIONS and GROUP BY
/*
Functions are built-in operations that perform calculations, manipulate data, or return system information. 
They're generally divided into the following categories:
    Aggregate Functions:-
        COUNT(*)	                Number of rows
        SUM(column)	                Sum of values
        AVG(column)	                Average of values
        MIN(column)	                Smallest value
        MAX(column)	                Largest value
    String Functions:-
        LEN(string)	                        Length of a string
        UPPER(string)	                    Convert to uppercase
        LOWER(string)	                    Convert to lowercase
        SUBSTRING(str, start, length)		Extract substring
        REPLACE(str, old, new)	Replace 	substring
        LTRIM(string) / RTRIM(string)		Trim spaces from left/right
        CONCAT(str1, str2, ...)				Combine strings
    Date/Time Functions:-
        GETDATE()							Current date and time
        CURRENT_TIMESTAMP					Same as GETDATE()
        DATEADD(unit, value, date)			Add interval to date
        DATEDIFF(unit, start, end)			Difference between two dates
        DATEPART(unit, date)				Extract part (e.g. year, month, day)
        FORMAT(date, format)				Format date output (SQL Server)
    Numeric Functions
        ABS(number)							Absolute value
        ROUND(num, decimals)				Round to n decimals
        CEILING(number)						Smallest integer ≥ number
        FLOOR(number)						Largest integer ≤ number
        POWER(x, y)							x to the power of y
        RAND()								Random float between 0 and 1
    Logical & System Functions
        ISNULL(expr, replacement)				Replace NULL with a value
        COALESCE(val1, val2, ...)				First non-null value
        CASE WHEN ... THEN ... ELSE ... END		Conditional logic
        NULLIF(val1, val2)						NULL if values are equal
        SCOPE_IDENTITY()						Last inserted identity in scope
*/

select sum(products_table.Price) as Total,products_table.ProductName,customer_table.[First Name] from orders_table
inner join products_table on orders_table.ProductId=products_table.ProductId
inner join customer_table on orders_table.CustomerId=customer_table.Id
group by products_table.ProductName,customer_table.[First Name]

