drop table if exists entries;
create table entries(
  id integer primary key autoincrement,
  user text not null,
  score integer not null,
  last_post time not null
);

drop table if exists alerts;
create table alerts(
  id integer primary key autoincrement,
   text not null,
   sent_to text not null,
   last_alert time not null
);
