let rec insert l i = 
  match l with
  | [] -> [i]
  | h::t -> if h > i then i :: h :: t else h :: (insert t i);;

insert [] 10;;
insert [1;2;3;4] 3;;
insert [10;15;20;30] 40;;
insert [10;15;20;30] 5;;

let insertion_sort = fun l ->
  List.fold_left(fun a b -> insert a b) [] l;;

insertion_sort [1;5;2;3;4;-1;22];;

