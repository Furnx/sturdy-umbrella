# fun-000-syntax - Python Fundamentals & Problem Solving

In this assessment you will be requred to complete the python probelms as detailed. The assessment focuses on:

- String Manipulation
- Number Processing
- Logical Operations
- TDD (Test-Driven Development)

## Project Structure

```
fun-000-syntax-b/
├──fundamentals.py #Your implementation goes here
└── tests/
    └── test_fundamentals.py  #Sample tests

```
## Instructions

###  Complete the Functions

- `get_date_of_birth(id_number:str)->str` - Extract date of birth from South African ID number

- ``get_gender(id_number:str)->str`` - Determine gender from South African ID number

- ``get_citizenship(id_number:str)->str`` - Determine citizenship status from South African ID number

- ``fizzbuzz(n:int)->None:`` - Implement the classic FizzBuzz problem

- ``check_weirdness(n:int)->str`` - Classify numbers based on specific weirdness rules

Each function has detailed requirements and examples in its docstring. Read the docstrings carefully - they contain all the information you need to implement the solutions correctly.

---

### Test Your Implementation

#### Sample Tests (For Guidance)

The tests/test_fundamentals.py file contains basic sample tests to help you understand the expected behavior:

```bash
# Run all sample tests
python3 -m unittest tests/test_fundamentals.py

# Run a specific test (example)
python3 -m unittest tests.test_fundamentals.TestFundamentals.test_get_date_of_birth
```

Note: These sample tests are for your guidance only. Do NOT modify them.

### Comprehensive Hidden Tests

This will test your implementation against many more test cases and provide detailed feedback on your solution.

NB: You can run(copy and paste) the following commands on your terminal to run our hidden tests against your implementation

```bash
#Run this only once
chmod +x .lms/run_hidden.sh 
```

```bash
#You can run this every time you want to test against the hidden tests
.lms/run_hidden.sh   
```
