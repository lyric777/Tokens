# JavaScript: Comments & Keywords
#
# In this exercise you will write token definition rules for all of the
# tokens in our subset of JavaScript *except* IDENTIFIER, NUMBER and
# STRING. In addition, you will handle // end of line comments
# as well as /* delimited comments */. 
#
# We will assume that JavaScript is case sensitive and that keywords like
# 'if' and 'true' must be written in lowercase. There are 26 possible
# tokens that you must handle. The 'tokens' variable below has been 
# initialized below, listing each token's formal name (i.e., the value of
# token.type). In addition, each token has its associated textual string
# listed in a comment. For example, your lexer must convert && to a token
# with token.type 'ANDAND' (unless the && is found inside a comment). 
#
# Hint 1: Use an exclusive state for /* comments */. You may want to define
# t_comment_ignore and t_comment_error as well. 

import ply.lex as lex

def test_lexer(lexer,input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result
  
tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
#       'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
#       'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
#       'STRING',       #### Not used in this problem. 
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

#注意顺序
states=(
    ('javascriptcomment','exclusive'),
)

def t_javascriptcomment(t):
    r'/\*'
    t.lexer.begin('javascriptcomment')

def t_javascriptcomment_end(t):
    r'\*/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    
def t_SLASHSLASH(t):
    r'//.*'
    pass

t_ignore = ' \t\v\r' # whitespace 
t_javascriptcomment_ignore = '\t\v\r'

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
        print "JavaScript Lexer: Illegal character " + t.value[0]
        t.lexer.skip(1)

def t_javascriptcomment_error(t):
    t.lexer.skip(1)

def t_ANDAND(t):
    r'&&'
    t.type = 'ANDAND'
    return t

def t_COMMA(t):
    r','
    t.type = 'COMMA'
    return t

def t_DIVIDE(t):
    r'\/'
    t.type = 'DIVIDE'
    return t

def t_ELSE(t):
    r'else'
    t.type = 'ELSE'
    return t

def t_EQUALEQUAL(t):
    r'=='
    t.type = 'EQUALEQUAL'
    return t

def t_EQUAL(t):
    r'='
    t.type = 'EQUAL'
    return t

def t_FALSE(t):
    r'false'
    t.type = 'FALSE'
    return t

def t_FUNCTION(t):
    r'function'
    t.type = 'FUNCTION'
    return t

def t_GE(t):
    r'>='
    t.type = 'GE'
    return t

def t_GT(t):
    r'>'
    t.type = 'GT'
    return t

def t_IF(t):
    r'if'
    t.type = 'IF'
    return t

def t_LBRACE(t):
    r'{'
    t.type = 'LBRACE'
    return t

def t_LE(t):
    r'<='
    t.type = 'LE'
    return t

def t_LPAREN(t):
    r'\('
    t.type = 'LPAREN'
    return t

def t_LT(t):
    r'<'
    t.type = 'LT'
    return t

def t_MINUS(t):
    r'-'
    t.type = 'MINUS'
    return t

def t_NOT(t):
    r'!'
    t.type = 'NOT'
    return t

def t_OROR(t):
    r'\|\|'
    t.type = 'OROR'
    return t

def t_PLUS(t):
    r'\+'
    t.type = 'PLUS'
    return t

def t_RPAREN(t):
    r'\)'
    t.type = 'RPAREN'
    return t

def t_RETURN(t):
    r'return'
    t.type = 'RETURN'
    return t

def t_RBRACE(t):
    r'}'
    t.type = 'RBRACE'
    return t

def t_SEMICOLON(t):
    r';'
    t.type = 'SEMICOLON'
    return t

def t_VAR(t):
    r'var'
    t.type = 'VAR'
    return t
    
def t_TRUE(t):
    r'true'
    t.type = 'TRUE'
    return t
    
def t_TIMES(t):
    r'\*'
    t.type = 'TIMES'
    return t
# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own. 

lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer(input1) == output1

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print test_lexer(input2) == output2
