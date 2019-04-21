
(* Polynome ℤ/2ℤ *)
let rec somme p q = match (p,q) with
| p, [] -> p
| [], q -> q
| p,q when List.hd p < List.hd q -> (List.hd q)::(somme p (List.tl q))
| p,q when List.hd p = List.hd q -> somme (List.tl p) (List.tl q)
| p, q -> somme q p;;

let rec produit_mon p n = match p with
| [] -> []
| a::q -> (a+n)::(produit_mon q n);;

let rec produit_pol p q = match (p,q) with
| p, [] -> []
| [], q -> []
| p, q -> somme (produit_mon q (List.hd p)) (produit_pol q (List.tl p));;

let rec division p q = match (p, q) with
| [], q -> ([], [])
| p, [] -> failwith "division par zéro"
| a::r, b::s when a<b -> ([], p)
| p, q -> let (c,r)=division (somme p (produit_mon q (List.hd p - List.hd q))) q in ((List.hd p - List.hd q)::c, r);;

let rec pgcd p q = match (p, q) with
| p, [] -> p
| [], q -> q
| p, q -> pgcd q (snd (division p q));;

let rec derivee p = match p with 
| [] -> []
| a::q when (a mod 2)=0 -> derivee q
| a::q -> (a-1)::(derivee q);;

(* Exo 4 *)
let rec mini l = match l with
| [] -> failwith "aucun élément"
| [x] -> (x, [])
| x::q -> let (y, r)=mini q in
          if x<y then (x, y::r) else (y, x::r);;

let rec tri l = match l with 
| [] -> []
| _ -> let (x,t)=mini l in x::(tri t);;

let rec abscents_aux t i j = match t with
| [] -> if i=j then [] else i::(abscents_aux t (i+1) j)
| x::q -> if i=j then []
          else if i=x then (abscents_aux q (i+1) j)
          else if i<x then i::(abscents_aux t (i+1) j)
          else (abscents_aux q i j);;

let abscents l n = abscents_aux (tri l) 0 n;;

let asseoir l n =
  let tab=Array.make n (-1) in
  let rec parcours l = match l with
    | [] -> ()
    | i::q -> if i<=n || i<0 then tab.(i) <- i;
                parcours q
  in parcours l;
  tab;;

let abscents2 l n =
  let tab = asseoir l n in 
  let rec compter i =
    if i=n then []
    else if tab.(i) <> -1 then compter(i+1)
    else i::(compter(i+1))
  in compter 0;;

let rec place tab i =
  if i <> -1 then
  begin 
      let temp=tab.(i) in
      tab.(i) <- i;
      place tab temp;
  end;;

  
let classe = [|-1;4;5;-1;3;0|];;


(* La fonction place mets le ième élève à sa place, et si elle est occupé par le mauvais élève le déplace *)

let placement tab n = 
  for i=0 to (n-1) do
    if tab.(i) <> -1 && tab.(i) <> i then
      begin 
        let temp=tab.(i) in
        tab.(i) <- -1;
        place tab temp
      end
  done;;