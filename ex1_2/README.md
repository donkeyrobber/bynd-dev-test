**Dev-Test**


**Exercise 1:** Write a function to take a fixed set of data and insert it into a database.

**Exercise 2:** Write a unit test to verify the function works.

**Setup**

`docker-compose up -d`

**Execution**

- ex. 1 

    - `docker-compose run app python insert_record.py`
    
    (The database is exposed on `port 33060`, so it can be connected to from an external client for verification)

- ex. 2

   - `docker-compose run app python -m unittest`
