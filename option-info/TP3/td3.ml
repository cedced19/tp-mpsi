(*Ex 2*)
let rec produit n l = match l with
  | [] -> n
  | x::q -> produit (n*x) q;;

let produit_final l = produit 0 l;;

(*Ex 3*)
let rec double lo l = match l with
  | [] -> lo
  | x::q -> double (x::x::lo) q;;

let double_final l = produit [] l;;

(*Ex 4*)
let rec avantdernier l = match l with
| [] -> failwith "liste de moins de deux éléments"
| [a] -> failwith "liste de moins de deux éléments"
| (a::[b]) -> a
| a::q -> avantdernier q;;

(*Ex 6*)
let rec somme l1 l2  = match (l1, l2) with
| [], _ -> []
| _, [] -> []
| y::p, x::q -> (y+x)::(somme p q);;

(*Ex 7*)
type 'a monome = int*'a;;
type 'a polynome = ('a monome) list;;

let p1=[(0,9);(3,8);(102,5)];;
let p2=[(0,7);(3,-8);(7,9)];;

let rec addpoly p1 p2 = match (p1, p2) with
  | [], _ -> []
  | _, [] -> []
  | ((a,b)::q), ((e,f)::p) when (a>e) -> (e,f)::(addpoly q p2)
  | ((a,b)::q), ((e,f)::p) when (e>a) -> addpoly p2 p1
  | ((a,b)::q), ((e,f)::p) when (a=e) -> if b+.f =0. then addpoly q p else (a,f+.b)::(addpoly q p);;


let rec prodmon m1 p2 = match (m1, p1) with
  | _, [] -> []
  | (a,b), ((e,f)::q) -> (a*.b,e*.f)::(prodmon m1 q);;

let rec prodpoly p1 p2 = match (p1, p2) with
  | _, [] -> []
  | [], _ -> []
  | m::q, _ -> addpoly (prodmon m p2) (addpoly q p2);;

let rec derive p= match p with
 | [] -> []
 | (d,a)::q -> (d-1,(float_of_int d) * a)::derive q;;

(*Ex 10*)
let rec takewhile p s = match p(List.hd s) with
  |true -> (List.hd s) :: (takewhile p (List.tl s))
  |false -> [];;

let rec dropewhile p s = match p(List.hd s) with
  |true -> dropewhile p (List.tl s)
  |false -> List.tl s;;

let appl p l = List.for_all p (takewhile p l);;

(* s = dropewhile p s "+" takewhile p s  *)