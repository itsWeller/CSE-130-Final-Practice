let rec insert l i =
  match l with
  | [] -> [i]
  | h::t -> if h < i then h :: insert t i else i :: h :: t;;

let insertion_sort = fun l -> List.fold_left(fun a b -> insert a b) [] l;;

insertion_sort [2;4;1;2;6;6;9;11;0];;
