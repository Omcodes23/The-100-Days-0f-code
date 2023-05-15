-- inserting values
insert into newtable(1,'om',1000,'newyork');

-- updating value
update table set eno=12 where name='om';

--deleting values
delete from newtable where eno=12;

-- creating a script
insert into newtable(eno,name,salary,region)
values (&eno,&name,&salary,&region);

--merge statenebt
merge into newtable as nt
using second_newtable as snt
when matched then
update set nt.eno = snt.eno,
           nt.name = snt.name,
           nt.salary = snt.salary,
           nt.region = snt.region
when not matched then
insert values(snt.eno,snt.name,snt.salary,snt.region);