
open Printf

(* Exo 1 *)

let rec bin n = match n with
  | 0 -> []
  | _ -> bin(n/2) @ [n mod 2];;


(* List.iter(printf "%d ") (bin 6);; *)


let rec bin2 n = match n with
  | 0 -> []
  | _ -> n mod 2 :: bin(n/2);;

(* List.iter(printf "%d ") (List.rev(bin2 6));; *)

let rec bin3_h l n = match n with 
| 0 -> l
| _ -> bin3_h (n mod 2 :: l) (n / 2);;

let bin3 = bin3_h [];;

(* List.iter(printf "%d ") (bin3 6);; *)