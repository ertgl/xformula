# XFormula

A highly customizable language front-end and parser generator. Designed for
rapid prototyping of
[domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
implementations. *Applicable also for general-purpose languages.*

___

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
  - [Defining Tokens](#defining-tokens)
  - [Defining AST Nodes](#defining-ast-nodes)
  - [Transforming Tokens into AST Nodes](#transforming-tokens-into-ast-nodes)
  - [Setting Up the Feature](#setting-up-the-feature)
  - [Initializing the Parser](#initializing-the-parser)
  - [Dynamic Syntax Concept](#dynamic-syntax-concept)
- [Portability](#portability)
- [Real-world Example](#real-world-example)
- [License](#license)

## Overview

XFormula is a language front-end tool that enables developers to define
language syntax and semantics using the object-oriented paradigm, achieving
exceptional modularity and flexibility. It offers a set of built-in, commonly
used features for general-purpose languages that can be omitted or extended as
needed for rapid prototyping.

While XFormula itself does not provide any compilation or evaluation
capabilities, it allows you to define a highly flexible and customizable
[AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) structure in a
modular way. Additionally, it includes a parser that generates an AST based on
a given input string.

At its core, XFormula is a parser generator that leverages the powerful
[Lark Parser Toolkit](https://lark-parser.readthedocs.io/) under the hood. Lark
supports [LALR(1)](https://en.wikipedia.org/wiki/LALR_parser), Earley, and CYK
parsing algorithms, and XFormula's default features are designed to be
compatible with the LALR(1) algorithm, which is renowned for its speed and
efficiency in both time (CPU) and space (memory).

## Usage

If you are already familiar with the terminology, the best way to understand
how to use XFormula is by examining the following modules:

- [xformula.syntax.ast](src/xformula/syntax/ast/nodes/abc)
- [xformula.syntax.core.features](src/xformula/syntax/core/features)
- [xformula.syntax.core.operations.default_operator_precedences](src/xformula/syntax/core/operations/default_operator_precedences.py#L16)

The final [EBNF](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)
grammar, generated automatically by XFormula using the default features, is
output to the [out/Grammar.lark](out/Grammar.lark) file.

To illustrate the development process, let’s define a few simple syntax
features and their corresponding AST nodes for the `none` and `bool` types.

### Defining Tokens

The first step is to specify how the tokens should be parsed.

```python
from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token


class NONE(
    # Note: The `Terminal` class is generic and requires the type of the
    # transformed token as a type argument.
    Terminal[None],
):
    class Meta:

        # The priority of the terminal in the lexer rules.
        priority = 2000

        tags = {
            # The priority of this terminal in the `None` non-terminal grammar
            # rules group.
            non_terminal("None"): 0,
        }

    # The grammar definition of the terminal,
    # that will be used by the lexer.
    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        bound = self.regex.bound
        word = self.regex.word

        return define(regex(bound(word("none"))))

    # The runtime transformation of the token.
    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> None:
        # The token is already of type `None`.
        return None
```

Next, define the `bool` type:

```python
from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token


class BOOL(
    Terminal[bool],
):
    class Meta:

        priority = 2000

        tags = {
            non_terminal("Bool"): 1000,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        any_of = self.regex.any_of
        bound = self.regex.bound
        word = self.regex.word

        return define(
            regex(
                any_of(
                    bound(word("false")),
                    bound(word("true")),
                ),
            ),
        )

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> bool:
        # Transform the `false` and `true` tokens into False and True,
        # respectively.
        return token.value.lower() == "true"
```

### Defining AST Nodes

Defining the AST nodes for the `none` and `bool` types is straightforward,
thanks to the comprehensive `xformula.syntax.ast` module.

For the `none` type:

```python
import dataclasses

from xformula.syntax.ast.nodes import Literal


@dataclasses.dataclass()
class None_(
    # Note: The `Literal` class is generic and requires the type of the
    # transformed token as a type argument.
    Literal[None],
):

    # The `value` field is implemented with the `None` type.
    value: None = dataclasses.field(
        kw_only=True,
        init=False,
        default=None,
    )
```

And for the `bool` type:

```python
import dataclasses

from xformula.syntax.ast.nodes import Literal


@dataclasses.dataclass()
class Bool(
    Literal[bool],
):

    # The `value` field is implemented with the `bool` type.
    value: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )
```

### Transforming Tokens into AST Nodes

Once the syntax features and AST nodes are defined, the next step is to specify
how tokens should be transformed into AST nodes.

Define the `None` non-terminal as follows (note that `None` is reserved in
Python, so we use `None_` instead):

```python
from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import None_ as NoneNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree


# `None` is reserved in Python, so we use `None_` instead.
class None_(
    NonTerminal[NoneNode],
):
    class Meta:

        # This will replace the default definition name `None_`.
        definition_name = "None"

        # Mark this non-terminal as atomic.
        # This means that we want to use our custom transformation logic
        # for the parse tree of this non-terminal.
        # See the `transform_parse_tree` method below.
        atomic = True

        tags = {
            non_terminal("Literal"): -1000,
        }

    # The grammar definition of the non-terminal.
    def build_grammar(self) -> str:
        # Since we tagged the `NONE` terminal with the `None` non-terminal,
        # we can automatically reference it here.
        # And, if another feature is added that tags the `None` non-terminal,
        # the related terminals/non-terminals will be included here as well.
        # Respecting the priority levels of the tags.
        return self.ebnf.define_tagged_alternation()

    # The runtime transformation of the parse tree.
    # This is where we transform the parse tree into an AST node.
    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree,
    ) -> NoneNode:
        return NoneNode()
```

Similarly, define the `Bool` non-terminal:

```python
from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import Bool as BoolNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree


class Bool(
    NonTerminal[BoolNode],
):
    class Meta:

        atomic = True

        tags = {
            non_terminal("Literal"): -2000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[bool],
    ) -> BoolNode:
        # The `Bool` non-terminal has only one child, the transformed value
        # from the `BOOL` terminal.
        value = cast(bool, tree.children[0])
        # Return the `bool` node with that transformed value.
        return BoolNode(
            value=value,
        )
```

Lastly, define the non-terminal for `Literal`:

```python
from typing import TypeVar, cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Literal as LiteralNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree


T = TypeVar("T")


class Literal(
    NonTerminal[
        LiteralNode[T],
    ],
):
    class Meta:

        tags = {
            # Mark this non-terminal as the start rule of the grammar.
            non_terminal("Start"): -1,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    # Default transformation for non-atomic non-terminals.
    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[T],
    ) -> LiteralNode[T]:
        return cast(LiteralNode, tree.children[0])
```

### Setting Up the Feature

To use these features, define a feature class that modifies the syntax context
during setup:

```python
from xformula.syntax.core.features.abc import Feature


class LiteralFeature(Feature):

    def setup(self) -> None:
        self.non_terminal_types.extend(
            [
                None_,
                Bool,
                Literal,
            ],
        )

        self.terminal_types.extend(
            [
                NONE,
                BOOL,
            ],
        )
```

### Initializing the Parser

Finally, initialize the parser:

```python
from xformula.syntax.core.context import SyntaxContext
# Note: We tagged our `Literal` non-terminal with the `Start` non-terminal.
# If the `Start` non-terminal is not defined, you can either define it or use
# the `PolyfillFeature` to handle it automatically.
from xformula.syntax.core.features.polyfill import PolyfillFeature
from xformula.syntax.parser import Parser


syntax_context = SyntaxContext(
    feature_types=[
        LiteralFeature,
        # `PolyfillFeature` automatically defines any missing tags as
        # non-atomic non-terminals during setup.
        PolyfillFeature,
    ],
)

parser = Parser(
    syntax_context=syntax_context,
    # Optionally, you can also pass a runtime context here to customize or
    # override the default.
)

# Parse an input string.
ast = parser.parse("true")

# Outputs: Bool(value=True)
print(ast)

# Outputs: True
print(ast.value)

# Outputs: None_(value=None)
print(parser.parse("none"))
```

The generated grammar is accessible via the `ebnf_document` attribute of the
parser. In this example, it might look like:

```ebnf
?start : literal

?literal : bool
         | none

bool : BOOL

none : NONE

BOOL.2000 : /\bfalse\b|\btrue\b/

NONE.2000 : /\bnone\b/
```

As you can see, the `start` rule is prefixed with a `?` character. This is
because the `PolyfillFeature` automatically defines the `Start` non-terminal as
non-atomic. Since it does not have specific transformation logic and is used
only for tagging purposes, the parser automatically replaces the `Start`
non-terminal's parse tree with that of the `Literal` non-terminal. Likewise,
because `Literal` is also non-atomic, its parse tree is further replaced by
that of the `Bool` or `None` non-terminal based on the input. This approach
helps avoid deep nesting of AST nodes while leveraging the inheritance and
polymorphism features of OOP.

To observe the default polymorphism, you can inspect the
[MRO](https://docs.python.org/3/howto/mro.html) of an AST node class, similar
to the following:

```python
>>> parser.parse("none").__class__.__mro__
(
  <class 'xformula.syntax.core.features.literals.ast.nodes.none_.None_'>,
  <class 'xformula.syntax.ast.nodes.abc.literal.Literal'>,
  <class 'xformula.syntax.ast.nodes.abc.term.Term'>,
  <class 'xformula.syntax.ast.nodes.abc.primary.Primary'>,
  <class 'xformula.syntax.ast.nodes.abc.operand.Operand'>,
  <class 'xformula.syntax.ast.nodes.abc.simple_expression.SimpleExpression'>,
  <class 'xformula.syntax.ast.nodes.abc.expression.Expression'>,
  <class 'xformula.syntax.ast.nodes.abc.has_value.HasValue'>,
  <class 'typing.Generic'>,
  <class 'xformula.syntax.ast.nodes.abc.node.Node'>,
  <class 'xformula.arch.meta.configurable.Configurable'>,
  <class 'abc.ABC'>,
  <class 'object'>
)
```

### Dynamic Syntax Concept

As demonstrated above, syntax features are defined in a modular way. The
dynamic syntax concept further enhances this modularity by allowing you to plug
in or remove features without modifying the core syntax definition.

For more low-level details, refer to the following classes:

- [xformula.syntax.EBNFExpressionBuilderProtocol](src/xformula/syntax/grammar/definitions/abc/ebnf_expression_builder_protocol.py#L164)
- [xformula.syntax.SyntaxContext](src/xformula/syntax/core/context/abc/syntax_context.py#L104)
- [xformula.syntax.TaggedDefinitionIterator](src/xformula/syntax/core/customization/tagging/tagged_definition_iterator.py#L13)

## Portability

Since Lark is available for various programming languages, the grammars
generated by XFormula can be used in those languages out of the box. To achieve
the same dynamic transformation capabilities as XFormula's generated parser, it
is necessary to align with the
[NonTerminalOperationClassBuilder.transform_parse_tree](src/xformula/syntax/core/features/operations/runtime/reflection/non_terminal_operation_class_builder.py#L236)
function, which automatically resolves operator associativity and precedence.

For a list of available Lark implementations, see the
[extra features](https://lark-parser.readthedocs.io/en/stable/features.html#extra-features)
section in the Lark documentation.

## Real-world Example

For an overview of the default features and an example runtime implementation
for the language, check out the
[django-xformula](https://github.com/ertgl/django-xformula) project. This
[Django](https://www.djangoproject.com/) application transforms formulas into
SQL queries using Django's powerful
[ORM](https://en.wikipedia.org/wiki/Object–relational_mapping) capabilities.

## License

This project is licensed under the
[MIT License](https://opensource.org/license/mit).

See the [LICENSE](LICENSE) file for more information.
