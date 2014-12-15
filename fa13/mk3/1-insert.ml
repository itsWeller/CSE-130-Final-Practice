let rec insert l i =
  match l with
  | [] -> [i]
  | h::t -> if h > i then i :: h :: t else h :: (insert t i);;

let insertion_sort = fun l -> List.fold_left(fun a b -> insert a b) [] l;;

