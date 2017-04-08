drop table if exists teams; 
drop table if exists individuals;

create table teams (
	id integer primary key autoincrement, 
	team text not null, 
	size integer
); 

create table individuals (
	id integer primary key autoincrement, 
	team text not null,
	mentor text, 
	project text, 
	major text, 
	technology blob,
	year text, 
	hometown text, 
	race text, 
	languages text, 
	gender text, 
	hobbies blob, 
	coded integer, 
	prog_langs blob, 
	spot text, 
	role_model text, 
	pineapple id, 
	coffee_order blob
);