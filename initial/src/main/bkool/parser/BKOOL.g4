grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: classdecl* EOF;

//Class declaration
classdecl: CLASS ID (EXTENDS ID)? LP memberdecl* RP;
memberdecl:  attributedecl | methoddecl;

//Attribute declaration
attributedecl: vardecl | constdecl;
vardecl: STATIC? typ attrlist SEMI;
typ: INT | FLOAT | BOOLEAN | STRING | ID | arraytype;
attrlist: attrname subattrlist;
attrname: ID INITASSIGN expr | ID;
subattrlist: COMMA attrname subattrlist | ;

constdecl: FINAL typ constattrlist SEMI | FINAL STATIC typ constattrlist SEMI | STATIC FINAL typ constattrlist SEMI;
constattrlist: constattr subconstattrlist;
constattr: ID INITASSIGN expr;
subconstattrlist: COMMA constattr subconstattrlist | ;

//Method declaration
methoddecl: staticmethods | instancemethods;
staticmethods: STATIC returntype ID LB paramlist? RB blockstmt;
instancemethods: returntype? ID LB paramlist? RB blockstmt;
paramlist: param subparamlist;
subparamlist: SEMI param subparamlist | ;
param: typ ID idlist;
returntype: typ | VOID;
idlist: COMMA ID idlist | ;

//Statement
//Block statement
blockstmt: LP stmtlist RP;
stmtlist: stmt stmtlist | ;
stmt: attributedecl | assignstmt | ifstmt | forstmt | breakstmt | continuestmt | returnstmt | expr SEMI;
assignstmt: lhs ASSIGN expr SEMI;
forstmt: FOR scalarvar ASSIGN expr (TO | DOWNTO) expr DO (stmt | ifstmt);
ifstmt: IF expr THEN stmt (ELSE stmt)? | blockstmt;
breakstmt: BREAK SEMI;
continuestmt: CONTINUE SEMI;
returnstmt: RETURN expr SEMI;

//Expression
expr: expr OP0 expr1 | expr1;
expr1: expr1 OP1 expr2 | expr2;
expr2: expr3 OP2 expr3 | expr3;
expr3: expr4 OP3 expr4 | expr4;
expr4: expr4 OP4 expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: expr6 CONCAT expr7 | expr7;
expr7: expr8 LSB expr RSB | expr8;
expr8: expr8 DOT ID | expr8 DOT ID LB exprlist RB | expr9;
expr9: NEW ID LB exprlist RB | expr10;
expr10: LP exprlist RP | expr11;
expr11: LB expr RB | expr12;
expr12: OP0 expr12 | operands;
operands: THIS | INTLIT | FLOATLIT | TRUE | FALSE | NIL | ID | STRLIT;
exprlist: expr argumentslist | ;
fieldaccess: expr DOT ID | expr DOT ID LB exprlist RB | ID DOT ID | ID DOT ID LB exprlist RB;
argumentslist: COMMA expr argumentslist | ;

scalarvar: ID;
lhs: ID | arraycell | fieldaccess;
arraycell: expr LSB expr RSB;
arraytype: (FLOAT | INT | BOOLEAN | STRING | ID) LSB INTLIT RSB;
attributeinstancedecl: typ attrlist SEMI | FINAL typ constattrlist SEMI ;
literallist: literal subliterallist | ;
literal: FLOATLIT | INTLIT | TRUE | FALSE | NIL | STRLIT | THIS;
subliterallist: COMMA literal subliterallist | ;
//KEYWORD
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INT: 'int';
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';
//Operator
OP0: '+' | '-';
OP1: '*' | '/' | '\\' | '%';
OP2: '==' | '!=';
OP3: '>' | '>=' | '<' | '<=';
OP4: '&&' | '||';
NOT: '!';
CONCAT: '^';
ASSIGN: ':=';
INITASSIGN: '=';
//Separator
LB: '('; RB: ')';
LSB: '['; RSB: ']';
LP: '{'; RP: '}';
SEMI: ';';
CL: ':';
DOT: '.';
COMMA: ',';
//Literal
INTLIT: [0-9]+;
FLOATLIT: INTLIT '.' [0-9]* EXPONENT? | INTLIT EXPONENT;
STRLIT: '"' CHARACTERS? '"';

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines
COMMENT: '/*' .*? '*/' -> skip;
LINECOMMENT: '#' ~[\r\n\f]* -> skip;

fragment EXPONENT: [eE][+-]? [0-9]+;
fragment ESC: '\\' [bfrnt"\\];
fragment NONEESC: '\\' ~[bfrnt"\\];
fragment CHARACTERS: (~["\\\r\n\f] | ESC)*;
//Identifier
ID: [_a-zA-Z][_a-zA-Z0-9]*;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' CHARACTERS {raise UncloseString(self.text)};
ILLEGAL_ESCAPE: '"' CHARACTERS? NONEESC {raise IllegalEscape(self.text)};