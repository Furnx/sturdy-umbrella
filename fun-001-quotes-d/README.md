# fun-001-quotes - Quote System & File Operations

In this assessment you will be required to complete the Python functions as detailed. The assessment focuses on:

- Functions
- Basic loops
- Processing data
- Basic error handling
- Simple algorithms (Problem solving)


## Project Structure

```
fun-001-quotes-b/
├── quote_system.py      # Your implementation goes here
├── quotes.txt           # Sample quotes file
└── tests/
    └── test_quotes.py   # Sample tests
```

## Instructions

### Complete the Functions

- `ask_file_name(user_input: str or None) -> str` - Handle file name selection based on user input

- `read_file(file_name: str) -> str` - Open and read file content with proper error handling

- `select_random_quotee(quotees_list: list) -> str` - Randomly select a quotee from the provided list

- `find_quote(quotee_name: str, quotes_list: list) -> str` - Search for a specific quotee's quote in the quotes list

- `final_output(quote_string: str, quotee_name: str) -> None` - Format and display the final quote output

Each function has detailed requirements and examples in its docstring. Read the docstrings carefully - they contain all the information you need to implement the solutions correctly.

---

### Test Your Implementation

#### Sample Tests (For Guidance)

The tests/test_quotes.py file contains basic sample tests to help you understand the expected behavior:

```bash
# Run all sample tests
python3 -m unittest tests/test_quotes.py

# Run a specific test (example)
python3 -m unittest tests.test_quotes.TestQuoteSystemSample.test_ask_file_name
```

Note: These sample tests are for your guidance only. Do NOT modify them.

### Comprehensive Hidden Tests

This will test your implementation against many more test cases and provide detailed feedback on your solution.

NB: You can run(copy and paste) the following commands on your terminal to run our hidden tests against your implementation

```bash
# Run this only once
chmod +x .lms/run_hidden.sh 
```

```bash
# You can run this every time you want to test against the hidden tests
.lms/run_hidden.sh   
```
