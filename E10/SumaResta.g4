grammar SumaResta;

expr: NUM op NUM ;

op: '+' | '-' ;

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
