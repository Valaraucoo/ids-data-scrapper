### Bus delay scrapper - Cracow

- Create and activate virtual enviroment:
    ```bash
    python3 -m venv venv
  
    # for Windows
    venv\Scripts\activate.bat
    
    # for Unix or MacOS
    source venv/bin/activate
    ```
- Set up project:
    ```bash
    python3 setup.py
    ```
- If everything is OK run `start.py`.
- Collected data will be stored in `data/` directory.

You can change value of `DELAY_BETWEEN_LOOPS` and `DELAY_BETWEEN_STOPS` with additional arguments in `start.py`:
```bash
# default
python3 start.py
[INFO]: DELAY_BETWEEN_LOOPS=10, DELAY_BETWEEN_STOPS=0.5

# manually set DELAY_BETWEEN_LOOPS
python3 start.py 20
[INFO]: DELAY_BETWEEN_LOOPS=20, DELAY_BETWEEN_STOPS=0.5

# manually set DELAY_BETWEEN_LOOPS and DELAY_BETWEEN_STOPS
python3 start.py 20 1
[INFO]: DELAY_BETWEEN_LOOPS=20, DELAY_BETWEEN_STOPS=1
``` 
