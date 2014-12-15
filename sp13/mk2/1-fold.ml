let count f l = List.fold_left(fun a b -> if f b then a + 1 else a) 0 l;;
let stretch l = List.fold_left(fun a b -> a@[b;b]) [] l;;

