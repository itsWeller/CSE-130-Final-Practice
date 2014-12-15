sat(var(X)) :- X = 1.
sat(not(var(X))) :- X = 0.

sat(and([])).
sat(and([X|Tail])) :- sat(var(X)),sat(and([Tail])).
sat(or([])):- fail.
