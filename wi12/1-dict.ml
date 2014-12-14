let prices = [ ("Baseball Bat", 20); ("Soccer Ball", 10); ("Tennis Racket", 40) ];;
let rec find d k =
  match d with
  | [] -> raise Not_found
  | (k',v') :: t -> if k' = k then v' else find t k

let rec add d k v =
  match d with
  | [] -> [(k,v)]
  | (k',v') :: t -> if k' == k then (k',v)::t else
    if k' > k then (k,v)::d else (k',v')::(add t k v)

let keys d = List.map(fun (k,v) -> k) d;;
let values d = List.map(fun (k,v) -> v) d;;

let key_of_max_val d = 
  match d with
  | [] -> raise Not_found
  | h::t -> List.fold_left(fun (k',v') (k,v) -> if v > v' then (k,v) else (k',v')) ("",-1) d;;


