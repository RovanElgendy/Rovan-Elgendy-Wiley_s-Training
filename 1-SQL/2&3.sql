CREATE USER rovantest@localhost IDENTIFIED BY 'rovan';
grant all on *.* to rovantest@localhost;
GRANT SELECT, INSERT, UPDATE ON *.* TO rovantest@localhost;
show grants for rovantest@localhost;
select user,host,account_locked,password_expired from mysql.user;
select user,host,db,command from information_schema.processlist;
select user();   #returns the username and hostname of the currently logged-in user
use mysql;
SELECT User, Host FROM mysql.user;
SHOW CREATE USER rovantest@localhost;
DROP USER rovan@localhost;
UPDATE mysql.user SET Password=PASSWORD('rovan') WHERE User='rovantest';  # to change the password of user,works with old version of sql
SET PASSWORD FOR rovantest@localhost = PASSWORD('rovan');   # works with old versions of sql
ALTER USER rovantest@localhost IDENTIFIED WITH caching_sha2_password BY 'rovan'; # works in MySQL new version from 8.0 or later
ALTER USER rovantest@localhost IDENTIFIED BY 'rovan';       # a way to change the pw
FLUSH PRIVILEGES;       # to make sure the password or any privilege is updated  and executed immediately in MySQL server


use rovan;
# how to change the engine of a table if the SELECT statement is running slow because of many data on the table

create table vehicle(
vehicle_no varchar(20) primary key,
model_name varchar(45),
price decimal(10,2),
sell_price decimal(10,2));



insert into vehicle(vehicle_no,model_name,price,sell_price)
values('ssajd314231','mercedes',276473,18797),
('ssajd3142328438','mercedes1',47647,48797),
('ssajd31423341','mercedes2',67647,98797);

select  * from vehicle;

select table_name,engine from information_schema.tables; #Retrieves the name of the tables and its current storage engine in the database used

select table_name,engine from information_schema.tables
where table_name='vehicle';
repair table vehicle;          # to repair the engine of this table

alter table vehicle ENGINE='MyISAM';

repair table vehicle quick extended;         # to repair this table and all the table related to it
show engines;
describe table vehicle;

# to get it back to InnoDB Engine
select table_name,engine from information_schema.tables
where table_name='vehicle';
repair table vehicle;          # to repair the engine of this table

alter table vehicle ENGINE='InnoDB';
repair table vehicle quick extended; 
show table status;             # it shows all the status for each table in the database including which ENGINE 


# how to add a column after a specific column in a table 
alter table vehicle add column description varchar(200) not null after vehicle_no;
alter table vehicle add column Vehicle_color varchar(200) not null first;

# to change the default value for a column

alter table vehicle alter description set default 'car is superb';
describe vehicle;   

 

# change the data type and before that we should do the ' show table ' command line to know what is the data type for this column
alter table vehicle modify car_description varchar(20) default 'car is superb';  
alter table vehicle modify description varchar(20);                       # this will delete the default set earlier ' car is superb' ot be 'null'
show columns from vehicle;            # to show the column name,type,null,key,default,extra  = describe vehicle;
describe vehicle;                     # to show the column name,type,null,key,default,extra 
show full columns from vehicle;      # it shows the col.name,type,collation,null,key,default,extra,privileges


# show the columns starts with ..
show columns from vehicle like 'v%';    
show columns from vehicle like '%i%';
show columns from student like '%_i%';
show COLUMNS FROM VEHICLE LIKE '%d' or 'v%';              # doesn't work
show full columns from vehicle like '_e%';         # _ is used as a wild character instead of %

# showing the autoincrement keys in extra table 
describe student;                  # as this table has an auto-increment key so it shows in the Extra table 'auto-increment'

# to show the collation for each column



# to rename a column name only
alter table vehicle rename column description to car_description;

#to change the name of the column and also the data type of it
show columns from vehicle;  # to check the data type of this column to be changed
alter table vehicle change column car_description description varchar(200);

# to rename more than one column at one command line
alter table vehicle rename column description to car_description,rename column vehicle_color to color;

# create view statement to avoid running the same command line multiple times; create view caches the data in the memory only but the table is not saved in the database
create view mercedescar as select vehicle_no,price from vehicle where model_name='mercedes';
select * from mercedescar;

# to lock the table from any update
lock table vehicle read;
describe vehicle;
show full columns from vehicle;       # it shows the privilege that we can write the statements but it cant be executed
unlock tables;
lock table vehicle write;


# to check the status of your connection; useful to know which user is clogging up the connection to others
select connection_id();
# you may know the user from this command
use rovan;
select user,host,db,command from information_schema.processlist;

