let issqrt n =
  let x = int_of_float(sqrt(float_of_int(n))) in
  n=x*x;;

let syracuse n k =
  let x = ref k in
    for i = 1 to n do
      if !x mod 2 = 0 then
	      x:=!x/2
      else
	      x:=!x*3+1
    done;
    !x;;

let disto1 k =
  let c = ref 0 in
  let x = ref k in
  while !x!=1 do
    c:=!c+1;
    if !x mod 2 = 0 then
	    x:=!x/2
    else
	    x:=!x*3+1
  done;
  !c;;

let maxi k= 
  let m = ref k in
  let x = ref k in
    while !x!=1 do
      if !x mod 2 = 0 then
	      x:=!x/2
      else
        x:=!x*3+1;
      if !m < !x then
        m:=!x;
    done;
    !m;;

let maxi_opt k=
  let x=ref k and m=ref k in
  while !x!=1 do
    x:=syracuse 1 !x;
    if !m < !x then
      m:=!x;
  done;
  !m;;


(*
print_int(maxi_opt 27);
print_newline();
print_int(maxi 27);
*)

let silverman n=
  let tab = Array.make (n+1) 1 in
  let c = ref 0 in
  for i = 1 to n do
      let k = ref 0 in
      while !c + !k < n && !k < tab.(i-1) do 
        tab.(!c + !k) <- i;
        k:=!k+1;
      done;
      c:=!c + !k;
  done;
  (*
  for i = 0 to n do
    print_int(i+1);
    print_string(" ");
    print_int(tab.(i));
    print_newline();
  done;
  *)
  tab.(n-1);;



let phi n =
  let p = (1. +. sqrt(5.)) /. 2. in
  (p**(2. -. p))*.(float_of_int(n)**(p -. 1.));;


let compare n =
  print_int(silverman n);
  print_string(" ");
  print_float(phi n);
  print_newline();;

(*
compare(28);
compare(5000);
compare(15498);
*)