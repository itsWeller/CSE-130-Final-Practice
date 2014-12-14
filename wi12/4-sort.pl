sorted([]).
sorted([_]).
sorted([A,B|T]) :- A=<B,sorted([B|T]).

sort2(L1,L2) :- permutation(L1,L2), L2 = sorted(L2).
