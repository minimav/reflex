"""Stub file for reflex/components/core/debounce.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Type, Union
from reflex.components.component import Component
from reflex.constants import EventTriggers
from reflex.event import EventHandler
from reflex.vars import Var, VarData

DEFAULT_DEBOUNCE_TIMEOUT = 300

class DebounceInput(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        min_length: Optional[Union[reflex.vars.Var[int], int]] = None,
        debounce_timeout: Optional[Union[reflex.vars.Var[int], int]] = None,
        force_notify_by_enter: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        force_notify_on_blur: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        value: Optional[
            Union[reflex.vars.Var[Union[float, int, str]], str, int, float]
        ] = None,
        input_ref: Optional[Union[reflex.vars.Var[str], str]] = None,
        element: Optional[
            Union[reflex.vars.Var[Type[Component]], Type[Component]]
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
        on_change: Optional[
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
    ) -> "DebounceInput":
        """Create a DebounceInput component.

        Carry first child props directly on this tag.

        Since react-debounce-input wants to create and manage the underlying
        input component itself, we carry all props, events, and styles from
        the child, and then neuter the child's render method so it produces no output.

        Args:
            children: The child component to wrap.
            props: The component props.

        Returns:
            The DebounceInput component.

        Raises:
            RuntimeError: unless exactly one child element is provided.
            ValueError: if the child element does not have an on_change handler.
        """
        ...

debounce_input = DebounceInput.create
