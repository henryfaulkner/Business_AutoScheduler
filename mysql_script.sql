CREATE SCHEMA IF NOT EXISTS scheduler;
use scheduler;

CREATE TABLE manager (business varchar(40), name varchar(25), phone_number int(10), email varchar(40), pass varchar(25), primary key(email));
CREATE TABLE employee (business varchar(40), name varchar(25), phone_number int(10), email varchar(40), pass varchar(25), primary key(email));