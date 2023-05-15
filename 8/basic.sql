-- create table query 
create table newtable(eno number(10),
                      name varchar(10),
                      age number(2),
                      Region char(10),
                      salary number(7,2),
                      constratins pk_eno primary key(eno));

-- inserting values
insert into newtable(1,'om',18,"india",100000.00,);
insert into newtable(2,'jay',28,"india",500000.00,);
insert into newtable(3,'ajay',18,"india",100000.00,);

-- viewing value
select * from newtable

-- deleting table
drop column newtable.age;
drop table newtable

--updating table
update table newtable set eno=11 where name='om';
