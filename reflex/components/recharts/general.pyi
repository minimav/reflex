"""Stub file for reflex/components/recharts/general.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Dict, List, Union
from reflex.components.component import MemoizationLeaf
from reflex.event import EventHandler
from reflex.vars import Var
from .recharts import (
    LiteralAnimationEasing,
    LiteralIconType,
    LiteralLayout,
    LiteralLegendAlign,
    LiteralPosition,
    LiteralVerticalAlign,
    Recharts,
)

class ResponsiveContainer(Recharts, MemoizationLeaf):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        aspect: Optional[Union[reflex.vars.Var[int], int]] = None,
        width: Optional[Union[reflex.vars.Var[Union[int, str]], int, str]] = None,
        height: Optional[Union[reflex.vars.Var[Union[int, str]], int, str]] = None,
        min_width: Optional[Union[reflex.vars.Var[int], int]] = None,
        min_height: Optional[Union[reflex.vars.Var[int], int]] = None,
        debounce: Optional[Union[reflex.vars.Var[int], int]] = None,
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
    ) -> "ResponsiveContainer":
        """Create a new memoization leaf component.

        Args:
            *children: The children of the component.
            aspect: The aspect ratio of the container. The final aspect ratio of the SVG element will be (width / height) * aspect. Number
            width: The width of chart container. Can be a number or string
            height: The height of chart container. Number
            min_width: The minimum width of chart container.
            min_height: The minimum height of chart container. Number
            debounce: If specified a positive number, debounced function will be used to handle the resize event.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The memoization leaf
        """
        ...

class Legend(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        width: Optional[Union[reflex.vars.Var[int], int]] = None,
        height: Optional[Union[reflex.vars.Var[int], int]] = None,
        layout: Optional[
            Union[
                reflex.vars.Var[Literal["horizontal", "vertical"]],
                Literal["horizontal", "vertical"],
            ]
        ] = None,
        align: Optional[
            Union[
                reflex.vars.Var[Literal["left", "center", "right"]],
                Literal["left", "center", "right"],
            ]
        ] = None,
        vertical_align: Optional[
            Union[
                reflex.vars.Var[Literal["top", "middle", "bottom"]],
                Literal["top", "middle", "bottom"],
            ]
        ] = None,
        icon_size: Optional[Union[reflex.vars.Var[int], int]] = None,
        icon_type: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "line",
                        "plainline",
                        "square",
                        "rect",
                        "circle",
                        "cross",
                        "diamond",
                        "star",
                        "triangle",
                        "wye",
                    ]
                ],
                Literal[
                    "line",
                    "plainline",
                    "square",
                    "rect",
                    "circle",
                    "cross",
                    "diamond",
                    "star",
                    "triangle",
                    "wye",
                ],
            ]
        ] = None,
        chart_width: Optional[Union[reflex.vars.Var[int], int]] = None,
        chart_height: Optional[Union[reflex.vars.Var[int], int]] = None,
        margin: Optional[Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]] = None,
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
    ) -> "Legend":
        """Create the component.

        Args:
            *children: The children of the component.
            width: The width of legend container. Number
            height: The height of legend container. Number
            layout: The layout of legend items. 'horizontal' | 'vertical'
            align: The alignment of legend items in 'horizontal' direction, which can be 'left', 'center', 'right'.
            vertical_align: The alignment of legend items in 'vertical' direction, which can be 'top', 'middle', 'bottom'.
            icon_size: The size of icon in each legend item.
            icon_type: The type of icon in each legend item. 'line' | 'plainline' | 'square' | 'rect' | 'circle' | 'cross' | 'diamond' | 'star' | 'triangle' | 'wye'
            chart_width: The width of chart container, usually calculated internally.
            chart_height: The height of chart container, usually calculated internally.
            margin: The margin of chart container, usually calculated internally.
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

class GraphingTooltip(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        separator: Optional[Union[reflex.vars.Var[str], str]] = None,
        offset: Optional[Union[reflex.vars.Var[int], int]] = None,
        filter_null: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        cursor: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        view_box: Optional[
            Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]
        ] = None,
        item_style: Optional[
            Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]
        ] = None,
        wrapper_style: Optional[
            Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]
        ] = None,
        content_style: Optional[
            Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]
        ] = None,
        label_style: Optional[
            Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]
        ] = None,
        allow_escape_view_box: Optional[
            Union[reflex.vars.Var[Dict[str, bool]], Dict[str, bool]]
        ] = None,
        active: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        position: Optional[
            Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]
        ] = None,
        coordinate: Optional[
            Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]
        ] = None,
        is_animation_active: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        animation_duration: Optional[Union[reflex.vars.Var[int], int]] = None,
        animation_easing: Optional[
            Union[
                reflex.vars.Var[
                    Literal["ease", "ease-in", "ease-out", "ease-in-out", "linear"]
                ],
                Literal["ease", "ease-in", "ease-out", "ease-in-out", "linear"],
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
    ) -> "GraphingTooltip":
        """Create the component.

        Args:
            *children: The children of the component.
            separator: The separator between name and value.
            offset: The offset size of tooltip. Number
            filter_null: When an item of the payload has value null or undefined, this item won't be displayed.
            cursor: If set false, no cursor will be drawn when tooltip is active.
            view_box: The box of viewing area, which has the shape of {x: someVal, y: someVal, width: someVal, height: someVal}, usually calculated internally.
            item_style: The style of default tooltip content item which is a li element. DEFAULT: {}
            wrapper_style: The style of tooltip wrapper which is a dom element. DEFAULT: {}
            content_style: The style of tooltip content which is a dom element. DEFAULT: {}
            label_style: The style of default tooltip label which is a p element. DEFAULT: {}
            allow_escape_view_box: This option allows the tooltip to extend beyond the viewBox of the chart itself. DEFAULT: { x: false, y: false }
            active: If set true, the tooltip is displayed. If set false, the tooltip is hidden, usually calculated internally.
            position: If this field is set, the tooltip position will be fixed and will not move anymore.
            coordinate: The coordinate of tooltip which is usually calculated internally.
            is_animation_active: If set false, animation of tooltip will be disabled. DEFAULT: true in CSR, and false in SSR
            animation_duration: Specifies the duration of animation, the unit of this option is ms. DEFAULT: 1500
            animation_easing: The type of easing function. DEFAULT: 'ease'
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

class Label(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        view_box: Optional[
            Union[reflex.vars.Var[Dict[str, Any]], Dict[str, Any]]
        ] = None,
        value: Optional[Union[reflex.vars.Var[str], str]] = None,
        offset: Optional[Union[reflex.vars.Var[int], int]] = None,
        position: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "top",
                        "left",
                        "right",
                        "bottom",
                        "inside",
                        "outside",
                        "insideLeft",
                        "insideRight",
                        "insideTop",
                        "insideBottom",
                        "insideTopLeft",
                        "insideBottomLeft",
                        "insideTopRight",
                        "insideBottomRight",
                        "insideStart",
                        "insideEnd",
                        "end",
                        "center",
                    ]
                ],
                Literal[
                    "top",
                    "left",
                    "right",
                    "bottom",
                    "inside",
                    "outside",
                    "insideLeft",
                    "insideRight",
                    "insideTop",
                    "insideBottom",
                    "insideTopLeft",
                    "insideBottomLeft",
                    "insideTopRight",
                    "insideBottomRight",
                    "insideStart",
                    "insideEnd",
                    "end",
                    "center",
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
    ) -> "Label":
        """Create the component.

        Args:
            *children: The children of the component.
            view_box: The box of viewing area, which has the shape of {x: someVal, y: someVal, width: someVal, height: someVal}, usually calculated internally.
            value: The value of label, which can be specified by this props or the children of <Label />
            offset: The offset of label which can be specified by this props or the children of <Label />
            position: The position of label which can be specified by this props or the children of <Label />
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

class LabelList(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        data_key: Optional[Union[reflex.vars.Var[Union[int, str]], str, int]] = None,
        position: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "top",
                        "left",
                        "right",
                        "bottom",
                        "inside",
                        "outside",
                        "insideLeft",
                        "insideRight",
                        "insideTop",
                        "insideBottom",
                        "insideTopLeft",
                        "insideBottomLeft",
                        "insideTopRight",
                        "insideBottomRight",
                        "insideStart",
                        "insideEnd",
                        "end",
                        "center",
                    ]
                ],
                Literal[
                    "top",
                    "left",
                    "right",
                    "bottom",
                    "inside",
                    "outside",
                    "insideLeft",
                    "insideRight",
                    "insideTop",
                    "insideBottom",
                    "insideTopLeft",
                    "insideBottomLeft",
                    "insideTopRight",
                    "insideBottomRight",
                    "insideStart",
                    "insideEnd",
                    "end",
                    "center",
                ],
            ]
        ] = None,
        offset: Optional[Union[reflex.vars.Var[int], int]] = None,
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
    ) -> "LabelList":
        """Create the component.

        Args:
            *children: The children of the component.
            data_key: The key of a group of label values in data.
            position: The position of each label relative to it view box。"Top" | "left" | "right" | "bottom" | "inside" | "outside" | "insideLeft" | "insideRight" | "insideTop" | "insideBottom" | "insideTopLeft" | "insideBottomLeft" | "insideTopRight" | "insideBottomRight" | "insideStart" | "insideEnd" | "end" | "center"
            offset: The offset to the specified "position"
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

responsive_container = ResponsiveContainer.create
legend = Legend.create
graphing_tooltip = GraphingTooltip.create
label = Label.create
label_list = LabelList.create
