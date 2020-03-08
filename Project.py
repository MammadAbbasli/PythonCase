# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:38:33 2020

@author: mamed
"""
###############LIBRARIES################
import pandas as pd
import requests
from bs4 import BeautifulSoup
######################################   CAR INFO   #####################
Model=[]
Year=[]  
Prices=[]
Ext_Color=[]
Int_Color=[]
Transmission=[]
Drivetrain=[]
Numbers=[]
################### MODEL , YEAR....... ##############################
###############function helps to clear data###########

def clean(parameter):
    parameter=parameter.replace('Ext. Color:','')
    parameter=parameter.replace('Int. Color:','')
    parameter=parameter.replace('Transmission:','')
    parameter=parameter.replace('Drivetrain:','')
    parameter=parameter.strip()
    return parameter
###########################getting ford information#######################
ford=0    
for i in range(1,3):
    ########################## CONNECTION ###################################
    url=("https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&mkId=20015&page="+str(i)+"&perPage=20&searchSource=GN_REFINEMENT&sort=relevance&zc=90006")
    param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    response=requests.get(url,param)
    soup=BeautifulSoup(response.content,"html.parser")
        
    for i in range(0,20):
        Title=soup.find_all('div',attrs={"class":"shop-srp-listings__inner"})[i].find("div",{"class":"listing-row__details"}).find("h2",{"class":"listing-row__title"}).text.strip()
        model=Title[5:9]
        year=Title[0:4]
        Model.append(model)
        Year.append(year)
        if(model=="Ford"):
            ford=ford+1
            ####
            info=soup.find_all('div',attrs={"class":"shop-srp-listings__inner"})[i].find("div",{"class":"listing-row__details"}).find("ul",{"class":"listing-row__meta"})
            extcolor=info.find_all("li")[0].text.strip()
            extcolor=clean(extcolor)
            inttcolor=info.find_all("li")[1].text.strip()
            inttcolor=clean(inttcolor)
            trs=info.find_all("li")[2].text.strip()
            trs=clean(trs)
            drr=info.find_all("li")[3].text.strip()
            drr=clean(drr)
            Ext_Color.append(extcolor)
            Int_Color.append(inttcolor)
            Transmission.append(trs)
            Drivetrain.append(drr)
              ###########################
            price=soup.find_all('div',attrs={"class":"shop-srp-listings__inner"})[i].find("div",{"class":"listing-row__details"}).find("div",{"class":"payment-section"})
            payment=price.find("span").text.strip()
            Prices.append(payment)
              ########################
            dealer=soup.find('div',attrs={"class":"shop-srp-listings__inner"}).find("div",{"class":"listing-row__details"}).find("div",{"class":"dealer-name"}).find('div',{"class":"listing-row__phone"})
            number=dealer.find_all("span")[3].text
            Numbers.append(number)

print(ford)
###########################getting bmw information######################
bmw=0
for i in range(1,3):
     ########################## CONNECTION ###################################
    url=("https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&mkId=20005&page="+str(i)+"&perPage=20&searchSource=GN_REFINEMENT&sort=relevance&zc=90006")
    param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    response=requests.get(url,param)
    soup=BeautifulSoup(response.content,"html.parser")
        
    for i in range(0,20):
        Title=soup.find_all('div',attrs={"class":"shop-srp-listings__inner"})[i].find("div",{"class":"listing-row__details"}).find("h2",{"class":"listing-row__title"}).text.strip()
        model=Title[5:9]
        year=Title[0:4]
        Model.append(model)
        Year.append(year)
        if(model=="BMW "):
            bmw+=1
            ####
            info=soup.find_all('div',attrs={"class":"shop-srp-listings__inner"})[i].find("div",{"class":"listing-row__details"}).find("ul",{"class":"listing-row__meta"})
            extcolor=info.find_all("li")[0].text.strip()
            extcolor=clean(extcolor)
            inttcolor=info.find_all("li")[1].text.strip()
            inttcolor=clean(inttcolor)
            trs=info.find_all("li")[2].text.strip()
            trs=clean(trs)
            drr=info.find_all("li")[3].text.strip()
            drr=clean(drr)
            Ext_Color.append(extcolor)
            Int_Color.append(inttcolor)
            Transmission.append(trs)
            Drivetrain.append(drr)
              ###########################
            price=soup.find_all('div',attrs={"class":"shop-srp-listings__inner"})[i].find("div",{"class":"listing-row__details"}).find("div",{"class":"payment-section"})
            payment=price.find("span").text.strip()
            Prices.append(payment)
              ########################
            dealer=soup.find('div',attrs={"class":"shop-srp-listings__inner"}).find("div",{"class":"listing-row__details"}).find("div",{"class":"dealer-name"}).find('div',{"class":"listing-row__phone"})
            number=dealer.find_all("span")[3].text
            Numbers.append(number)

print(bmw)

###################### COLLECT ALL DATE IN DATAFRAME ######################
Model=pd.DataFrame(Model,columns=["models"])
Year=pd.DataFrame(Year,columns=['year'])
Prices=pd.DataFrame(Prices,columns=['price'])
Ext_Color=pd.DataFrame(Ext_Color,columns=['ext_color'])
Int_Color=pd.DataFrame(Int_Color,columns=['int_color'])
Transmission=pd.DataFrame(Transmission,columns=['transmission'])
Drivetrain=pd.DataFrame(Drivetrain,columns=['drivetrain'])
Numbers=pd.DataFrame(Numbers,columns=['phone_num'])
final_data=pd.concat([Model,Year],axis=1)
final_data=pd.concat([final_data,Prices],axis=1)
final_data=pd.concat([final_data,Ext_Color],axis=1)
final_data=pd.concat([final_data,Int_Color],axis=1)
final_data=pd.concat([final_data,Transmission],axis=1)
final_data=pd.concat([final_data,Drivetrain],axis=1)
final_data=pd.concat([final_data,Numbers],axis=1)
final_data.to_csv('table.csv')
