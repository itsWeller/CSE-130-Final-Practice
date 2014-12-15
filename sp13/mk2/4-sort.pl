part([],_,[],[]).
part([H1|T1],P,[H1|T2],R) :- H1 =< P, part(T1,P,T2,R).
part([H1|T1],P,R,[H1|T3]) :- H1 > P, part(T1,P,R,T3).

qsort([],[]).
qsort([H|T],R) :- part(
