
(* Tri bulle *)
let rec une_passe l = match l with
 |[] -> false,[]
 |[x] -> false,[x]
 |x::reste -> let boolean,res=(une_passe reste) in if x<=(List.hd res) then boolean,x::res else true,(List.hd res)::x::(List.tl res);;


let rec tribulle l = match l with
 |[] -> []
 |l -> let (modifiee,liste)=une_passe l in if modifiee then (List.hd liste)::tribulle(List.tl liste) else liste;;