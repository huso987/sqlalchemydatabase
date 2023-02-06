
from sqlalchemy import create_engine,Column,Integer,String,MetaData
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import * 
from sqlalchemy_utils import database_exists,create_database,drop_database
import sqlalchemy as sa


'''
As the exception message says, sqlalchemy "could not assemble any 
primary key columns for mapped table 'users'". The sqlalchemy orm
needs a primary key for each mapped table.
'''

class MySql:

    def __init__(self):
        self.a=False
        self.b=False
        
        
    
    def login(self,uname,upsw):
        try:
           
            self.url='mysql://'+uname+':'+upsw+'@localhost:3306'
            engine=create_engine(self.url)
            connection=engine.connect()
            self.a=True            
        except:
            print("You entered does not match an serveracount")
    
           
    def createDatabase(self,dataname):
        engine=create_engine(self.url+'/'+dataname)
        if not database_exists(engine.url):
            create_database(engine.url)
    def dropDatabase(self,dataname):
        engine=create_engine(self.url+'/'+dataname)
        if database_exists(engine.url):
            drop_database(engine.url)
    def listDatabases(self):
        engine=sa.create_engine(self.url)
        insp = sa.inspect(engine)
        db_list = insp.get_schema_names()
        for i in db_list:
            print(i)
    def createTable(self,dname,tname,data):
        
        try:
          engine=create_engine(self.url+'/'+dname)
          connection=engine.connect()
          self.b=True
        except:
            print("You entered does not match an database")
        if self.b==True:
            Session=sessionmaker(bind=engine)
            session=Session()
            base=declarative_base()
            class User(base):
                __tablename__=tname                   
                id=Column(Integer,primary_key=True)
                name=Column(String(50))
                age=Column(Integer)
            base.metadata.create_all(engine)
            
            print("!!Created Table!!".center(50," "))
            connection.close()
    def dropTable(self,dname,tname):
        try:
          engine=create_engine(self.url+'/'+dname)
          connection=engine.connect()
          self.b=True
        except:
            print("You entered does not match an database")
        if self.b==True:
            Session=sessionmaker(bind=engine)
            session=Session()
            base=declarative_base()
            class User(base):
                __tablename__=tname                   
                id=Column(Integer,primary_key=True)
                name=Column(String(50))
                age=Column(Integer)
            base.metadata.drop_all(engine)
            connection.close()
    def listTables(self,dname):
        try:
          engine=create_engine(self.url+'/'+dname)
          connection=engine.connect()
          self.b=True
        except:
            print("You entered does not match an database")
        if self.b==True:
            insp = sa.inspect(engine)
            db_list = insp.get_table_names()
            for  i in db_list:
                print(i)
            print("!!Listed  Tables!!".center(50," "))
            connection.close()
    def insertTable(self,dname,tname):
        try:
          engine=create_engine(self.url+'/'+dname)
          connection=engine.connect()
          self.b=True
        except:
            print("You entered does not match an database")
        if self.b==True:
            Session=sessionmaker(bind=engine)
            session=Session()
            base=declarative_base()
            class User(base):
                __tablename__=tname
                id=Column(Integer,primary_key=True)
                name=Column(String(50))
                age=Column(Integer)
            user1=User(name='hasan',age=25)
            user2=User(name='ufuk',age=27)
            #session.add(user1)
            session.add_all([user1,user2])
            session.commit()
            print("!!Inserted!!".center(50," "))
            connection.close()
    def readTable(self,dname,tname):
        try:
          engine=create_engine(self.url+'/'+dname)
          connection=engine.connect()
          self.b=True
        except:
            print("You entered does not match an database")
        if self.b==True:
            Session=sessionmaker(bind=engine)
            session=Session()
            base=declarative_base()
            class User(base):
                __tablename__=tname
                id=Column(Integer,primary_key=True)
                name=Column(String(50))
                age=Column(Integer)
            users=session.query(User)
            for i in users:
                print(i.id, i.name , i.age)
            connection.close()
    def updateTable(self,dname,tname):
        try:
          engine=create_engine(self.url+'/'+dname)
          connection=engine.connect()
          self.b=True
        except:
            print("You entered does not match an database")
        if self.b==True:
            Session=sessionmaker(bind=engine)
            session=Session()
            base=declarative_base()
            class User(base):
                __tablename__=tname
                id=Column(Integer,primary_key=True)
                name=Column(String(50))
                age=Column(Integer)
            users=session.query(User).filter(User.name=="hasan").first()
            users.name="ufuk"
            session.commit()
            connection.close()
    def deleteinTable(self,dname,tname):
        try:
          engine=create_engine(self.url+'/'+dname)
          connection=engine.connect()
          self.b=True
        except:
            print("You entered does not match an database")
        if self.b==True:
            Session=sessionmaker(bind=engine)
            session=Session()
            base=declarative_base()
            class User(base):
                __tablename__=tname
                id=Column(Integer,primary_key=True)
                name=Column(String(50))
                age=Column(Integer)
            users=session.query(User).filter(User.name=="ufuk").first()
            session.delete(users)
            session.commit()
            connection.close()



    
object1=MySql()
print("LOGIN".center(50,"*"))
x=input("username=")
y=input("userpassword=")
object1.login(x,y)


if object1.a==True:
    print("!!Signed in!!")
    while True:
        print("Menu".center(50,"*"))    
        seçim=input("1-List Databases\n2-Create Database\n3-Drop Database\n4-Create Table\n5-Drop Tables\n"+
        "6-List Tables\n7-Insert data in Table\n8-Read data in Table\n9-Update data in Table\n10-Delete data in table\n11-Exit\nSeçiminiz=")
        print("".center(50,"*"))
        if seçim=="1":
            object1.listDatabases()
            print("!!Listed Databases!!".center(50," "))
        elif seçim=="2":
            dataname=input("Dataname=")
            rest=object1.createDatabase(dataname)
            print("!!Created Database!!".center(50," "))
        elif seçim=="3":
            dataname=input("Dataname=")
            rest=object1.dropDatabase(dataname)
            print("!!Deleted Database!!".center(50," "))
        elif seçim=="4":
            datan=input("Dataname=")
            tabname=input("Tablename=")
                
            rest=object1.createTable(datan,tabname)
            
        elif seçim=="5":
            data_name=input("Dataname=")
            tabname=input("Tablename=")   
            object1.dropTable(data_name,tabname)
            
        elif seçim=="6":
            dname=input("Dataname=")  
            object1.listTables(dname)
           
        elif seçim=="7":
            datan=input("Dataname=")
            tabname=input("Tablename=")       
            rest=object1.insertTable(datan,tabname)
        elif seçim=="8":
            datan=input("Dataname=")
            tabname=input("Tablename=")       
            rest=object1.readTable(datan,tabname)
        elif seçim=="9":
            datan=input("Dataname=")
            tabname=input("Tablename=")       
            rest=object1.updateTable(datan,tabname)
        elif seçim=="10":
            datan=input("Dataname=")
            tabname=input("Tablename=")       
            rest=object1.deleteinTable(datan,tabname)
        elif seçim=="11":
            break
        else:
            print("Incorrect choice".center(50," "))







    
    
    




    


