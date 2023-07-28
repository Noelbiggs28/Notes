-- create table
DROP TABLE IF EXISTS activities;
CREATE TABLE activities (
  id           serial PRIMARY KEY,
  football      varchar(255) NOT NULL,
  journalism      varchar(255) NOT NULL,
  debate_team     varchar(255) NOT NULL
);

-- insert into
INSERT INTO activities (id, football, journalism, debate_team) 
VALUES (1, 'yes', 'no', 'yes');

-- add column
ALTER table students
ADD Column activities int;

-- update table
UPDATE students
SET activities = id
Where id != 0
;

-- includes name
select * from cd.facilities where name like '%Tennis%';

-- make new column with values inserted per case
select name,  
case 
	when monthlymaintenance > 100 then 'expensive'
	else 'cheap'
end as cost
from cd.facilities ;

-- extracting datetime info
select memid,surname,firstname,joindate 
from cd.members 
where extract(month from joindate) >=9 
and extract(year from joindate) >= 2012;

-- ordering,limiting,distint
select distinct(surname) from cd.members order by surname asc limit 10;

-- combine to columns to one
select surname from cd.members 
union
select name from cd.facilities

-- joining tables
select starttime from bookings
join members on bookings.memid = members.memid
where firstname = 'David'
And surname = 'Farrell';

-- working with times
select cd.bookings.starttime as start, cd.facilities.name as name 
from cd.bookings join cd.facilities on cd.facilities.facid = cd.bookings.facid
where cd.bookings.starttime >= '2012-09-21'
and cd.bookings.starttime < '2012-09-22'
and name like 'Tennis Court%'
order by start asc;

-- join a table with itself
select distinct originals.firstname,originals.surname from cd.members as originals
join cd.members as joiners on joiners.recommendedby = originals.memid 
order by surname
;

-- make it equal to two things
select * from numbers where number in (1,5);

-- left outer join. double order by
select originals.firstname, originals.surname, joiners.firstname, joiners.surname 
from cd.members as originals
left outer join cd.members as joiners 
on joiners.memid = originals.recommendedby 
order by originals.surname, originals.firstname
;