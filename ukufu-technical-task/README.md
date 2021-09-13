# Instruction Manual
---------------------------


##  I Prerequisite steps before executing FASTAPI:
      1. Create virtual env  using cmd - python -m venv ukufu_venv.      
      2. Actiavte virtual env - django_env_01\Scripts\activate.
      3. Ensure the folder strucure is created similar to the one here in guthub.
      3. Ensure python version is above 3.6 or later (Python version - 3.8).
      4. Install dependencies using - pip install -r requirements.txt.

## II Run the server with command:
        uvicorn main:app --reload



## III Testing the API end points:

### Scenerio 01 - Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.

Run this url in browser: http://127.0.0.1:8000/employees/98?

### Scenerio 02 - Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common who have brown eyes and are still alive.

Run this url in browser: http://127.0.0.1:8000/people/?name_01=Bonnie%20Bass&name_02=Rosemary%20Hayes

### Scenerio 03 - Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: {"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}.

Run this url in browser: http://127.0.0.1:8000/food/921?
   
