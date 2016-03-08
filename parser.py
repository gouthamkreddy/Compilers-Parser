import yacc
import pprint
from lexer import tokens, lexer
from helper import dump
def p_start(p):
    '''start : block
        | statements'''
            pprint.pprint(p.slice)

def p_block(p):
    '''block : LEFTBRACE statements RIGHTBRACE
        | LEFTBRACE RIGHTBRACE'''
            pprint.pprint(p.slice)

def p_statements(p):
    '''statements : statement SEMICOLON statements
        | statement'''
            pprint.pprint(p.slice)

def p_statement_semicolon(p):
    '''statement : assignment SEMICOLON '''
        pprint.pprint(p.slice)
# | declaration SEMICOLON
# | reassignment SEMICOLON
# | BREAK SEMICOLON
# | CONTINUE SEMICOLON
# | RETURN expression SEMICOLON
# | PRINT LEFTPAREN expression RIGHTPAREN SEMICOLON
# | functioncall SEMICOLON '''

# def p_statement_no_semicolon(p):
# 	'''statement : ifthen
# 				 | ifthenelse
# 				 | while
# 				 | for
# 				 | funcdecl'''

def p_assignment(p):
    '''assignment : VAR assignlist'''
        pprint.pprint(p.slice)

def p_assignlist(p):
    '''assignlist : ID EQ expression COMMA assignlist
        | ID EQ expression'''
            pprint.pprint(p.slice)

def p_declaration(p):
    '''declaration : VAR ID COMMA declList
        | VAR ID'''
            pprint.pprint(p.slice)

def p_declList(p):
    '''declList : ID COMMA declList
        | ID'''
            pprint.pprint(p.slice)

def p_reassignment(p):
    '''reassignment : ID EQ expression
        | ID PLUSEQ expression
        | ID MINUSEQ expression
        | ID INTOEQ expression
        | ID DIVEQ expression
        | ID INCR
        | ID DECR
        | ID LSHIFTEQ expression
        | ID RSHIFTEQ expression
        | ID URSHIFTEQ expression
        | ID ANDEQ expression
        | ID OREQ expression
        | ID XOREQ expression
        | ID MODEQ expression'''

# Precedence of Operators
precedence = (
              ('left', 'OR'),
              ('left', 'AND'),
              ('left', 'DOUBLEEQ', 'NOTEQUAL', 'STREQUAL', 'STRNEQUAL'),
              ('left', 'LT', 'GT', 'LTE', 'GTE'),
              ('left', 'PLUS', 'MINUS'),
              ('left', 'INTO', 'DIVIDE', 'MOD'),
              ('right', 'NOT'),
              )

def p_expression_op(p):
    '''expression : expression PLUS expression
        | expression MINUS expression
        | expression INTO expression
        | expression DIVIDE expression
        | expression MOD expression'''
            pprint.pprint(p.slice)

def p_groupExp(p):
    '''expression : LEFTPAREN expression RIGHTPAREN'''
        '''expression : NOT expression'''

def p_expression_binop(p):
    '''expression : expression BINAND expression
        | expression BINOR expression
        | expression BINXOR expression
        | expression BINNOT expression
        | BINNOT expression'''

def p_expression_relop(p):
    '''expression : expression LT expression
        | expression GT expression
        | expression DOUBLEEQ expression
        | expression NOTEQUAL expression
        | expression LTE expression
        | expression GTE expression
        | expression STREQUAL expression
        | expression STRNEQUAL expression
        | expression AND expression
        | expression OR expression'''

def p_expression_shift(p):
    '''expression : expression LSHIFT expression
        | expression RSHIFT expression
        | expression URSHIFT expression'''



def p_expression(p):
    '''expression : basicTypes'''
        pprint.pprint(p.slice)

def p_basicTypes(p):
    '''basicTypes : NUMBER
        | STRING
        | ID'''
            pprint.pprint(p.slice)



# Error rule for syntax errors
def p_error(p):
    pprint.pprint(p)
        print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = raw_input('calc > ')
        except EOFError:
            break
        if not s: continue
        print s
        result = parser.parse(s, lexer=lexer)
    print result

