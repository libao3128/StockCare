import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import datetime



def Get_Inten(target):
    Intensive={}
    url = "https://concords.moneydj.com/z/zc/zco/zco_"+target+"_1.djhtm"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    text=soup.findAll("td",class_="t3n1",colspan="4")
    if(len(text)==4):
        Intensive["1b"]=text[0].text
        Intensive["1s"]=text[1].text
    else:
        Intensive["1b"]=np.nan
        Intensive["1s"]=np.nan
     
    url = "https://concords.moneydj.com/z/zc/zco/zco_"+target+"_2.djhtm"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    text=soup.findAll("td",class_="t3n1",colspan="4")
    if(len(text)==4):
        Intensive["5b"]=text[0].text
        Intensive["5s"]=text[1].text
    else:
        Intensive["5b"]=np.nan
        Intensive["5s"]=np.nan
   
    url = "https://concords.moneydj.com/z/zc/zco/zco_"+target+"_4.djhtm"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    text=soup.findAll("td",class_="t3n1",colspan="4")
    if(len(text)==4):
        Intensive["20b"]=text[0].text
        Intensive["20s"]=text[1].text
    else:
        Intensive["20b"]=np.nan
        Intensive["20s"]=np.nan


    url = "https://concords.moneydj.com/z/zc/zco/zco_"+target+"_6.djhtm"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    text=soup.findAll("td",class_="t3n1",colspan="4")
    if(len(text)==4):
        Intensive["60b"]=text[0].text
        Intensive["60s"]=text[1].text
    else:
        Intensive["60b"]=np.nan
        Intensive["60s"]=np.nan 
    #print(text)
    
    url = "https://concords.moneydj.com/z/zc/zco/zco_"+target+"_8.djhtm"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    text=soup.findAll("td",class_="t3n1",colspan="4")
    if(len(text)==4):
        Intensive["240b"]=text[0].text
        Intensive["240s"]=text[1].text
    else:
        Intensive["240b"]=np.nan
        Intensive["240s"]=np.nan
    
    return Intensive


table=pd.read_excel("???????????????.xlsx",usecols="A:M")
table.to_excel("???????????????copy.xlsx",index=False)
table['??????']=table['??????'].fillna('null')
table=table[~table['??????'].isin(['null'])]
today=datetime.date.today()


for i in range (len(table)):
    print(table.loc[i,"??????"])
    if(table.loc[i,'????????????'] != today):
        table.loc[i,'??????']=int(table.loc[i,'??????'])
        table.loc[i,'??????']=str(table.loc[i,'??????'])
        Inten=Get_Inten(table.loc[i,'??????'])
        table.loc[i,"1?????????"]=Inten["1b"];
        table.loc[i,"1?????????"]=Inten["1s"];
        table.loc[i,"5?????????"]=Inten["5b"];
        table.loc[i,"5?????????"]=Inten["5s"];
        table.loc[i,"20?????????"]=Inten["20b"];
        table.loc[i,"20?????????"]=Inten["20s"];
        table.loc[i,"60?????????"]=Inten["60b"];
        table.loc[i,"60?????????"]=Inten["60s"];
        table.loc[i,"240?????????"]=Inten["240b"];
        table.loc[i,"240?????????"]=Inten["240s"];
    table.loc[i,"????????????"]=today;
    if(i%100==0):
        table.to_excel("???????????????.xlsx",index=False)
table.to_excel("???????????????.xlsx",index=False)



