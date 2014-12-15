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
      | (Const(a),Const(b)) -> Const(a+b)
      | _ -> Plus(e1',e2'))
  | _ -> e

simpl (Plus (Const 4, Const 7));;
simpl (Plus (Plus (Const 20, Const 10), Var "a"));;
simpl (Plus (Plus (Const 4, Const 10), Const 7));;
simpl (Plus (Const 4, Var "a"));;
simpl (Plus (Var "a", Var "b"));;
simpl (Plus (Plus (Var "a", Const 10), Const 7));;


