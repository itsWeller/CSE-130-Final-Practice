type 'a tree =
| Empty
| Node of 'a * 'a tree list;;

let rec zip l1 l2 =
  match (l1,l2) with
  | ([],[]) -> []
  | (h1::t1, h2::t2) -> (h1,h2)::(zip t1 t2)
  | _ -> raise Exception

let rec tree_zip t1 t2 =
  match (t1,t2) with
  | (Empty,Empty) -> Empty
  | (Node(a1,l1),Node(a2,l2)) ->
      let node_pairs = zip l1 l2 in
      let comp_list = List.map(fun x -> tree_zip fst x, snd x) node_pairs in
      Node((a1,a2),comp_list)
  | _ -> failwith "Mismatch";;

let t1 = Node(1,[Node(2, []); Node(3, [])]);;
let t2 = Node(4,[Node(5, []); Node(6, [])]);;
tree_zip t1 t2;;

