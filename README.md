# BigData-training

|Organisme | Formateur     |
| ---      | :---: |
| PLB Consultant  | Alaoui Mohamed |

Hand's on for BigData training

Cette partie sera principalement basé sur hortonworks

# Telechargement du Bac à Sable

**Une becanne avec 8 gig de RAM minimum**

**Attention, l'image fait presque 10 gig**

Clicker sur : [Sandbox](https://fr.hortonworks.com/downloads/#sandbox)

Guide : [Install](https://fr.hortonworks.com/tutorial/sandbox-deployment-and-install-guide/)

Demarrer la VM

# Tutorial

Le guide des tutoriaux est basé sur le site de Hortonworks.
Vous trouverez ci-dessus des points pour faciliter l'avancer des TPs

## 1. [Manipulation de la sandbox](https://fr.hortonworks.com/tutorial/learning-the-ropes-of-the-hortonworks-sandbox/)

- Veuillez travailler dans un dossier sous :
workspace/training/BigData/HDP-SB/
- Changer le mot de passe root de la SB
- Si Ambari ne demarre pas veuillez en parler au formateur, une configuration de la VM est peut etre necessaire
- Fair un petit tour sur la platforme


## 2. [HDFS](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/2/)
- Load files in distributed file system
- Set all necessary permissions

## 3. [Hive](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/3/)
- Set execution engine to tez
- Charger des vues Hive et regarder les jobs...Qu'en pensez vous?
- Faire l'analyse des datas avec un pipeline de transformation hive : chaine de requete hive

## 4. [pig](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/4/)

## 5. [spark](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/5/)
- Use Zeppeline and shell to test spark

## 6. [Reporting](https://fr.hortonworks.com/tutorial/hadoop-tutorial-getting-started-with-hdp/section/6/)


## 7. Manipulation HDFS direct

Use case : 
- Naviguer dans la sandbox avec hadoop fs et retrouver les fichier sauvegrader à partir de Ambari
- Sauvegarder un fichier de quelque meg dans HDS (fichier leonardo.txt)

## 8. Apache spark Zeppeline
- Use Zeppeline for wc distributed computing

## 9. Big data et Machine Learning
- Regression with spark

docker run --name cassandra1 -m 2g -d cassandra:3.0.4 

docker ps

docker logs cassandra1

docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra1

docker run -it --link cassandra1 --rm cassandra:3.0.4 sh -c 'exec cqlsh 172.17.0.2'

docker run --name cassandra2 -m 2g -d -e CASSANDRA_SEEDS="$(docker inspect --format='{{.NetworkSettings.IPAddress }}' cassandra1)" cassandra:3.0.4

docker exec -i -t cassandra1 sh -c 'nodetool status'


Code cql :

CREATE KEYSPACE demo WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE demo;
SELECT * FROM system.schema_keyspaces;
ALTER KEYSPACE demo WITH strategy_class=SimpleStrategy AND strategy_options:replication_factor=2;
DROP KEYSPACE demo;

CREATE TABLE Persons (
  familyName varchar, 
  firstName varchar, 
  age int, 
  address varchar,
  PRIMARY KEY(familyName));

SELECT columnfamily_name FROM schema_columnfamilies WHERE keyspace_name = 'demo';

ELECT column_name FROM schema_columns WHERE keyspace_name = 'cassandrademocql' and columnfamily_name = 'persons';

ALTER TABLE Persons ADD phone VARCHAR;

DROP COLUMNFAMILY Persons;

USE cassandrademocql;
INSERT INTO Persons (familyName, firstName, age, address,phone) VALUES ('BARON', 'Mickael', 36, 'Poitiers', '+33549498073');


SELECT * FROM cassandrademocql.Persons;

UPDATE cassandrademocql.persons SET firstname = 'Keulkeul' WHERE familyname = 'BARON';

DELETE FROM Persons WHERE familyname='BARON';

nodetool -h localhost -p 7199 status

nodetool -h localhost -p 7199 cfstats

nodetool -h localhost -p 7199 info

















