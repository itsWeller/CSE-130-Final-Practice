let rec insert l i = 
  match l with
  | [] -> [i]
  | h::t -> if (h < i) then h :: insert t i else i :: h :: t;;

let insertion_sort = fun l ->
  List.fold_left(fun a b -> insert a b) [] l;;

insertion_sort [2;4;8;1;-2;11];;

type expr =
| Var of string
| Const of int
| Plus of expr * expr;;

let rec simpl e =
  match e with
  | Plus (e1,e2) ->
      let e1' = simpl e1 in
      let e2' = simpl e2 in
      match (e1',e2') with
      | (Const a,Const b) -> Const(a+b)
      | _ -> Plus(e1',e2')
  | _ -> e

let count f l = List.fold_left(fun a b -> if (f b) then a + 1 else a) 0 l;;
count ((=) 7) [1;2;3;4;5;6;7;8;9];;

let stretch l = List.fold_left(fun a b -> a@b::[b]) [] l;;

(* QUESTION 2 IS FUCKING HARD*)

let sum_matrix l = 
  let sum_list n = List.fold_left(fun a b -> a + b) 0 n in 
  List.fold_left(fun a b -> a + (sum_list b)) 0 l

sum_matrix [[ 1; 2; 3];
         [ 4; 5; 6]];;

