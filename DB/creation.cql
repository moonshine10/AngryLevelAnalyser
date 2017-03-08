CREATE KEYSPACE IF NOT EXISTS Tracker with REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE Tracker;

CREATE TABLE Tweets (
id_str text PRIMARY KEY,
text text,
created_at text,
geo text);

create index on Tweets (created_at);

CREATE TABLE AL (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE AK (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE AZ (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE AR (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE CA (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE CO (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE CT (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE DE (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE FL (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE GA (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE HI (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE ID (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE IL (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE IND (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE IA (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE KS (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE KY (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE LA (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE ME (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE MD (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE MA (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE MI (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE MN (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE MS (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE MO (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE MT (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE NE (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE NV (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE NH (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE NJ (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE NM (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE NY (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE NC (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE ND (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE OH (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE OK (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE ORE (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE PA (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE RI (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE SC (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE SD (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE TN (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE TX (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE UT (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE VT (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE VA (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE WA (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE WV (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE WI (
tID text PRIMARY KEY,
date int,
sentiment decimal);

CREATE TABLE WY (
tID text PRIMARY KEY,
date int,
sentiment decimal);

