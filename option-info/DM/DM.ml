let rec conw n = 
  let k=n/4 in 
    match n mod 4 with
    | 1-> print_int n; conw(3*k+1)
    | 3-> print_int n; conw(3*k+2)
    | t-> n*3/2;;
 


let rec suppr_liste test l = match l with
| [] -> []
| e::f -> if test e then suppr_liste test f else e::(suppr_liste test f);;

let test2 a = a mod 2 = 0;;


let rec merp l = match List.length l with
| 0 -> true
| n -> let ll=suppr_liste (function a -> a=n) l in (List.length ll=n-1)&&(merp ll);;

(* La fonction merp renvoie 'true' si la liste  de longueur n contient tout les éléments de {1, n} (peu importe leur ordre) sinon renvoie 'false' *)

(* La récursivité n'est pas terminale: du fait de  (List.length ll=n-1)&&(merp ll) *)


(* Exo 1 *) 

(* 1a
La récurrence s'arrête quand k=1
À chaque étape on effectue une multiplication, et on appel puissance n k-1
Il y a donc k multiplications
*)

(*
puissance n 1 est correcte 

Supposons que l’appel récursif puissance2 n k/2 fournisse le résultat correct.
Dans ce cas la valeur retournée puissance2 n k sera correcte, car la valeur de
x vaut n^(k/2) où k/2 est le quotient de la division de k par 2
Dans le cas où k est paire 
la valeur retournée x*x est égale à n^k et puissance2 n k est correcte
Dans le cas où k est impaire k=(k/2)*2 + 1 
la valeur retournée x*x*n  est égale à n^k et puissance2 n k est correcte
*)

let rec puissance2 n k =
  if k=1 then n 
  else n * (puissance2 n (k-1));;

let test_puissance n k =
  let rec aux m = match puissance2 m k with
  | t when n=t -> true
  | t when n<t -> false 
  | _ -> aux (m+1)
  in aux 2;;


let test_puissance_entiere n =
  let rec aux k = 
    if puissance2 2 k <= n then
      if test_puissance n k then true else aux (k+1)
    else false 
  in aux 2;;  

let rec  liste1_puissances_entieres k = match k with
    | 2 -> []
    | k -> if (test_puissance_entiere k) then k::(liste1_puissances_entieres (k-1)) else liste1_puissances_entieres (k-1);;

(* On peut enlever les nombres premiers *)

let rec liste2_puissances_entieres n =
  let i = ref 2 in
  let puiss = ref [] in
	while (!i)*(!i) <= n do
      let k = ref 2 in
      let j = ref (puissance2 !i !k) in
      while (!j <= n) do 
        puiss := !j::!puiss; 
        k:=!k+1;
        j:= puissance2 !i !k
      done;
    i:=!i+1
  done;
  !puiss;;
  
let decalG l e = (l mod 1000) * 10 + e;;


let mot = [|1;2;3;4;6;2;0;3;1;7;5;2;0;1;7|];;

let rec testG_motif tab =
  let rec aux mot i = 
    if (i > (Array.length tab)-1) then false 
    else
    let l = decalG mot tab.(i) in
    match l with 
    | l when l = 2017 -> true
    | l -> aux l (i+1) in 
  let l = tab.(0)*100 + tab.(1)*10 + tab.(2) in
  aux l 3;;

  let rec nbG_motif tab =
    let rec aux mot i c = 
      if (i > (Array.length tab)-1) then c 
      else
      let l = decalG mot tab.(i) in
      match l with 
      | l when l = 2017 -> aux l (i+1) (c+1)
      | l -> aux l (i+1) c in 
    let l = tab.(0)*100 + tab.(1)*10 + tab.(2) in
    aux l 3 0;;


let calculH l = (l.(0)*1000 + l.(1)*100 + l.(2)*10 + l.(3)) mod 11
