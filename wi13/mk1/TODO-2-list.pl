prefix([],_).
prefix([H1|T1],[H1|T2]) :- prefix(T1,T2).
