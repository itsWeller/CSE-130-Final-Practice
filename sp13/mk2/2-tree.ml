type 'a tree =
  | Empty
  | Node of 'a * 'a tree list;;

let rec zip l1 l2 =
  match (l1,l2) with
  | ([],[]) -> []
  | (h1::t1, h2::t2) -> (h1,h2)::(zip t1 t2);;

let rec tree_zip t1 t2 =
  match (t1,t2) with
  | (Empty,Empty) -> Empty
  | (Node(a,l1),Node(b,l2)) -> 
      let node_list = zip l1 l2 in
      let tree_list = List.map(fun (x,y) -> tree_zip x y) node_list in
      Node((a,b),tree_list);;

let t1 = Node(1,[Node(2, []); Node(3, [])]);;
let t2 = Node(4,[Node(5, []); Node(6, [])]);;
tree_zip t1 t2;;
