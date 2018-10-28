table(A):- printt(A,10).
printt(A,0):-
write('Aish').
printt(A,B):-
D is B - 1,
C is 10 - D,
E is A * C,
write(A),
write("*"),
write(C),
write("="),
write(E),
nl,
printt(A,D).