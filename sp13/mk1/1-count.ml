let count f l = List.fold_left(fun a b -> if (f b) then a + 1 else a) 0 l;;
count ((=) 7) [1;2;3;4;5;6;7;8;9];; (*1*)
count ((!=) 8) [1;2;3;4;5;6;7;8;9];; (*8*)
count ((<) 3) [1;2;3;4;5;6;7;8;9];; (*6*)
count ((>=) 2) [1;2;3;4;5;6;7;8;9];; (*2*)
count (fun x -> x mod 2 = 0) [1;2;3;4;5;6;7;8;9];; (*4*)

let stretch l = List.fold_left(fun a b -> a @ [b] @ [b]) [] l;;
stretch [1;2;3;4];;
stretch ["a";"b";"c"];;
stretch [0;0;1];;

