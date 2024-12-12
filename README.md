# XFormula

Highly customizable language front-end, aimed to be a base for custom
[domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
implementations.

*With no extra limitations for use in general-purpose languages as well*.

___

XFormula is a language front-end tool that allows developers to define
language syntax and semantics in the
[OO paradigm](https://en.wikipedia.org/wiki/Object-oriented_programming)
to achieve a high level of modularity and flexibility. For fast prototyping,
it provides a set of built-in, commonly used general-purpose language features,
which can be omitted or extended as needed.

As a language front-end tool, XFormula does not provide any compilation or
evaluation capabilities. Instead, it allows the definition of a very flexible
and customizable [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
structure in a modular way. Finally, it also provides a parser that can
generate an AST based on a given string input.

That said, at the lowest level, XFormula is a parser generator that uses the talented
[Lark Parser Toolkit](https://lark-parser.readthedocs.io/) under the hood.
Lark supports LALR(1), Earley, and CYK parsing algorithms. XFormula's
default features are designed to be compatible with the
[LALR(1)](https://en.wikipedia.org/wiki/LALR_parser) algorithm,
which is very fast and efficient in terms of both time (CPU) and
space (memory).

## Usage example

Assuming you are familiar with the terminology, the best way to understand how
to use XFormula is to check the
[xformula.syntax.ast](src/xformula/syntax/ast/nodes/abc),
[xformula.syntax.core.features](src/xformula/syntax/core/features), and
[xformula.syntax.core.operations.default_operator_precedences](src/xformula/syntax/core/operations/default_operator_precedences.py#L16)
modules. The final
[EBNF](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form) grammar,
generated automatically by XFormula using the default features, is dumped into
the [out/Grammar.lark](out/Grammar.lark) file.

To concentrate on the flow of the development process, we will define a few
simple syntax features and AST nodes for them. Here, we will define `none`
and `bool` types.

The first step is to define how the tokens should be parsed.

```python
from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.ebnf import non_terminal
from xformula.syntax.grammar.terminals.abc import Terminal
from xformula.syntax.lexer.tokens.abc import Token


class NONE(
    # Note that the `Terminal` class is generic and requires
    # the type of the transformed token as a type argument.
    Terminal[None],
):
    # Django-style `Meta` class for configuration.
    class Meta:

        # The priority of the terminal in the lexer rules.
        priority = 2000

        tags = {
            # The priority of the terminal in the
            # `None` non-terminal grammar rules group.
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
        # The token is already a `None` type.
        return None
```

Now for the `bool` type.

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
        # Transform the `"false"` and `"true"` tokens into
        # `False` and `True` values.
        return token.value.lower() == "true"
```

Defining the AST nodes for the `none` and `bool` types
is a straightforward process, thanks to the completeness
of `xformula.syntax.ast` module.

```python
import dataclasses

from xformula.syntax.ast.nodes import Literal


@dataclasses.dataclass()
class None_(
    # Note that the `Literal` class is generic and requires
    # the type of the literal as a type argument.
    Literal[None],
):

    # Implement the `value` field with the `None` type.
    value: None = dataclasses.field(
        kw_only=True,
        init=False,
        default=None,
    )
```

Same for the `bool` type.

```python
import dataclasses

from xformula.syntax.ast.nodes import Literal


@dataclasses.dataclass()
class Bool(
    Literal[bool],
):

    # Implement the `value` field with the `bool` type.
    value: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )
```

Since we have defined the syntax features and AST nodes, we are ready to
specify how the tokens should be transformed into AST nodes.

For this, we will define the `None` non-terminal.

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

And the `Bool` non-terminal.

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
        # We know that the `Bool` non-terminal has only one child,
        # which is the `BOOL` terminal's transformed value.
        value = cast(bool, tree.children[0])
        # Return the bool node with that transformed value.
        return BoolNode(
            value=value,
        )
```

And the last one, for the type `Literal`.

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
            # Mark this non-terminal as the start non-terminal.
            non_terminal("Start"): -1,
        }

    def build_grammar(self) -> str:
        return self.ebnf.define_tagged_alternation()

    # The default behavior of non-atomic non-terminals.
    def transform_parse_tree(
        self,
        runtime_context: RuntimeContext,
        tree: ParseTree[T],
    ) -> LiteralNode[T]:
        return cast(LiteralNode, tree.children[0])
```

To be able to use these features, we need to define a feature class,
which will mutate the syntax context on setup time.

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

Finally, we are ready to get our parser.

```python
from xformula.syntax.core.context import SyntaxContext
# Remember, we tagged our `Literal` non-terminal with the `Start` non-terminal.
# But, we did not define the `Start` non-terminal. To fix this, either we can
# define the class, or we can get the `PolyfillFeature` done it for us.
from xformula.syntax.core.features.polyfill import PolyfillFeature
from xformula.syntax.parser import Parser


syntax_context = SyntaxContext(
    feature_types=[
        LiteralFeature,
        # This class automatically defines the missing
        # tags as non-atomic non-terminals on setup time.
        PolyfillFeature,
    ],
)

parser = Parser(
    syntax_context=syntax_context,
    # You can also pass a runtime context here,
    # to customize/override the default one.
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

The generated grammar can be accessed via the `ebnf_document` attribute of the
parser. In that example, it will contain something like this:

```ebnf
?start : literal

?literal : bool
         | none

bool : BOOL

none : NONE

BOOL.2000 : /\bfalse\b|\btrue\b/

NONE.2000 : /\bnone\b/
```

As you can see, the `start` rule has a leading `?` character. This is because
the polyfill feature automatically defined the `Start` non-terminal as an
non-atomic. Since it doesn't have any specific transformation logic, and it is
used only for tagging purposes, the parser will automatically replace the
parse-tree of the `Start` non-terminal with the parse-tree of the `Literal`
non-terminal. And because of `Literal` is also non-atomic, the parser will
continue to replace the parse-tree of the `Literal` non-terminal with the
parse-tree of the `Bool` or `None` non-terminal, based on the input string.
This is particularly useful in order to avoid deep nesting of the AST nodes,
and get benefit from the inheritance and polymorphism features of the OOP.

To observe the default polymorphism, you can check the
[MRO](https://docs.python.org/3/howto/mro.html) of an AST node class.

```python
>>> parser.parse("none").__class__.__mro__
(
  <class '__main__.None_'>,
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

### Dynamic syntax concept

As seen in the example above, the syntax features are defined in a modular way.
The dynamic syntax concept is a powerful complement to this modularity.
Therefore, plugging in or out some features without requiring any changes in
the syntax definition is also possible with that practical concept.

For more low-level details, check the
[xformula.syntax.EBNFExpressionBuilderProtocol](src/xformula/syntax/grammar/definitions/abc/ebnf_expression_builder_protocol.py#L164),
[xformula.syntax.SyntaxContext](src/xformula/syntax/core/context/abc/syntax_context.py#L104),
and
[xformula.syntax.TaggedDefinitionIterator](src/xformula/syntax/core/customization/tagging/tagged_definition_iterator.py#L13)
classes.

### Portability

Since Lark is available for various programming languages,
it should be possible to use the grammars generated by XFormula
in those languages out of the box. In order to achieve the same
dynamic transformation capabilities of XFormula's generated parser, aligning
specifically with
[NonTerminalOperationClassBuilder.transform_parse_tree](src/xformula/syntax/core/features/operations/runtime/reflection/non_terminal_operation_class_builder.py#L236)
function is necessary for automatic resolution of operator associativity and
precedence.

For the list of available Lark implementations, see the
[extra features](https://lark-parser.readthedocs.io/en/stable/features.html#extra-features)
section of the Lark documentation.

## Real-world example

For a quick overview of the default features and how to implement a runtime
for the language, you can check the
[django-xformula](https://github.com/ertgl/django-xformula) project,
which provides a [Django](https://www.djangoproject.com/) application for
transforming given formulas into [SQL](https://en.wikipedia.org/wiki/SQL)
queries using Django's amazing
[ORM](https://en.wikipedia.org/wiki/Object–relational_mapping)
capabilities.

## License

This project is licensed under the
[MIT License](https://opensource.org/license/mit).

See the [LICENSE](LICENSE) file for more information.
