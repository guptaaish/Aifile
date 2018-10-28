lcm(X1,X2):-
lcm(X1,X2,Y),
write(Y),
write('Aish'),
nl.

lcm(X1,X2,Y):-
gcd(X1,X2,Y1),
X3 is X1 * X2,
Y is X3/Y1.

gcd(X1,X2):-
gcd(X1,X2,Y),
write(Y),
nl.

gcd(X1,0,Y):-
Y is X1.

gcd(X1,X2,Y):-
X1 = X2,
Y is X2. 

gcd(X1,X2,Y):-
X1 < X2,
gcd(X2,X1,Y).

gcd(X1,X2,Y):-
X3 is mod(X1,X2),
gcd(X2,X3,Y).
