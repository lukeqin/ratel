#drop database RATEL
DROP DATABASE IF EXISTS `RATEL`; 

#create RATEL database
create database RATEL character set utf8 collate utf8_general_ci;

#use database RATEL
use RATEL;

#create r_user table 
create table r_user(
	ID int(4) not null AUTO_INCREMENT, 
	NAME char(16) not null,
	PASSWORD char(255) not null,
	isADMIN tinyint(2) not null default '0',
	isLOCK tinyint(2) not null default '0', 
	DEPT varchar(16) default null,
	LOGINT char(24) default null,
	primary key(id),
	KEY index_name(name)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

#create r_group table
	create table r_group(
	ID int(4) not null AUTO_INCREMENT, 
	NAME char(16) not null,
	DEPT varchar(16) default null,
	INUSERS char(255) default null,
	primary key(id),
	KEY index_name(name)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

#create r_host table
create table r_host(
	ID int(4) not null AUTO_INCREMENT, 
	NAME char(16) not null,
	IP int(4) not null,
	OS char(16) not null,
	CPU char(16) not null,
	MEM char(16) not null,
	STATUS char(16) not null,
	primary key(id),
	KEY index_name(name)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

insert into r_user(name,password,dept) values("admin","$5$rounds=535000$xHiZVFqmIYpecTH.$NI5v4yhDY70SCgmGsVSZ3hy9b4ePhvY/WUK47zbuYSD","admin");