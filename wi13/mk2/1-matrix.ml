let sum_matrix l =
  let sum_list m = List.fold_left(fun a b -> a + b) 0 m in
  List.fold_left(fun a b -> a + sum_list b) 0 l;;

sum_matrix( [[ 1; 2; 3 ]; [ 4; 5; 6 ]]);;
sum_matrix( [[ 1; 2 ]; [ 4; 5 ]]);;
