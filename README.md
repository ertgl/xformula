# XFormula

Highly customizable language front-end, aimed to be a base
for custom DSL evaluators.

---

**Developer note:** I've created this library to use in many of my projects and
decided to publish the source code, because it may help somebody to write a DSL
compiler or evaluator can get benefit from Python ecosystem, within a reasonable
time.

I couldn't write documentation because of my tight schedule in these days. 
But I see the code as self-explanatory, feel free to read it if you're interested.

In the meantime, please note that **this project is still in development**.

---


## Features:

- Built on top of [Lark Parser Toolkit](https://lark-parser.readthedocs.io/en/latest/)
- - LALR(1), Earley and CYK parsing algorithms are supported by Lark;
    XFormula uses LALR(1) by default
- Automatic EBNF grammar generator via declarative Python functions
  (The final grammar generated using the default features can be found in
  [out/Grammar.lark](https://github.com/ertgl/xformula/blob/main/out/Grammar.lark)
  file)
- Modular featurization system to manipulate grammar and parser context dynamically. 
- A ready-to-use compact dialect that supports some general purpose data types
  and basic symbols
  (See `xformula.syntax.ast` package)

See `xformula.syntax.core.features` package and
`xformula.syntax.core.operations.default_operator_precedences` module for more
information about the default behaviours.


## License

[MIT](https://github.com/ertgl/xformula/blob/main/LICENSE)
