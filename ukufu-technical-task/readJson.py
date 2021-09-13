"""
Description: This module reads the data from json files present in resources directory
             and perform different fetch operations based on below scenarios.
              Following scenerios have been covered in this script:-

              1. Given a company, the API needs to return all their employees. 
                 Provide the appropriate solution if the company does not have any
                 employees.
              2. Given 2 people, provide their information (Name, Age, Address, phone) 
                and the list of their friends in common who have brown eyes and 
                are still alive.

              3. Given 1 people, provide a list of fruits and vegetables they like.
                 This endpoint must respect this interface for the output: 
                 {"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], 
                  "vegetables": ["beetroot", "lettuce"]} 

Author:     Shivender Khajuria           
Dated:      13-09-21
Filename:   readJson.py
Version:    1.0
Purpose:    UKUFU Tech Test

"""

import json

#Global variables
dir_path = '../ukufu-technical-task/resources/'
filename_people = 'people.json'
filename_company = 'companies.json'
emp_name_list, index_list, company_id_list = [], [], []
fav_food_list,company_name_list = [], []

#Read Operations - people.json
def readJsonPeople(dir_path,filename_people):
    #People json deserialize op    
    with open(dir_path + filename_people, "r") as read_file:
        data_people = json.load(read_file)
    return data_people

   
#Read Operations - companies.json
def readJsonCompany(dir_path,filename_company):
    #Company json deserialize operation
    with open(dir_path + filename_company, "r") as read_file:
        data_companies = json.load(read_file)
    return data_companies

"""
Reqmt_01.Given a company, the API needs to return all their employees. 
Provide the appropriate solution if the company does not have any
employees.
"""
def fetch_employees(p_company_id):
    data_people =  readJsonCompany(dir_path,filename_people)        
    for item in data_people:
        index_list.append(item['index'])
        emp_name_list.append(item['name'])
        company_id_list.append(item['company_id'])
        fav_food_list.append(item['favouriteFood'])
    keys = company_id_list
    values = emp_name_list  
    emp_dict = {k: [values[i] for i in [j for j, x in enumerate(keys) if x == k]] for k in set(keys)}           
    return emp_dict.get(p_company_id)

"""
Reqmt_02.Given 2 people, provide their information 
(Name, Age, Address, phone) and the list of their 
friends in common who have brown eyes and #are still alive.
"""
def fetch_people_details(p_name_01,p_name_02):    
    data_people =  readJsonCompany(dir_path,filename_people)    
    list_01, list_02 = [], []

    for i in range(len(data_people)):
        if p_name_01 == data_people[i]['name']:            
            list_01.append(data_people[i]['name'])
            list_01.append(data_people[i]['age'])
            list_01.append(data_people[i]['address'])
            list_01.append(data_people[i]['phone'])
            for item in data_people[i]['friends']:
                if data_people[item.get('index')]['eyeColor'] == 'brown' \
                and data_people[item.get('index')]['has_died'] == False:         
                    list_01.append(data_people[item.get('index')]['name'])
    
    for i in range(len(data_people)):
        if p_name_02 == data_people[i]['name']:            
            list_02.append(data_people[i]['name'])
            list_02.append(data_people[i]['age'])
            list_02.append(data_people[i]['address'])
            list_02.append(data_people[i]['phone'])
            for item in data_people[i]['friends']:
                if data_people[item.get('index')]['eyeColor'] == 'brown'\
                and data_people[item.get('index')]['has_died'] == False:               
                    list_02.append(data_people[item.get('index')]['name'])    
    return list_01,list_02

   
"""
Reqmt_03
Given 1 people, provide a list of fruits and vegetables they like.
This endpoint must respect this interface for the output: 
{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], 
"vegetables": ["beetroot", "lettuce"]}
""" 
def fetch_food_details(p_index):    
    data_people =  readJsonCompany(dir_path,filename_people)    
    dict_food = {}
    for i in range(len(data_people)):
        if p_index == data_people[i]['index']:                      
            dict_food['username'] = data_people[i]['name']
            dict_food['age'] = data_people[i]['age']
            for item in data_people[i]['favouriteFood']:
                if item not in ['cucumber', 'beetroot','celery', 'carrot']:                                      
                    dict_food.setdefault('fruits', []).append(item)
            for item in data_people[i]['favouriteFood']:          
                if item  not in ['orange','banana', 'strawberry', 'apple']:                    
                    dict_food.setdefault('vegetables', []).append(item)
    return dict_food     

#Driver code to perform basic sanity check.Uncomment when required to validate API data.
""""
if __name__ == '__main__':
    #Rqmt_01    
    emp_dict = fetch_employees(98)
    print("Rqmt_01 data-->")
    print(emp_dict)
    l1, l2 = [], []    
    #Reqmt_02
    l1, l2 = fetch_people_details('Hardin Bradshaw','Gilbert Grant')
    print("Rqmt_02 data-->")
    print("l1 is :: ", l1)
    print("l2 is :: ", l2)
    #Reqmt_03    
    dict_food = {}
    dict_food = fetch_food_details(921)
    print("Rqmt_03 data-->")
    print("Printing diction for food...", dict_food)
    
"""
     
    
    
  
