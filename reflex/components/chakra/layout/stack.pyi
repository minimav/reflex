"""Stub file for reflex/components/chakra/layout/stack.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import List, Union
from reflex.components.chakra import ChakraComponent, LiteralStackDirection
from reflex.vars import Var

class Stack(ChakraComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        align_items: Optional[Union[reflex.vars.Var[str], str]] = None,
        direction: Optional[
            Union[
                reflex.vars.Var[Union[List[str], Literal["row", "column"]]],
                Literal["row", "column"],
                List[str],
            ]
        ] = None,
        is_inline: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        justify_content: Optional[Union[reflex.vars.Var[str], str]] = None,
        should_wrap_children: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        spacing: Optional[Union[reflex.vars.Var[str], str]] = None,
        wrap: Optional[Union[reflex.vars.Var[str], str]] = None,
        justify: Optional[Union[reflex.vars.Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Stack":
        """Create the component.

        Args:
            *children: The children of the component.
            align_items: Shorthand for alignItems style prop
            direction: The direction to stack the items.
            is_inline: If true the items will be stacked horizontally.
            justify_content: Shorthand for justifyContent style prop
            should_wrap_children: If true, the children will be wrapped in a Box, and the Box will take the spacing props
            spacing: The space between each stack item
            wrap: Shorthand for flexWrap style prop
            justify: Alignment of contents.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class Hstack(Stack):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        align_items: Optional[Union[reflex.vars.Var[str], str]] = None,
        direction: Optional[
            Union[
                reflex.vars.Var[Union[List[str], Literal["row", "column"]]],
                Literal["row", "column"],
                List[str],
            ]
        ] = None,
        is_inline: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        justify_content: Optional[Union[reflex.vars.Var[str], str]] = None,
        should_wrap_children: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        spacing: Optional[Union[reflex.vars.Var[str], str]] = None,
        wrap: Optional[Union[reflex.vars.Var[str], str]] = None,
        justify: Optional[Union[reflex.vars.Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Hstack":
        """Create the component.

        Args:
            *children: The children of the component.
            align_items: Shorthand for alignItems style prop
            direction: The direction to stack the items.
            is_inline: If true the items will be stacked horizontally.
            justify_content: Shorthand for justifyContent style prop
            should_wrap_children: If true, the children will be wrapped in a Box, and the Box will take the spacing props
            spacing: The space between each stack item
            wrap: Shorthand for flexWrap style prop
            justify: Alignment of contents.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class Vstack(Stack):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        align_items: Optional[Union[reflex.vars.Var[str], str]] = None,
        direction: Optional[
            Union[
                reflex.vars.Var[Union[List[str], Literal["row", "column"]]],
                Literal["row", "column"],
                List[str],
            ]
        ] = None,
        is_inline: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        justify_content: Optional[Union[reflex.vars.Var[str], str]] = None,
        should_wrap_children: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        spacing: Optional[Union[reflex.vars.Var[str], str]] = None,
        wrap: Optional[Union[reflex.vars.Var[str], str]] = None,
        justify: Optional[Union[reflex.vars.Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Vstack":
        """Create the component.

        Args:
            *children: The children of the component.
            align_items: Shorthand for alignItems style prop
            direction: The direction to stack the items.
            is_inline: If true the items will be stacked horizontally.
            justify_content: Shorthand for justifyContent style prop
            should_wrap_children: If true, the children will be wrapped in a Box, and the Box will take the spacing props
            spacing: The space between each stack item
            wrap: Shorthand for flexWrap style prop
            justify: Alignment of contents.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...
