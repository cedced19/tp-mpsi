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
  | (a,b), ((e,f)::q) -> (a+e,b*.f)::(prodmon m1 q);;

let rec prodpoly p1 p2 = match (p1, p2) with
  | _, [] -> []
  | [], _ -> []
  | m::q, _ -> addpoly (prodmon m p2) (addpoly q p2);;

let rec derive p= match p with
 | [] -> []
 | (d,a)::q -> (d-1,(float_of_int d) *. a)::derive q;;

(*Ex 10*)
let rec takewhile p s = match p(List.hd s) with
  |true -> (List.hd s) :: (takewhile p (List.tl s))
  |false -> [];;

let rec dropewhile p s = match p(List.hd s) with
  |true -> dropewhile p (List.tl s)
  |false -> List.tl s;;

let appl p l = List.for_all p (takewhile p l);;

(* s = dropewhile p s "+" takewhile p s  *)


(*Ex 12*)
let rec somme t i j = match i,j with
| i, j when i=j -> t.(j)
| i, j -> (somme t i (j-1)) + t.(j);;

(* example array *)
let randarr = Array.init (Random.int 100) (fun n -> (Random.int 100)*(int_of_float ((-1.)**(float_of_int (n * Random.int 2)))));;
let n = Array.length randarr;;

let tranche_min1 t n =
  let m = ref t.(0) in
  for i=0 to n-1 do 
    for j=i to n-1 do
      m:= min (somme t i j) !m
    done;
  done;
  !m;;

let rec somme_min t j n = match j with
| j when j=n-1 -> t.(n-1)
| j -> let s = somme_min t (j+1) n in min t.(j) (s+t.(j))

let tranche_min2 t n =
  let m = ref t.(n-1) in
  for j=n-1 downto 0 do
    m:= min (somme_min t j n) !m
  done;
  !m;;

(* En variant i, il faut savoir si smin reste la somme minimale ou si s+t.(i+1) devient la nouvelle somme minimale sur 0, i+1 *)
let tranche_min3 t n =
  let smin = ref t.(0) and s = ref t.(0) and k = ref 0 and d = ref 0 and f = ref 0 in 
  for i=0 to n-1 do
    if t.(i) < !s + t.(i) then
      begin
        s:=t.(i);
        k:=i;
      end
    else
      s:= !s + t.(i);
    if !s < !smin then
      begin
        smin:=!s;
        d:=!k;
        f:=i;
      end
  done;
  !d, !f, !smin;;

(*Ex 13*)
let inferieur u v = u < v;;

(*
val sub : string -> int -> int -> string
String.sub s start len returns a fresh string of length len, containing the substring of s that starts at position start and has length len.
*)

let conjugue u i =
  let n = String.length u in
  let v = String.sub u 0 (i-1) and w = String.sub u (i-1) (n-i+1) in w^v;;

let rec lyndon_aux u n k = match k with
  | 0 -> true
  | k -> inferieur u (String.sub u k (n-k)) && lyndon_aux u n (k-1);;

let lyndon u =
  let n = String.length u in
  lyndon_aux u n (n-1);;


let factorisation u =
  (* Conversion en une liste de charactère*)
  let n = String.length u in
  let rec initialise l k = match k with
    | k when k=0 -> l
    | k -> initialise ((String.make 1 u.[k-1])::l) (k-1) in 
  let ul = initialise [] n in
  (* On raccourci la séquence *)
  let rec compacte l = match l with
    |[] -> []
    |[a] -> [a]
    |(a::b::q) when a<b -> (a^b)::(compacte q)
    |(a::b::q) -> a::compacte (b::q) in 
  let ll = ref ul in let lll = ref (compacte !ll) in
    while !ll <> !lll do
    ll := !lll ; 
    lll := compacte !ll 
    done;
  !ll;;

let rec insere_mot_lst u l = match l with
  | [] -> [u]
  | (a::q) when u < a -> u::a::q
  | (a::q) when u = a -> a::q
  | (a::q) -> a::(insere_mot_lst u q);;

let rec insere_lst_lst l1 l2 = match l1 with
  | [] -> l2 
  | (a::q) -> insere_lst_lst q (insere_mot_lst a l2);;

let rec fusionne_listes l1 l2 = match (l1, l2) with
  | [], _ -> l2
  | _, [] -> l1
  | (a::q), (b::r) -> let la = fusionne_listes (a::q) r and lb = fusionne_listes q r in
                      let lc = insere_lst_lst la lb in 
                        if a<b then 
                          insere_mot_lst (a^b) lc 
                        else 
                          lc;;

let nmax=9;;
let lynd = Array.make (nmax+1) [];;
let remplir_lynd n =
      lynd.(1) <- ["0";"1"];
      for i=2 to n do
        for j=1 to i do
          lynd.(i) <- insere_lst_lst lynd.(i) (fusionne_listes lynd.(j) lynd.(i-j))
        done
      done;
      for i=2 to n do
        let rec aux l lt = match lt with
          | [] -> l
          | (a::q) -> if (String.length a) = i then 
                        aux (a::l) q
                      else 
                        aux l q
                      in
          lynd.(i) <- aux [] lynd.(i)
      done;;
      

remplir_lynd 4;;
lynd;;