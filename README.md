# XFormula

A modular language front-end and parser generator for building
<a href="https://en.wikipedia.org/wiki/Domain-specific_language" target="_blank">domain-specific languages</a> (DSLs).

## Table of Contents

- [Overview](#overview)
  - [Core Model](#core-model)
  - [Dynamic Syntax](#dynamic-syntax)
  - [AST Composition](#ast-composition)
- [Usage](#usage)
  - [Define Tokens](#define-tokens)
  - [Define AST Nodes](#define-ast-nodes)
  - [Connect Grammar to AST](#connect-grammar-to-ast)
  - [Package the Syntax as a Feature](#package-the-syntax-as-a-feature)
  - [Build the Parser](#build-the-parser)
  - [Keeping the Grammar Small](#keeping-the-grammar-small)
- [Portability](#portability)
- [A Practical Example](#a-practical-example)
- [License](#license)

## Overview

In XFormula, syntax is assembled from independent features. A feature can
introduce tokens, grammar rules,
<a href="https://en.wikipedia.org/wiki/Abstract_syntax_tree" target="_blank">AST</a>
nodes, and the transformations that
connect them. Features can then be combined, extended, or removed without
rewriting the rest of the language.

The result is a language definition that can evolve as a system rather than as
a single grammar file.

Under the hood, XFormula generates an
<a href="https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form" target="_blank">EBNF</a>
grammar for
<a href="https://lark-parser.readthedocs.io/" target="_blank">Lark Parser Toolkit</a>,
while providing the type system, object model, transformation logic, and
customization layer around it.

Lark supports
<a href="https://en.wikipedia.org/wiki/LALR_parser" target="_blank">LALR(1)</a>,
Earley, and CYK
parsing algorithms, and XFormula's default features are additionally designed
to be compatible with the LALR(1) algorithm, since it is known for its speed
and efficiency in both time (CPU) and space (memory).

### Core Model

XFormula separates three concerns that are often mixed together in parser
implementations:

1. **Lexical syntax**: What text should be recognized as a token?
2. **Grammar**: How are those tokens composed into language constructs?
3. **Semantic transformation**: How does the parse result become an AST node?

A "feature" can participate in all three.

### Dynamic Syntax

A syntax feature does not need to modify a central grammar definition. Instead,
it contributes definitions to a shared syntax context. Other definitions can
discover those contributions through "tags" and "priorities."

For example:

```text
BOOL token ───────────> Bool ─────┐
                                  │
NONE token ───────────> None_ ────┤
                                  │
                                  └──> Literal ───> Start
```

Adding another literal feature can extend the same structure without modifying
the existing `Literal` implementation. This is particularly useful for
languages that have optional syntax, experimental features, dialects, or
domain-specific extensions.

The main building blocks behind this mechanism are:

* [`EBNFExpressionBuilderProtocol`](src/xformula/syntax/grammar/definitions/abc/ebnf_expression_builder_protocol.py#L164)
* [`SyntaxContext`](src/xformula/syntax/core/context/abc/syntax_context.py#L104)
* [`TaggedDefinitionIterator`](src/xformula/syntax/core/customization/tagging/tagged_definition_iterator.py#L13)

### AST Composition

XFormula uses inheritance to represent the relationships between language
constructs. For example, a parsed `Bool` node can participate in the broader
AST hierarchy:

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

Because the language model is represented directly in the Python type
hierarchy, generic operations can work against abstractions such as `Literal`,
`Expression`, or `Node` without requiring every concrete syntax feature to be
explicitly registered.

For example:

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

The important consequence is that syntax features can specialize a common
language model without losing their semantic identity.

## Usage

The easiest way to understand XFormula is to build a language feature.

We will re-define two literals; bool and none:

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

### Define Tokens

A terminal describes how the lexer recognizes a piece of source text and how
that token is transformed at runtime.

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

The boolean token works in exactly the same way:

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

The important part is not the regular expression itself. It is the boundary
between **syntax recognition** and **typed runtime values**.

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

The AST therefore keeps the semantic value rather than the original source
representation.

```text
"true"
   ↓
BOOL token
   ↓
bool("true")
   ↓
Bool(value=True)
```

That pipeline is the foundation for the rest of the language.

### Connect Grammar to AST

A non-terminal describes how a grammar construct is assembled and, when
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

The boolean non-terminal can consume the already transformed value produced by
`BOOL`:

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

The final `Literal` non-terminal does not need to directly know which literal
types exist. It simply collects the definitions that have been tagged as
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

This is where the compositional model becomes completely visible. `Literal`
does not manually enumerate `Bool` and `None_`. The features declare their
relationship to `Literal`, and XFormula assembles the grammar from those
declarations.

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

The grammar is therefore an artifact of the feature composition rather than the
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
tree node. XFormula can therefore use intermediate grammar rules to compose the
language without forcing those rules to become unnecessary AST layers.
This keeps the resulting AST focused on semantic constructs rather than
implementation details of the grammar.

The `PolyfillFeature` can also provide missing non-terminals automatically when
they are only needed as structural or tagging points.

## Portability

XFormula generates EBNF for Lark Parser Toolkit. This keeps the generated
grammar separate from the Python implementation of the language itself.
The grammar can therefore serve as an interchange point for environments that
support Lark-compatible grammars.

The dynamic transformation behavior provided by XFormula is more specific to
the XFormula runtime. Reproducing that behavior elsewhere requires equivalent
transformation logic, particularly the automatic operator precedence and
associativity handling implemented by:

- [`NonTerminalOperationClassBuilder.transform_parse_tree`](src/xformula/syntax/core/features/operations/runtime/reflection/non_terminal_operation_class_builder.py#L236)

See the
<a href="https://lark-parser.readthedocs.io/en/stable/features.html#extra-features" target="_blank">extra features</a>
section in the Lark documentation for the available implementations.

## A Practical Example

<a href="https://github.com/ertgl/django-xformula" target="_blank">django-xformula</a>
uses XFormula to transform formulas into SQL queries through
<a href="https://www.djangoproject.com/" target="_blank">Django</a>'s
<a href="https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping" target="_blank">ORM</a>.

That is a useful demonstration of the architecture in practice:

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
