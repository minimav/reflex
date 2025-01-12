"""Stub file for reflex/components/radix/themes/layout/list.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Iterable, Literal, Optional, Union
from reflex.components.component import Component, ComponentNamespace
from reflex.components.core.foreach import Foreach
from reflex.components.el.elements.typography import Li, Ol, Ul
from reflex.components.lucide.icon import Icon
from reflex.components.radix.themes.typography.text import Text
from reflex.vars import Var

LiteralListStyleTypeUnordered = Literal["none", "disc", "circle", "square"]
LiteralListStyleTypeOrdered = Literal[
    "none",
    "decimal",
    "decimal-leading-zero",
    "lower-roman",
    "upper-roman",
    "lower-greek",
    "lower-latin",
    "upper-latin",
    "armenian",
    "georgian",
    "lower-alpha",
    "upper-alpha",
    "hiragana",
    "katakana",
]

class BaseList(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        items: Optional[Union[reflex.vars.Var[Iterable], Iterable]] = None,
        list_style_type: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal[
                            "none",
                            "decimal",
                            "decimal-leading-zero",
                            "lower-roman",
                            "upper-roman",
                            "lower-greek",
                            "lower-latin",
                            "upper-latin",
                            "armenian",
                            "georgian",
                            "lower-alpha",
                            "upper-alpha",
                            "hiragana",
                            "katakana",
                        ],
                        Literal["none", "disc", "circle", "square"],
                    ]
                ],
                Literal["none", "disc", "circle", "square"],
                Literal[
                    "none",
                    "decimal",
                    "decimal-leading-zero",
                    "lower-roman",
                    "upper-roman",
                    "lower-greek",
                    "lower-latin",
                    "upper-latin",
                    "armenian",
                    "georgian",
                    "lower-alpha",
                    "upper-alpha",
                    "hiragana",
                    "katakana",
                ],
            ]
        ] = None,
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
    ) -> "BaseList":
        """Create a list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            list_style_type: The style of the list. Default to "none".
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.

        """
        ...

    def add_style(self) -> dict[str, Any] | None: ...

class UnorderedList(BaseList, Ul):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        items: Optional[Union[reflex.vars.Var[Iterable], Iterable]] = None,
        list_style_type: Optional[LiteralListStyleTypeUnordered] = "disc",
        access_key: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
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
    ) -> "UnorderedList":
        """Create a unordered list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            list_style_type: The style of the list.
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.

        """
        ...

class OrderedList(BaseList, Ol):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        items: Optional[Union[reflex.vars.Var[Iterable], Iterable]] = None,
        list_style_type: Optional[LiteralListStyleTypeOrdered] = "decimal",
        reversed: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        start: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        type: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        access_key: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
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
    ) -> "OrderedList":
        """Create an ordered list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            list_style_type: The style of the list.
            reversed: Reverses the order of the list.
            start: Specifies the start value of the first list item in an ordered list.
            type: Specifies the kind of marker to use in the list (letters or numbers).
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.

        """
        ...

class ListItem(Li):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        access_key: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
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
    ) -> "ListItem":
        """Create a list item component.

        Args:
            *children: The children of the component.
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list item component.

        """
        ...

class List(ComponentNamespace):
    item = staticmethod(ListItem.create)
    ordered = staticmethod(OrderedList.create)
    unordered = staticmethod(UnorderedList.create)

    @staticmethod
    def __call__(
        *children,
        items: Optional[Union[reflex.vars.Var[Iterable], Iterable]] = None,
        list_style_type: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal[
                            "none",
                            "decimal",
                            "decimal-leading-zero",
                            "lower-roman",
                            "upper-roman",
                            "lower-greek",
                            "lower-latin",
                            "upper-latin",
                            "armenian",
                            "georgian",
                            "lower-alpha",
                            "upper-alpha",
                            "hiragana",
                            "katakana",
                        ],
                        Literal["none", "disc", "circle", "square"],
                    ]
                ],
                Literal["none", "disc", "circle", "square"],
                Literal[
                    "none",
                    "decimal",
                    "decimal-leading-zero",
                    "lower-roman",
                    "upper-roman",
                    "lower-greek",
                    "lower-latin",
                    "upper-latin",
                    "armenian",
                    "georgian",
                    "lower-alpha",
                    "upper-alpha",
                    "hiragana",
                    "katakana",
                ],
            ]
        ] = None,
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
    ) -> "BaseList":
        """Create a list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            list_style_type: The style of the list. Default to "none".
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.

        """
        ...

list_ns = List()
list_item = list_ns.item
ordered_list = list_ns.ordered
unordered_list = list_ns.unordered
