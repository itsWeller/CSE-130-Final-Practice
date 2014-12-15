remove_all(_,[],[]).
remove_all(X,[X|T],R) :- remove_all(X,T,R).
remove_all(X,[H|T],[H|R]) :- remove_all(X,T,R), not(X=H).

prefix([],_).
prefix([H1|T1],[H1|T2]) :- prefix(T1,T2).

segment(L1,L2) :- prefix(L1,L2).
segment([H1|T1],[H1|T2]) :- prefix(T1,T2).
