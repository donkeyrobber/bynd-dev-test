**Dev-Test**

Beyond backend developer coding test submission

Exercises:

1. Write a function to take a fixed set of data and insert it into a database.
2. Write a unit test to verify the function works.
3. Create a client/server application to allow discovery on a network.
  a. A simple server that broadcasts it's existence with a set of data (i.e. ID, MAC or IP)
  b. A client that searches for the server and displays in a terminal the data received.

**Setup**

`docker-compose up -d`

**Execution**

- ex. 1 

    - `docker-compose run app python insert_record.py`
    
    (The database is exposed on `port 33060`, so it can be connected to from an external client for verification)

- ex. 2

   - `docker-compose run app python -m unittest`
