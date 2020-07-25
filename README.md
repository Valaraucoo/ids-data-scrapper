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
- Collected data will be stored in `Firebase`.
- You can also load `.csv` data to `Firebase` using `load_data_from_csv.py` (manual below).
----------------

You can change value of `LINE_NO`, `DELAY_BETWEEN_LOOPS` and `DELAY_BETWEEN_STOPS` with additional arguments in `start.py`.

Parameter  | Description
  ------------- | -------------
  `LINE_NO`  | Bus line number, it must be one value from the specified list (below).
  `DELAY_BETWEEN_LOOPS`  | Delay between execution of the query loop to the [TTSS](http://www.ttss.krakow.pl/).
  `DELAY_BETWEEN_STOPS`| Delay execution of the query between each stop per specified `LINE_NO`.

For more informations try `python3 start.py -h` or `python3 start.py --help`:

```
usage: start.py [-h] [-l LOOPS] [-s STOPS] line_number

positional arguments:
  line_number           Bus line number, it must be one value from the specified list.

optional arguments:
  -h, --help            show this help message and exit
  -l LOOPS, --loops LOOPS
                        Delay between execution of the query loop.
  -s STOPS, --stops STOPS
                        Delay execution of the query between each stop per specified line_number.
```
### Examples:
```bash
# default
python3 start.py 139
[INFO]: Line number: 139, loops delay: 5, stops delay: 0.5.

# manually set LINE_NO
python3 start.py 144
[INFO]: Line number: 144, loops delay: 5, stops delay: 0.5.

# manually set DELAY_BETWEEN_LOOPS
python3 start.py 159 -l 30
[INFO]: Line number: 159, loops delay: 30, stops delay: 0.5.

# manually set DELAY_BETWEEN_LOOPS and DELAY_BETWEEN_STOPS
python3 start.py 501 -l 30 --stops=2
[INFO]: Line number: 501, loops delay: 30, stops delay: 2.

python3 start.py 139 -loops=10 --stops=2
[INFO]: Line number: 139, loops delay: 10, stops delay: 2.
``` 
----------------
### Manual for `load_data_from_csv.py`

To load `.csv` data to `Firebase`'s database you can use `load_data_from_csv.py` sript. You can load data from any `.csv` files or directories.
```bash
python3 load_data_from_csv.py data_file.csv

python3 load_data_from_csv.py data_file_1.csv data_file_2.csv

python3 load_data_from_csv.py data_directory_1 data_directory_2 data_file_3.csv

python3 load_data_from_csv.py path/to/data_directory path/to/data_file.csv
```

----------------

### Parameters details

- Line number must be one of this: `['100', '101', '102', '103', '105', '189', '107', '109', '110', '742', '112', '113', '324', '117', '120', '122', '123', '124', '125', '127', '128', '129', '130', '131', '133', '106', '136', '578', '208', '209', '210', '211', '212', '213', '214', '215', '217', '218', '220', '221', '222', '223', '224', '225', '227', '229', '230', '232', '233', '235', '237', '238', '239', '240', '242', '243', '244', '245', '247', '248', '249', '250', '252', '253', '255', '257', '258', '259', '260', '263', '265', '267', '268', '269', '270', '273', '275', '277', '278', '280', '283', '285', '287', '297', '301', '304', '405', '422', '424', '451', '501', '502', '503', '572', '601', '605', '608', '610', '637', '642', '662', '664', '669', '902', '904', '271', '192', '160', '116', '469', '484', '537', '704', '264', '219', '274', '114', '134', '137', '138', '139', '141', '142', '143', '144', '149', '151', '152', '154', '158', '159', '162', '163', '164', '168', '169', '171', '172', '173', '174', '175', '178', '179', '181', '182', '183', '184', '193', '194', '201', '202', '203', '204', '207', '478', '111', '161', '722', '743', '234', '140', '352', '427', '773', '714', '176', '228', '135', '254', '156']`