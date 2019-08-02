let number_magique n =
  n*(n*n+1)/2;;

(*  
  Code naïf

  let c = ref 1 and s = ref 1 in
  while !c <> n * n do
    c:=!c + 1;
    s:=!s + !c;
  done;
  !s/n;;
*)

let test_magique matrice =
  (* On vérifie si toutes les valeurs de 1 à n² sont prises *)
  let n = Array.length matrice and resultat = ref true in 
  let v=Array.make (n*n) false in (* On utilise la méthode du crible d'Ératosthène*)
  for i=1 to n do
    for j=1 to n do
      if matrice.(i-1).(j-1) >= 1 && matrice.(i-1).(j-1) <= n*n then
        v.(matrice.(i-1).(j-1))<-true;
    done;
  done;
  for k=0 to n*n-1 do
    resultat:=!resultat && v.(k);
  done;

  
  let s = number_magique n in

  (* On fait la somme des lignes *)
  for i=1 to n do
    let s_test = ref 0 in 
    for j=1 to n do
      s_test:=!s_test + matrice.(i-1).(j-1);
    done;
    resultat:=!resultat && (s = !s_test);
  done;

  (* On fait la somme des colonnes*)
  for j=1 to n do
    let s_test = ref 0 in 
    for i=1 to n do
      s_test:=!s_test + matrice.(i-1).(j-1);
    done;
    resultat:=!resultat && (s = !s_test);
  done;
  
  (* On fait la somme de la diagonale principale *)
  let s_test = ref 0 in 
  for i=1 to n do
    s_test:=!s_test + matrice.(i-1).(i-1);
  done;
  resultat:=!resultat && (s = !s_test);


  (* On fait la somme de l'autre diagonale *)
  let s_test = ref 0 in 
  for i=1 to n do
    s_test:=!s_test + matrice.(i-1).(n-i);
  done;
  resultat:=!resultat && (s = !s_test);

  !resultat;;


let construct_carre n =
  let m=Array.make_matrix n n 0 and i = ref (n/2) and j = ref (n/2) and k = ref 1 in 
  while !k <= n*n do
    m.(!i).(!j)<- !k;
    k:=!k+1;
    i:=(!i+1) mod n;
    j:=(!j+1) mod n;
    if !k <= n*n then
      begin
        while m.(!i).(!j) <> 0 do
          j:=(!j+n-1) mod n; (* mod négatif fonctionne mal *)
        done;
      end;
  done;
  m;;
