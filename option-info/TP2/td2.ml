
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

let rec reverse_aux ch = match ch with
  | "" -> ""
  | ch -> String.concat "" [(reverse_aux (String.sub ch 1 (String.length(ch)-1))); (String.make 1 ch.[0])];;

(*print_string(reverse_aux "1234");; *)

let reverse n =
  let ch = string_of_int(n) in
  int_of_string(reverse_aux(ch));;

(* print_int(reverse 1234);; *)

let palindrome n = (reverse n = n);;

let rec miroir l1 l2 = match l1 with
| [] -> l2
| x::q -> miroir q (x::l2);;

let miroir_final l = miroir l [];;

let miroir2 l =
  let x1 = ref l and x2 = ref [] in
  while !x1 <> [] do
    x2:=(List.hd !x1)::!x2;
    x1:=List.tl !x1
  done;
  x2;;

let rec concat1 l1 list2 = match l1 with (* récurrence non termiale *)
  | []-> l1
  | hd :: tl -> hd :: (merge tl l2);;

let rec concat2 l1 l2 f = match (l1, l2) with
  | [], [] -> miroir_final f
  | x::q, _ -> concat2 q l2 (x::f)
  | _, x::q -> concat2 l1 q (x::f);;

let concat2_final l1 l2 = concat2 l1 l2 [];;

let concat3 l1 l2 =
  let x1 = ref l1 and x2 = ref l2 and x3 = ref [] in
  while !x1 <> [] do
    x3:=(List.hd !x1)::!x3;
    x1:=List.tl !x1
  done;
  while !x3 <> [] do
    x2:=(List.hd !x3)::!x2;
    x3:=List.tl !x3
  done;
  !x2;;

let rec long n l = match l with
    | [] -> n
    | x::q -> long (n+1) q;;

let long_final l = long 0 l;;

let long2 l =
    let x = ref l and n = ref 0 in
    while !x <> [] do
      n:=!n+1;
      x:=List.tl !x
    done;
    !n;;

let rec maximum n l = match l with
  | [] -> n
  | x::q -> if (x>=n) then (maximum x q) else (maximum n q);;

let maximum_final l = maximum (List.hd l) (List.tl l);;

let maximum2 l = 
  let n = ref (List.hd l) and x = ref (List.tl l) in
  while !x <> [] do
    let p = (List.hd !x) in
      if (p>= (!n)) then 
        n:=p
      else ();
      x:=List.tl !x
  done;
  !n;;

let find n l = 
    let c = ref 0 and x = ref l in
    while !c <> n do
        c:=!c+1;
        x:=List.tl !x
    done;
    (List.hd !x);;  

let rec find1 c n l = if (c=n) then (List.hd l) else (find1 (c+1) n (List.tl l));;

let find1_final n l = find1 0 n l;;

let insert n e l =
  (* On inverse la liste et récupère la longueur *)
  let xa = ref l and xb = ref [] and length = ref 0 in
  while !xa <> [] do
    xb:=(List.hd !xa)::!xb;
    xa:=List.tl !xa;
    length:=!length +1
  done;
  let c = ref 0 and x = ref [] in
  (* On vide jusqu'à n *)
  let maximum = - n + !length in
  while !c <> maximum do
    x:=(List.hd !xb)::!x;
    xb:=List.tl !xb;
    c:=!c+1
  done;
  (* On ajoute l'élément *)
  xb:=e::!xb;
  (* On rajoute le reste de la liste *)
  while !xb <> [] do
    x:=(List.hd !xb)::!x;
    xb:=List.tl !xb
  done;
  !x;;

let delete n l =
  (* On inverse la liste et récupère la longueur *)
   let xa = ref l and xb = ref [] and length = ref 0 in
   while !xa <> [] do
     xb:=(List.hd !xa)::!xb;
     xa:=List.tl !xa;
     length:=!length +1
   done;
   let c = ref 0 and x = ref [] in
   (* On vide jusqu'à n - 1 *)
   let maximum = - 1 - n + !length in
   while !c <> maximum do
     x:=(List.hd !xb)::!x;
     xb:=List.tl !xb;
     c:=!c+1
   done;
   (* On supprime l'élément *)
   xb:=List.tl !xb;
   (* On rajoute le reste de la liste *)
   while !xb <> [] do
     x:=(List.hd !xb)::!x;
     xb:=List.tl !xb
   done;
   !x;;