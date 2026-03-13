grammar Calculadora;

prog: expresion EOF ;

expresion : expresion ('*'|'/') expresion   # MultDiv
          | expresion ('+'|'-') expresion   # AddSub
          | '(' expresion ')'               # Parentesis
          | NUMBER                          # Numero
          ;

NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;
