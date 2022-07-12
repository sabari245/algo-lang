
# ALGO LANG
This was an attempt to create an AI-based Programming language that lets you write code in human language. This is powered by **GPT-3**, **Rust Lang** and **Python**

## Installation Instructions
1. install rust from [rust-lang.org](https://www.rust-lang.org/)
2. create an account in [openai.com/api](https://openai.com/api/)
3. you can find your API Key at [beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys)
4. clone this github repo
5. install the requirements with `python3 -m pip install -r requirements.txt`
6. create a file named `.env` and write `OPENAI_API_KEY=<YOUR API KEY>`
7. write your algorithm in a file with `.algo` extensions
8. to run the program execute `python3 algo.py <filename>.algo`
9. now a rust file will be created you can which can be compiled and executed
### info
* The length of the created program cannot exceed 1024 characters
* The instructions in the algorithm should be precise
* Try to enclose variable and function names in quotes
* Open AI doesn't give the API key for free but it'll give you $18 free credit for a period of 3 months