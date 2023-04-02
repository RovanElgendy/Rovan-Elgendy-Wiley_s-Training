create database rovan;
use rovan;
show databases;
create table student (
id int,
username varchar(100));
SELECT * from student;  # key words can be used as capital or small letter
create table rovan(
id int,
age int,
college varchar(20));
select id from rovan;
create table information(
id int,
user_name varchar(10));
select * from rovan,information;
insert into student (id,username) values (55,'rovan');

insert into student (id) values (2); # it will insert the data into id only and the other is null because only one column is specified(id)
insert into student values (6); # it will give error because the data for the whole row must be inserted
insert into student values (6,'rov.'); # it will succeed because all the data is inserted in all the rows
update student set id=88 where username='rovan';  # it will give error because the safety mode is on,you can disable from edit-preferences-sql editor-disable it
show tables;  # it shows all the tables created in this database being used
select * from student;
delete from student where id=1;
update student set id=44,username='abdou' where username='noran';  # to update more than two values
select * from student;
alter table student           
rename column id to user_id;          # to rename a column
select * from student;
alter table student
rename column user_id to user_id,
rename column username to user_name;          # to rename a column
select * from student;
alter table student
modify column user_name varchar(20);  # to change the data type of column
describe student;   # it shows the column and its data type
create table student1 (
id int primary key,
username varchar(100));
insert into student1 values(4,'rovan'); # it gives error because id should be PK
select * from student1;
describe student1;
delete from student where user_id=2;
delete from student where user_id=88;
create table student3 (
id int,
username varchar(100));
alter table student3 add primary key (id); # to modify one column as primary key
select * from student3;
describe student3;
describe table student3;
insert into student3 (id,username) values (1,'rovan');
insert into student3 (id,username) values (1,'rovan'); # it will give error because the id(which is PK) value already exists
insert into student3 (id,username) values (2,'rovy');
insert into student3 (id,username) values (3,'rov.');
create table student4 (
id int primary key auto_increment,
username varchar(100));
insert into student4 (username) values ('rovan'),('rovy'),('rouv'); # it will add the PK automatically because it is auto increment
delete from student4 where id=2;
select * from student4;
insert into student4 values ('rovy'); #error
insert into student4 values (2,'rovy');
truncate table student3; # removes the data in the rows
drop table student3;  # removes the whole table
select max(user_id) from student; # to know the last value for the PK
insert into student4 (username) values ('rou');