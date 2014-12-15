type expr = 
  | Var of string
  | Const of int
  | Plus of expr * expr;;

let rec simpl e = 
  match e with
  | Plus(e1,e2) ->
      let e1' = simpl e1 in
      let e2' = simpl e2 in
      (match (e1',e2') with
      | (Const a, Const b) -> Const(a+b)
      | _ -> Plus(e1',e2'))
  | _ -> e;;

simpl (Plus (Plus (Const 20, Const 10), Var "a"));;


