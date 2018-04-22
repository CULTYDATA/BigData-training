
Install ;

docker run -p 9042:9042 --name cassandra1 -m 2g -d cassandra:latest 

docker ps

docker logs cassandra1

docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra1

docker run -it --link cassandra1 --rm cassandra:latest sh -c 'exec cqlsh ip'

docker run -p 9043:9042 --name cassandra2 -m 2g -d -e CASSANDRA_SEEDS="$(docker inspect --format='{{.NetworkSettings.IPAddress }}' cassandra1)" cassandra:latest

docker run -p 9044:9042 --name cassandra3 -m 2g -d -e CASSANDRA_SEEDS="$(docker inspect --format='{{.NetworkSettings.IPAddress }}' cassandra2)" cassandra:latest
docker exec -i -t cassandra1 sh -c 'nodetool status'





Code cql :

CREATE KEYSPACE demo WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };
USE demo;

DROP KEYSPACE demo;

CREATE TABLE Persons (
  id uuid,  
  familyName varchar, 
  firstName varchar, 
  age int, 
  address varchar,
  phone varchar,
  PRIMARY KEY(id,familyName));




  DESC ... ;

ALTER TABLE Persons ADD phone VARCHAR;

DROP COLUMNFAMILY Persons;

USE demo;
INSERT INTO Persons (familyName, firstName, age, address,phone) VALUES ('BARON', 'Mickael', 36, 'Poitiers', '+33549498073');

SELECT * FROM demo.Persons;

UPDATE demo.persons SET firstname = 'xxxx' WHERE familyname = 'yyyyy';
