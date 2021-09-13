"""
Decription: This utility is based on FastAPI which is a modern, 
            fast (high-performance), web framework for building APIs with Python 3.6+ 
            based on standard Python type hints.
            
Author:     Shivender Khajuria           
Dated:      13=09-21
Filename:   main.py
Version:    1.0
Purpose:    UKUFU Tech Test

"""

from typing import Optional,List
from fastapi import FastAPI, Path
from pydantic import BaseModel
import readJson

app = FastAPI()

@app.get("/")
def read_root():
    return {"UKUFU": "Tech Task"}

#Reqmt_01: To fetch all the employees associated with a company.
@app.get("/employees/{company_id}")
def read_employees(company_id: int):   
    emp_name = readJson.fetch_employees(company_id)   
    return {"List of Employees": emp_name} if emp_name is not None else 'No Employees found'

#Reqmt_02: To get personal information of two people.
@app.get("/people/")
async def read_people_details(name_01: str = "Hardin Bradshaw", name_02: str = "Gilbert Grant"):  
    person_01, person_02 = readJson.fetch_people_details(name_01,name_02)    
    return {"People details are": person_01 + person_02}

#Reqmt_03: To fetch food data.
@app.get("/food/{index_id}")
def read_food_details(index_id: int):   
    dict_food = readJson.fetch_food_details(index_id)   
    return {"Food Details": dict_food}
