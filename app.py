import datetime
import argparse
import requests
import logging

from bs4 import BeautifulSoup
from tabulate import tabulate
url="https://www.mohfw.gov.in/"
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
header=[ 'State','Cases','Cured','Death']


if(__name__=="__main__"):

    #request for html data and getting required data
    response=requests.get(url)
    html=BeautifulSoup(response.content,"html.parser")
   
    data=html.tbody.find_all('tr')
    data=list(map(lambda x: x.find_all("td"),data))
    data=list(map(lambda x:[i.text for i in x[1:]] ,data))
    data=data[:-3]
    data.pop();

    #Data base work
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from state import State,Base
    
    engine=create_engine("sqlite:///data.db",echo=True)
    engine.connect();
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    session=Session()
    for row in data:
        state=State(*row)
        session.add(state)
    session.commit()