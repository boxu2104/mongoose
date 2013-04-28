# It's useful for debugging and error output to keep the *values* of these vtypes as strings.

# Keywords
INT_KEYWORD = "INT_KEYWORD"
FLOAT_KEYWORD = "FLOAT_KEYWORD"
STRING_KEYWORD = "STRING_KEYWORD"
BOOLEAN_KEYWORD = "BOOLEAN_KEYWORD"
RETURN_STATEMENT = "RETURN_STATEMENT"

# Arithmetic
ADD = "ADD"
SUBTRACT = "SUBTRACT"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
UMINUS = "UMINUS"
MODULUS = "MODULUS"
POWER = "POWER"

# Basic types
INTEGER_VALUE = "INTEGER_VALUE"
FLOAT_VALUE = "FLOAT_VALUE"
BOOLEAN_VALUE = "BOOLEAN_VALUE"
NONE_VALUE = "NONE_VALUE"
STRING_VALUE = "STRING_VALUE"

# Boolean operators
OR = "OR"
AND = "AND"
NOT = "NOT"

# String operators
CONCATENATE = "CONCATENATE"

# Equality
EQUAL = "EQUAL"
NOT_EQUAL = "NOT_EQUAL"

# Relational
LESS_THAN = "LESS_THAN"
GREATER_THAN = "GREATER_THAN"
LESS_THAN_EQUAL = "LESS_THAN_EQUAL"
GREATER_THAN_EQUAL = "GREATER_THAN_EQUAL"

#Control Flow
WHILE = "WHILE"
IF = "IF"
ELIF = "ELIF"
ELSE = "ELSE"
PIF = "PIF"
PELIF = "PELIF"
PELSE = "PELSE"

#List
LIST_TYPE = "LIST_TYPE"
BRACKET_DECL = "BRACKET_DECL"
BRACKET_ACCESS = "BRACKET_ACCESS" #used for LHS assignment or RHS access. x[3] = y or x = y[3]

#BLOCK KEYWORDS
ENVIRONMENT = "ENVIRONMENT"
POPULATE = "POPULATE"
ACTION = "ACTION"

#WEIGHTED VALUE
WEIGHTED_VALUE_STAT = "WEIGHTED_VALUE_STAT"
WEIGHTED_VALUE_CLAUSE = "WEIGHTED_VALUE_CLAUSE"

# FUNCTIONS
FORMAL_PARAM = "FORMAL_PARAM" #type with empty brackets
FORMAL_PARAM_LIST = "FORMAL_PARAM_LIST"
BRACKET_FORMAL_PARAM_OR_RETURN_TYPE = "BRACKET_FORMAL_PARAM_OR_RETURN_TYPE" #empty brackets
FUNCTION = "FUNCTION"
RETURN_TYPE = "RETURN_TYPE"
ACTUAL_PARAM_LIST = "ACTUAL_PARAM_LIST"


# Other
ASSIGNMENT = "ASSIGNMENT"
IDENTIFIER = "IDENTIFIER"
DECLARATION = "DECLARATION"
DECLARATION_ASSIGNMENT = "DECLARATION_ASSIGNMENT"
STATEMENT_LIST = "STATEMENT_LIST"
STATEMENT = "STATEMENT"
PROGRAM = "PROGRAM"
#EPSILON_STAT = "EPSILON_STAT" #blank statement
