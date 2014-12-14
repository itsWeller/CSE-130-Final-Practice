zip([],[],[]).
zip([H1|T1],[H2|T2],[[H1,H2]|Z]) :- zip(T1,T2,Z).
