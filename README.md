# XFormula

XFormula is a modular language front-end and parser generator for building
<a href="https://en.wikipedia.org/wiki/Domain-specific_language" target="_blank">domain-specific languages</a> (DSLs).

A language rarely stays small. A new literal becomes a new expression. An
optional syntax becomes a dialect. An experimental feature needs to be enabled
without rewriting unrelated grammar. An
<a href="https://en.wikipedia.org/wiki/Abstract_syntax_tree" target="_blank">AST</a>
node needs to participate in the language without being manually threaded
through every production.

XFormula is designed for that kind of evolution:
**build languages as systems, not as monolithic grammars.**

## Table of Contents

- [Overview](#overview)
  - [The Problem](#the-problem)
  - [The Solution](#the-solution)
  - [The Core Idea](#the-core-idea)
  - [Dynamic Syntax](#dynamic-syntax)
  - [AST Composition](#ast-composition)
  - [Summary](#summary)
- [A Practical Example](#a-practical-example)
  - [Install the Package](#install-the-package)
  - [Define Tokens](#define-tokens)
  - [Define AST Nodes](#define-ast-nodes)
  - [Connect Grammar to AST](#connect-grammar-to-ast)
  - [Package the Syntax as a Feature](#package-the-syntax-as-a-feature)
  - [Build the Parser](#build-the-parser)
  - [Keeping the Grammar Small](#keeping-the-grammar-small)
- [Portability](#portability)
- [A Practical Application](#a-practical-application)
- [License](#license)

## Overview

Instead of treating the grammar as the language's central source of truth,
XFormula lets independent "features" contribute syntax, grammar, AST nodes,
and semantic transformations. The language is assembled from those features.

Under the hood, XFormula generates an
<a href="https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form" target="_blank">EBNF</a>
grammar for
<a href="https://lark-parser.readthedocs.io/" target="_blank">Lark Parser Toolkit</a>.
Around that grammar, it provides the type system, object model, transformation
logic, and customization layer needed to build a composable language; so one
can add language features without turning the grammar into the place where the
whole language has to be known.

For flexibility, Lark supports
<a href="https://en.wikipedia.org/wiki/LALR_parser" target="_blank">LALR(1)</a>,
Earley, and CYK
parsing algorithms, and XFormula's default features are additionally designed
to be compatible with the LALR(1) algorithm, since it is known for its speed
and efficiency in both time (CPU) and space (memory).

### The Problem

A feature that should be independent becomes another production. A production
needs to know about every possible alternative. AST construction becomes tied
to grammar structure. Optional syntax creates conditional branches. Removing a
feature means finding and correcting every place where the grammar and
transformations know about it.

The language becomes difficult to evolve because its pieces are no longer
independent.

### The Solution

XFormula takes the opposite approach. A feature can declare:

- the tokens it introduces,
- the grammar constructs it provides,
- the AST nodes those constructs produce,
- and the transformations that connect parsed input to semantic objects.

Those declarations are composed through a shared syntax context. The central
grammar does not need to enumerate every concrete feature. That means a
language can evolve by composition rather than by continually rewriting its
grammar.

### The Core Idea

XFormula separates three concerns that are often mixed together in parser
implementations:

1. **Lexical syntax**: What source text should be recognized as a token?
2. **Grammar**: How are those tokens composed into language constructs?
3. **Semantic transformation**: How does the parse result become an AST node?

A "feature" can participate in all three.

```text
Source text
    │
    ▼
┌────────────────┐
│ Lexical syntax │  What is this?
└───────┬────────┘
        │
        ▼
┌───────────────┐
│    Grammar    │  How does it compose?
└───────┬───────┘
        │
        ▼
┌────────────────────┐
│ Semantic transform │  What does it mean?
└──────────┬─────────┘
           │
           ▼
          AST
```

This separation gives each feature a clear responsibility while allowing the
language as a whole to remain compositional.

### Dynamic Syntax

The key mechanism behind the modularity provided by XFormula is
**dynamic syntax composition**.

A syntax feature does not need to modify a central grammar definition. Instead,
it contributes definitions to a shared
[`SyntaxContext`](src/xformula/syntax/core/context/abc/syntax_context.py#L104).
Other definitions discover those contributions through "tags" and "priorities."

For example:

```text
BOOL token ───────────> Bool ─────┐
                                  │
NONE token ───────────> None_ ────┤
                                  │
                                  └──> Literal ───> Start
```

`Literal` does not need to know that `Bool` and `None_` exist.

The concrete features declare their relationship to `Literal`. XFormula
assembles the resulting grammar from those declarations. Adding another literal
therefore extends the same language structure without requiring the existing
`Literal` implementation to be rewritten.

This is useful when a language has:

- optional syntax,
- experimental features,
- dialects,
- domain-specific extensions,
- independently developed language features.

The main building blocks behind this mechanism are:

* [`EBNFExpressionBuilderProtocol`](src/xformula/syntax/grammar/definitions/abc/ebnf_expression_builder_protocol.py#L164)
* [`SyntaxContext`](src/xformula/syntax/core/context/abc/syntax_context.py#L104)
* [`TaggedDefinitionIterator`](src/xformula/syntax/core/customization/tagging/tagged_definition_iterator.py#L13)

### AST Composition

Syntax composition is only useful if the resulting semantic model composes as
well.

XFormula represents relationships between language constructs directly in the
Python type hierarchy.

For example:

```text
Bool
└── Literal
    └── Term
        └── Primary
            └── Operand
                └── SimpleExpression
                    └── Expression
                        └── Node
```

A parsed
[Bool](src/xformula/syntax/core/features/literals/ast/nodes/bool.py#L11)
is therefore not merely a concrete parser result. It is also a
[Literal](src/xformula/syntax/ast/nodes/abc/literal.py#L15), a
[Term](src/xformula/syntax/ast/nodes/abc/term.py#L9), an
[Operand](src/xformula/syntax/ast/nodes/abc/operand.py#L14), an
[Expression](src/xformula/syntax/ast/nodes/abc/expression.py#L8), and a
[Node](src/xformula/syntax/ast/nodes/abc/node.py#L9).

This allows generic operations to work against abstractions such as `Literal`,
`Expression`, or `Node` without requiring every concrete syntax feature to be
explicitly registered.

For one more example:

```python
parser.parse("none").__class__.__mro__
```

produces an inheritance chain similar to:

```text
None_
Literal
Term
Primary
Operand
SimpleExpression
Expression
HasValue
Node
Configurable
ABC
object
```

The important consequence is that a syntax feature can specialize the common
language model without losing its semantic identity.

### Summary

XFormula is not merely:

- A collection of regular expressions.
- A static grammar file.
- A wrapper around Lark.
- A parser with a different API.

Rather, it is:

- A modular language front-end. See the list of
  [default operators and precedences](src/xformula/syntax/core/operations/default_operator_precedences.py#L16).
- A parser generator built around feature composition.
- A system for composing lexical syntax, grammar, AST nodes, and transformations.
- A generator of EBNF grammars for Lark.
- A typed object model for language constructs.
- A customization layer for evolving DSLs.

## A Practical Example

For demonstration purposes, we will re-build the two literals `bool` and
`none`:

```text
true
false
none
```

and turn them into these AST nodes:

```python
Bool(value=True)
Bool(value=False)
None_(value=None)
```

### Install the Package

```sh
pip install xformula
```

### Define Tokens

A `terminal` describes how the lexer recognizes source text and how that token
is transformed at runtime.

The none token:

```python
from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token


class NONE(Terminal[None]):

    class Meta:
        priority = 2000

        tags = {
            non_terminal("None"): 0,
        }

    def build_grammar(self) -> str:
        define = self.ebnf.define
        regex = self.ebnf.regex

        bound = self.regex.bound
        word = self.regex.word

        return define(regex(bound(word("none"))))

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> None:
        return None
```

The `boolean` token works in exactly the same way:

```python
class BOOL(Terminal[bool]):

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
        return token.value.lower() == "true"
```

The regular expressions are the easy part. The important boundary is the one
between **syntax recognition** and **typed runtime values**.

```text
"true"
   ↓
BOOL token
   ↓
bool("true")
   ↓
Bool(value=True)
```

### Define AST Nodes

For literals, XFormula provides a generic `Literal` node that can be
specialized for different value types.

```python
import dataclasses

from xformula.syntax.ast.nodes import Literal


@dataclasses.dataclass()
class None_(Literal[None]):
    value: None = dataclasses.field(
        kw_only=True,
        init=False,
        default=None,
    )
```

```python
@dataclasses.dataclass()
class Bool(Literal[bool]):
    value: bool = dataclasses.field(
        kw_only=True,
        default=False,
    )
```

The AST stores the **semantic value** rather than the original source
representation.

### Connect Grammar to AST

A `non-terminal` describes how a grammar construct is assembled and, when
necessary, how its parse tree should be transformed.

For `None`:

```python
from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import None_ as NoneNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree


class None_(NonTerminal[NoneNode]):

    class Meta:
        definition_name = "None"

        atomic = True

        tags = {
            non_terminal("Literal"): -1000,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree,
    ) -> NoneNode:
        return NoneNode()
```

The `Bool` non-terminal can consume the already transformed value produced by
`BOOL` terminal:

```python
from typing import cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.features.literals.ast.nodes import Bool as BoolNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree


class Bool(NonTerminal[BoolNode]):

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
        value = cast(bool, tree.children[0])

        return BoolNode(
            value=value,
        )
```

Finally, `Literal` collects whatever definitions have tagged themselves as
`Literal`:

```python
from typing import TypeVar, cast

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Literal as LiteralNode
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.parser.trees.abc import ParseTree


T = TypeVar("T")


class Literal(NonTerminal[LiteralNode[T]]):

    class Meta:
        tags = {
            non_terminal("Start"): -1,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[T],
    ) -> LiteralNode[T]:
        return cast(LiteralNode, tree.children[0])
```

Notice what is missing. `Literal` does not enumerate `Bool` and `None_`. It
does not need to know which literal features exist. The concrete features
declare their relationships, and XFormula assembles the language from those
declarations. That is the base of the compositional model.

### Package the Syntax as a Feature

A feature is the unit XFormula uses to compose language functionality.

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

This is the point where the pieces become a language component. A feature can
now be enabled, combined with other features, or omitted entirely.

### Build the Parser

The parser is created from a `SyntaxContext`.

```python
from xformula.syntax.core.context import SyntaxContext
from xformula.syntax.core.features.polyfill import PolyfillFeature
from xformula.syntax.parser import Parser


syntax_context = SyntaxContext(
    feature_types=[
        LiteralFeature,
        PolyfillFeature,
    ],
)

parser = Parser(
    syntax_context=syntax_context,
)
```

Now the language can be used:

```python
ast = parser.parse("true")

print(ast)
# Bool(value=True)

print(ast.value)
# True

print(parser.parse("none"))
# None_(value=None)
```

The generated grammar is also available:

```python
print(parser.ebnf_document)
```

For this example, the result is approximately:

```ebnf
?start : literal

?literal : bool
         | none

bool : BOOL

none : NONE

BOOL.2000 : /\bfalse\b|\btrue\b/
NONE.2000 : /\bnone\b/
```

Note that the grammar is an artifact of the feature composition rather than the
primary source of truth.

### Keeping the Grammar Small

XFormula intentionally uses non-atomic non-terminals where no custom
transformation is required.

Consider:

```ebnf
?start : literal
?literal : bool | none
```

The leading `?` tells Lark that these rules do not need to create an additional
tree node, so XFormula can use intermediate grammar rules to compose the
language without forcing those rules to become unnecessary AST layers.
This keeps the resulting AST focused on semantic constructs rather than
implementation details of the grammar.

Also, the `PolyfillFeature` provides missing non-terminals automatically and
non-atomically when they are only needed as structural or tagging points.

## Portability

XFormula generates EBNF for Lark Parser Toolkit. This keeps the generated
grammar separate from the Python implementation of the language itself.
The grammar can therefore serve as an interchange point for environments that
support Lark-compatible implementations.

The dynamic transformation behavior provided by XFormula is more specific to
the XFormula runtime. Reproducing that behavior elsewhere requires equivalent
transformation logic, particularly the automatic operator precedence and
associativity handling implemented by:

- [`DEFAULT_OPERATOR_PRECEDENCES`](src/xformula/syntax/core/operations/default_operator_precedences.py#L16)
- [`NonTerminalOperationClassBuilder.transform_parse_tree`](src/xformula/syntax/core/features/operations/runtime/reflection/non_terminal_operation_class_builder.py#L236)

See the
<a href="https://lark-parser.readthedocs.io/en/stable/features.html#extra-features" target="_blank">extra features</a>
section in the Lark documentation for the available implementations.

## A Practical Application

<a href="https://github.com/ertgl/django-xformula" target="_blank">django-xformula</a>
uses XFormula and its default syntax features to transform formulas into SQL
queries through
<a href="https://www.djangoproject.com/" target="_blank">Django</a>'s
<a href="https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping" target="_blank">ORM</a>.

Simply, the architecture is:

```text
User formula
     │
     ▼
   Parser
     │
     ▼
    AST
     │
     ▼
 Django ORM expression
     │
     ▼
    SQL
```

## License

This project is licensed under the
<a href="https://opensource.org/license/mit" target="_blank">MIT License</a>.
See the [LICENSE](LICENSE) file for details.
