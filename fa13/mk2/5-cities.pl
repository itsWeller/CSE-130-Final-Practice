link(san_diego, seattle).
link(seattle, dallas).
link(dallas, new_york).
link(new_york, chicago).
link(new_york, seattle).
link(chicago, boston).
link(boston, san_diego).

path(A,B) :- path_helper(A,B,[A]).
path_helper(A,B,Seen):-link(A,B),not(member(B,Seen)).
path_helper(A,B,Seen):-
  link(A,C),
  not(memeber(C,Seen)),
  path_helper(A,C,[C|Seen]).

   
