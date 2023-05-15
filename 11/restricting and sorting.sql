-- using where clause --
select eno , name , salary , region from newtable where eno = 1;

-- character string --
select eno , name , salary , region from newtable where name = "om";

-- using comparison Condition --
select eno , name , salary , region from newtable where eno > 1 and salary < 50000;

-- between condition --
select eno , name , salary , region from newtable where eno between 1 and 3 and salary > 50000;

-- using In condition --
select eno , name , salary , region from newtable where eno in (1,2,3);

-- using Like condition --
select eno , name , salary , region from newtable where name like "o%";

-- using Like condition with escape character --
select eno , name , salary , region from newtable where name like "_o%" escape "_";

-- using Null conditon -- 
select eno , name , salary , region from newtable where salary is null;

-- using order by clause -- 
select eno , name , salary , region from newtable order by eno desc;

-- sorting by Column Alias -- 
select eno , name , salary*12 annual , region from newtable order by eno desc, annual asc;