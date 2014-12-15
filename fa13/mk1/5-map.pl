link(san_diego, seattle).
link(seattle, dallas).
link(dallas, new_york).
link(new_york, chicago).
link(new_york, seattle).
link(chicago, boston).
link(boston, san_diego).

path_2(A,B):-link(A,C),link(C,B).
path_3(A,B):-link(A,C),link(C,D),link(D,B).

path_N(A,B,N):-N=1,link(A,B).
path_N(A,B,N):-N>1,link(A,C),N1 is N-1,path_N(C,B,N1).

path(A,B):-path_helper(A,B,[A|[]]).
path_helper(A,B,Seen):- link(A,B),not(member(B,Seen)).
path_helper(A,B,Seen):-
  link(A,C),
  not(member(C,Seen)),
  path_helper(C,B,[C|Seen]).
