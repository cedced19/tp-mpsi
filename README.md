# TP MPSI

Python and workshop source code.

## Ocaml

To compile:
```
ocamlc -g td1.ml && ./a.out
```

## Merlin

Install `opam`

```
opam init
opam install merlin
```

Add this line to .bashrc
```
test -r /home/cjung/.opam/opam-init/init.sh && . /home/cjung/.opam/opam-init/init.sh > /dev/null 2> /dev/null || true
```

## VSCode

To run code just by doing *ctlr+enter*, add to `keybindings.json`:
```
[
    {
        "key": "ctrl+enter",
        "command": "workbench.action.terminal.runSelectedText",
        "when": "editorTextFocus && editorHasSelection"
      }
]
```

##  [UTop](https://opam.ocaml.org/blog/about-utop/#The-UTop-prompt)

```
opam install utop
eval `opam config env`  # may not be needed
utop
```
