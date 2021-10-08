[Emacs Cheat Sheet](https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf)

## *scratch* Buffer

`C-x C-b` Open scratch buffer

### Commands

`C-u C-x C-e`

`C-j` Evaluate previous value and output the result in the scratch buffer

Example 1:

(expt 2 2) calculates 2^2 and outputs 4 on the scratch buffer when `C-j` is pressed.

Example 2:

"Distance formula"

(defun dist (a b)

(sqrt (+ (* a a) (* b b))))

Type '(dist 3.0 4.0)' calls `dist` function above with a=3.0, b=4.0 and outputs 5.0

# Compilation

`C-j`  takes string to create a data structure representing your program in a tree structure

Example: (+ (expt 2 3) 1) can be represented in a tree structure and traverse through the data structure.  Traverse through the data structure when the code runs. Only used in development.

Pros: Readability

Cons: Too slow

Instead of this data structure approach, better practice is 

### Bytecode interpreter

`M-x byte-compile RET`  `./file.el RET` creates `file.elc` 

*elc - Emacs Lisp Compiled*

.elc file still has to be interpreted using an interpreter written in C(fast)

Pros: Byte code is machine independent

They are intended to executed by emacs interpreter 

## Compiling Approaches

1. Data structure interpretation
2. Byte code interpretation
3. Just In Time(JIT) compiling
    1. Compiling at runtime
    2. Browsers take this approach
        1. Takes JavaScript source code and compiles it to your particular device
    3. Machine independent
    4. Requires huge engineering base
4. Machine code
    1. Create object file `file.o` 
    2. Fastest

`M-:` open lips code mode in mini buffer. (function-expression) to run a function in mini buffer

### Set hot key in Emacs

`(global-set-key "@" 'what-cursor-position)`

= set @ as hotkey for (what-cursor-position)

`'` here means "don't evaluate the following expression but just treat it as data structure".

~/.emacs.d/
