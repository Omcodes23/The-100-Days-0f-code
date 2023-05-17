-- defining constaints --
create table employees(
                        employee_id number(6),
                        first_name varchar(20),
                        job_id varchar2(10) not null,
                        constaint emp_emp_id_pk primary key (employee_id)
);

-- unique constaint --
create table employees(
                        employee_id number(6),
                        last_name varchar2(25) not null,
                        email varchar2(25),
                        salary number(8,2),
                        commission_pct number(2,2),
                        hire_date date not null,
                        constaint emp_emial_uk unique(email)
);

-- primary key --
create table departments(
                            department_id number(4),
                            depart_name varchar2(30) constraint dept_name not null,
                            manager_id number(6),
                            location_id number(4),
                            constaint dept_id primary key (department_id)
);

-- foregin key --
create table employees(
                        employee_id number(6),
                        last_name varchar(25) not null , 
                        emial varchar2(25),
                        salary number(8,2),
                        commission pct number(2,2),
                        hire_date date not null,
                        department_id number(4),
                        constraint emp_dept_fk foreign key (department_id) feference departments(department_id),
                        constarint emp_emial_uk unique(email) 
);

-- check -- 
craete table employees(
    salary number(8,2) constraint emp_salary_min check (salary > 0)
);

-- adding constraint --
alter table employeesadd constaintemp_manager_fk 
    foreign key(manager_id) erference employees(employee_id);

-- Droppling constraints --
alter table employees
drop constraints emp_manager_fk; 

-- Disabling Constriants --
Alter table employees Disable constaintemp_emp_id_pk cascade;

-- Enabling constraints --
alter table employees enable constraint emp_emp_id_pk;

-- cascading constraints --
alter table test1
Drop (pk) cascade constraint;

alter table test1 
drop (ok , fk , col1) cascade Constriants;

-- viewing constraints --
select constrant_name , constraint_type , search_condition
from user_constraints
where table_name = 'Employees';

-- viewing the column associated with constraints --
select constraint_name , column_name 
from user_cons_columns
where table_name = 'Employees';