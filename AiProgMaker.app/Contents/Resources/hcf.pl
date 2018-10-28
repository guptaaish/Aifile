hcf(A,B,HCF):-
A = B,
write('Aish'),
HCF is A.
hcf(A,B,HCF):-
A < B,
NB is B - A,
hcf(A,NB,HCF).
hcf(A,B,HCF):-
A > B,
NA is A - B,
hcf(NA,B,HCF).