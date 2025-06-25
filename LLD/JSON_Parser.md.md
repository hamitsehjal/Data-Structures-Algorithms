1. Define the Input and Output at each stage - *lexer* and *parser*
	- Input Raw String: `{"name": "hamit", "values": [1, 2, 3]}1`
	- Lexer:
		- Ouput:
					```
					[
			    Token(type='LEFT_BRACE', value='{'),
			    Token(type='STRING', value='name'),
			    Token(type='COLON', value=':'),
			    Token(type='STRING', value='hamit'),
			    Token(type='COMMA', value=','),
			    Token(type='STRING', value='values'),
			    Token(type='COLON', value=':'),
			    Token(type='LEFT_BRACKET', value='['),
			    Token(type='NUMBER', value='1'),
			    Token(type='COMMA', value=','),
			    Token(type='NUMBER', value='2'),
			    Token(type='COMMA', value=','),
			    Token(type='NUMBER', value='3'),
			    Token(type='RIGHT_BRACKET', value=']'),
			    Token(type='RIGHT_BRACE', value='}')
]
					```
	- Parser:
		- Output: Boolean (valid/invalid) + error message if invalid

2. For Parser:
	- Started with bracket matching algorithm (uses stack) - won't scale beyond matching brackets
	- what do we need to validate?
		- After this `{` bracket, we need to have a **String** key
		- After String Key, we need to have a **Colon**
		- After Colon, we need to have a value of one of the following types - (Number, String, boolean, Array, Object, Null)
		- Array elements are seperated by commas
		- Object key-value pairs are seperated by commas

Json Grammer Rules:
- a `LEFT_BRACE` needs to be either followed by a `RIGHT_BRACE` or a String Key
- After a string key, we need to have a Colon
- 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NzUyMTE1OTQsNjQ3MjAxMDE1LC0yMD
cwMTk1OTgzXX0=
-->