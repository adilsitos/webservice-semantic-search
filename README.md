# webservice-semantic-search
This repository contains the back-end of a recommendation system using semantic search.

Recommendation system code can be found at: [amazon-semantic-search](https://github.com/Adilsitos/Semantic-Search-Amazon-Data)

The development was entirely made in [Django](https://www.djangoproject.com/) a framework in Python used to create web services. 

API can be found here: https://semanticserviceapi.herokuapp.com/

End points: 
  - /api/recommendations/ (Used to insert feedbacks from users about a recommendation) 


### Running Locally
1. Create a virtualEnv in the source 
    ```
    virtualenv -p python3 venv
    ```
2. Activate the virtual env
    ```
    source venv/bin/activate
    ```
3. Install the dependencies on the virtual env
    ```
    pip install -r src/requirements.txt
    ```
4. Execute the migrations on the database
    ```
    python src/manage.py migrate
    ```
