drop table if exists users CASCADE;
create table users (
  uid SERIAL PRIMARY KEY,
  name text
);