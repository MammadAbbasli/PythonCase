# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:30:53 2020

@author: Mammad Abbasli
"""

###################### LIBRARIES ########################################
from selenium import webdriver
import time
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
########################## CONNECTION ###################################
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&page=1&perPage=20&searchSource=GN_BREADCRUMB&sort=relevance&zc=90006")

time.sleep(3)
################################ SCROLL FOR FILTER #######################
driver.execute_script("window.scrollTo(0, 800)")
time.sleep(2)

#click SearchButton for filter models BMW#####################
clicke_bmw=driver.find_element_by_xpath("//*[@id='mkId']/ul/li[10]/label")
clicke_bmw.click()
time.sleep(2)
#scroll#
time.sleep(2)
driver.execute_script("window.scrollTo(0, 600)")
######################################   CAR INFO   #####################
Model=[]
Year=[]  
Prices=[]
Ext_Color=[]
Int_Color=[]
Transmission=[]
Drivetrain=[]
Numbers=[]
################### MODEL , YEAR AND PRICE ##############################
########################## BMW ##########################################
object_car=driver.find_elements_by_class_name("listing-row__title")
info=driver.find_elements_by_class_name("listing-row__meta")
numbers=driver.find_elements_by_class_name("dealer-name")
prices=driver.find_elements_by_class_name("listing-row__price")
match=False

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
bmw=0
try:
  while(match==False):
      time.sleep(1) 
      if(bmw<=40):
          for obj in object_car:
               obj=str(obj.text)
               Model.append(obj[5:9])
               Year.append(obj[:4])
               bmw=Model.count('BMW ')
                 
          for inf in info:
               inf=str(inf.text) 
               inf=inf.replace('Ext. Color:','')
               inf=inf.replace('Int. Color:','')
               inf=inf.replace('Transmission:','')
               inf=inf.replace('Drivetrain:','')
               inf=inf.strip()
               inf=inf.replace(" ",",")
               inf=inf.replace("\n","")
               inf=inf.split(",")
               Ext_Color.append(inf[0])
               Int_Color.append(inf[1])
               Transmission.append(inf[2])
               Drivetrain.append(inf[3])
                       
          for price in prices:
               price=str(price.text)
               price=price.replace("MSRP ","")
               Prices.append(price)
                 
          for num in numbers:
               num=str(num.text)
               num=num[-15:]
               num=num.strip()
               Numbers.append(num)
          
          lastCount = lenOfPage
          lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
          if lastCount == lenOfPage:
               next_btn=driver.find_element_by_xpath("/html/body/div[1]/div[4]/cars-filters/div[1]/cars-pagination/div[1]/a[2]")
               next_btn.click()
          
      else:
          match=True   
except:
     print("hata") 
print(bmw)
     
################## MODEL , YEAR AND PRICE ##############################
######################### Ford##########################################
driver.get("https://www.cars.com/for-sale/searchresults.action/?dealerType=localOnly&page=1&perPage=20&searchSource=GN_BREADCRUMB&sort=relevance&zc=90006")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 800)")
time.sleep(2)
#click SearchButton for filter models BMW#####################
clicke_ford=driver.find_element_by_xpath("//*[@id='mkId']/ul/li[31]/label")
clicke_ford.click()
time.sleep(2)
#scroll#
time.sleep(2)
driver.execute_script("window.scrollTo(0, 600)")
time.sleep(1)

object_car=driver.find_elements_by_class_name("listing-row__title")
info=driver.find_elements_by_class_name("listing-row__meta")
numbers=driver.find_elements_by_class_name("dealer-name")
prices=driver.find_elements_by_class_name("listing-row__price")
match=False
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
ford=0
try:
  while(match==False):
      time.sleep(2) 
      if(ford<=40): 
          for obj in object_car:
               obj=str(obj.text)
               Model.append(obj[5:9])
               Year.append(obj[:4])
               ford=Model.count('Ford')
                
          for inf in info:
               inf=str(inf.text) 
               inf=inf.replace('Ext. Color:','')
               inf=inf.replace('Int. Color:','')
               inf=inf.replace('Transmission:','')
               inf=inf.replace('Drivetrain:','')
               inf=inf.strip()
               inf=inf.replace(" ",",")
               inf=inf.replace("\n","")
               inf=inf.split(",")
               Ext_Color.append(inf[0])
               Int_Color.append(inf[1])
               Transmission.append(inf[2])
               Drivetrain.append(inf[3])
                   
          for price in prices:
               price=str(price.text)
               price=price.replace("MSRP ","")
               Prices.append(price)
                     
          for num in numbers:
               num=str(num.text)
               num=num[-15:]
               num=num.strip()
               Numbers.append(num)
       
          lastCount = lenOfPage
          lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
          if lastCount == lenOfPage:
               next_btn=driver.find_element_by_xpath("/html/body/div[1]/div[4]/cars-filters/div[1]/cars-pagination/div[1]/a[2]")
               next_btn.click()
              
      else:
          match=True   
except:
     print("hata") 
time.sleep(2)
driver.close()
##################### COLLECT ALL DATE IN DATAFRAME ######################
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
