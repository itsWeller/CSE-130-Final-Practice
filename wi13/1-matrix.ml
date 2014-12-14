let sum_matrix l =
  let sum_list m = List.fold_left(fun a b -> a+b) 0 m in
  List.fold_left(fun a b -> a + (sum_list b)) 0 l;;
