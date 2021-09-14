# Instruction Manual
---------------------------


##  I Prerequisite steps before executing FASTAPI:
      1. Ensure the folder strucure is created similar to the one here in github.
      2. Create virtual env using command:- python -m venv ukufu_venv.      
      3. Actiavte virtual env using command:- ukufu_venv\Scripts\activate.      
      4. Make sure python version is above 3.6 or later (Python version - 3.8) is installed.
      5. Install dependencies using - pip install -r requirements.txt.
      
      Note:* Please note that the developement for this project is done on Windows (Win 10) platform.

## II Run the server with command:
        uvicorn main:app --reload

## III Testing the API end points:

### Scenerio 01 - Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.

Run this url in browser: http://127.0.0.1:8000/employees/98?

(Here 98 represents company_id associated with a company)

### Scenerio 02 - Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common who have brown eyes and are still alive.

Run this url in browser: http://127.0.0.1:8000/people/?name_01=Bonnie%20Bass&name_02=Rosemary%20Hayes

(Here name_01 and name_02 represent names of two people)

### Scenerio 03 - Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: {"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}.

Run this url in browser: http://127.0.0.1:8000/food/921?

(Here 921 represents index id for a person)

### Alternatively try Interactive API docs- 
Go to URL: http://127.0.0.1:8000/docs.
