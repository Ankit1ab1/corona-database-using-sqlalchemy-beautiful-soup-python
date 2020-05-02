from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

class State(Base):
    __tablename__="Corona State wise Data"

    state=Column(String(100),primary_key=True)
    total_cases=Column(Integer)
    recovered=Column(Integer)
    death=Column(Integer)

    def __init__(self,state,total_cases,recovered,death):
        self.state=state;
        self.total_cases=total_cases
        self.recovered=recovered
        self.death=death

   
    def __str__(self):
        return """State :{}\nTotalcases :{}\nRecovered :{}Death :{}
                    """.format(self.state,self.total_cases,self.recovered,self.death)
  
