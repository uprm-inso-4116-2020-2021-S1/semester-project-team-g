import psycopg2

DATABASE_URL = 'postgres://ewlsfolgbjbyin' \
               ':34f17fc6c2d3dbc65842162b549486f6764c9c1462317f5607bd36f93c8d3986' \
               '@ec2-34-235-62-201.compute-1.amazonaws.com' \
               ':5432' \
               '/d662524kgh9iqj'


# user (without "postgres://"),
# password (without ":"),
# host (without "@"),
# port (without ";"),
# DB name (without "/")


class DBManager:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')
            cursor = self.connection.cursor()
            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL database in heroku:\n", error)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "CREATE TABLE Institutions(instid serial primary key, instname varchar(30), instlocation varchar(30), "
            "insttype varchar(30));"
        )
        cursor.execute(
            "CREATE TABLE Operator(oid serial primary key, ousername varchar(30), opassword varchar(100), " 
            "ofirstname varchar(30), olastname varchar(30), olevel varchar(30), " 
            "instid integer references Institutions(instid));"
        )
        cursor.execute(
            "CREATE TABLE Citizen(cid serial primary key, cfirstname varchar(30), clastname varchar(30), "
            "cDOB date, cgender varchar(30), caddress varchar(30), cphone varchar(30), " 
            "cssn numeric(9, 0) unique, ishp boolean);"
        )
        cursor.execute(
            "CREATE TABLE Illness(iid serial primary key, iname varchar(30) unique, iinfectedcount integer, "
            "iirecoveredcount integer, iireinfectedcount integer, ideceasedcount integer);"
        )
        cursor.execute(
            "CREATE TABLE Tests(tid serial primary key, " 
            "ttimestamp timestamp without time zone default (now() at time zone 'utc'), "
            "tillness varchar(30) references Illness(iname), tispositive boolean, instname varchar(30), "
            "cid integer references Citizen(cid), oid integer references Operator(oid));"
        )
        cursor.execute(
            "CREATE TABLE Infected(cid integer primary key references Citizen(cid), infcount integer, "
            "infcheckup integer default 14, infdate timestamp without time zone default (now() at time zone 'utc'), " 
            "infname varchar(30) references Illness(iname));"
        )
        cursor.execute(
            "CREATE TABLE Recovered(cid integer primary key references Citizen(cid), " 
            "rdate timestamp without time zone default (now() at time zone 'utc'), "
            "rlength varchar(30), rillness varchar(30) references Illness(iname));"
        )
        cursor.connection.commit()

    def drop_tables(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "DROP TABLE IF EXISTS Citizen, Illness, Infected, Institutions, Operator, Recovered, Tests CASCADE;"
        )
        cursor.connection.commit()

    def truncate_tables(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "TRUNCATE TABLE institutions, citizen, illness, infected, operator, recovered, tests " 
            "RESTART IDENTITY CASCADE;")
        self.connection.commit()

    def populate_db(self):
        cursor = self.connection.cursor()
        # POPULATE INSTITUTIONS TABLE
        cursor.execute(
            "INSERT INTO institutions(instname, instlocation, insttype) "
            "VALUES ('Perea', 'Mayaguez', 'Hospital');"
        )
        cursor.execute(
            "INSERT INTO institutions(instname, instlocation, insttype) "
            "VALUES ('Concepción', 'San German', 'Hospital');"
        )
        cursor.execute(
            "INSERT INTO institutions(instname, instlocation, insttype) "
            "VALUES ('Lab Irrizarry', 'Mayaguez', 'Lab');"
        )
        # POPULATE OPERATOR TABLE
        cursor.execute(
            "INSERT INTO operator(ousername, opassword, ofirstname, olastname, olevel, instid) "
            "VALUES ('ramoncin', '123abc', 'Ramon', 'Rosado', 'admin', 2);"
        )
        cursor.execute(
            "INSERT INTO operator(ousername, opassword, ofirstname, olastname, olevel, instid) "
            "VALUES ('chr1s', '123pescaitoEs', 'Chris', 'something', 'admin', 1);"
        )
        cursor.execute(
            "INSERT INTO operator(ousername, opassword, ofirstname, olastname, olevel, instid) "
            "VALUES ('marko', 'polo', 'Mark', 'noC', 'admin', 3);"
        )
        # POPULATE CITIZEN TABLE
        cursor.execute(
            "INSERT INTO citizen(cfirstname, clastname, cdob, cgender, caddress, cphone, cssn, ishp) "
            "VALUES ('Juan', 'delPueblo', '1/1/2020', 'M', 'San German', '7871234567', '000000000', 'true');"
        )
        cursor.execute(
            "INSERT INTO citizen(cfirstname, clastname, cdob, cgender, caddress, cphone, cssn, ishp) "
            "VALUES ('Soledad', 'nuncaEstaSola', '1/1/1996', 'F', 'Mayaguez', '7870000000', '111111111', 'true');"
        )
        cursor.execute(
            "INSERT INTO citizen(cfirstname, clastname, cdob, cgender, caddress, cphone, cssn, ishp) "
            "VALUES ('LaLlorona', 'deLajas', '6/6/2000', 'F', 'Lajas', '7876666666', '666666666', 'false');"
        )
        cursor.execute(
            "INSERT INTO citizen(cfirstname, clastname, cdob, cgender, caddress, cphone, cssn, ishp) "
            "VALUES ('Pedro', 'Romero', '3/6/2020', 'M', 'Ponce', '7871112233', '123456789', 'true');"
        )
        # POPULATE ILLNESS TABLE
        cursor.execute(
            "INSERT INTO Illness(iname, iinfectedcount, iirecoveredcount, iireinfectedcount, ideceasedcount) " 
            "VALUES ('COVID-19', 1, 0, 0, 1);"
        )
        # POPULATE TESTS TABLE
        cursor.execute(
            "INSERT INTO tests(ttimestamp, tillness, tispositive, instname, cid, oid) "
            "VALUES ('10/1/2020', 'COVID-19', 'true', 'Perea', 1, 1);"
        )
        cursor.execute(
            "INSERT INTO tests(ttimestamp, tillness, tispositive, instname, cid, oid) "
            "VALUES ('11/11/2020', 'COVID-19', 'false', 'Concepción', 2, 1);"
        )
        cursor.execute(
            "INSERT INTO tests(tillness, tispositive, instname, cid, oid) "
            "VALUES ('COVID-19', 'true', 'Lab Irrizarry', 4, 2);"
        )
        # POPULATE INFECTED TABLE
        cursor.execute(
            "INSERT INTO Infected(cid, infcount, infcheckup, infname) " 
            "VALUES (1, 1, 14, 'COVID-19');"
        )
        cursor.execute(
            "INSERT INTO Infected(cid, infcount, infcheckup, infdate, infname) "
            "VALUES (4, 1, 14, '8/8/2020', 'COVID-19');"
        )
        self.connection.commit()


if __name__ == '__main__':
    test = DBManager()
    test.drop_tables()
    test.create_tables()
    # test.truncate_tables()
    test.populate_db()
    test.connection.close()
