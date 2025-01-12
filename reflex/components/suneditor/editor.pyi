"""Stub file for reflex/components/suneditor/editor.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
import enum
from typing import Dict, List, Literal, Optional, Union
from reflex.base import Base
from reflex.components.component import Component, NoSSRComponent
from reflex.event import EventHandler
from reflex.utils.format import to_camel_case
from reflex.utils.imports import ImportDict, ImportVar
from reflex.vars import Var

class EditorButtonList(list, enum.Enum):
    BASIC = [["font", "fontSize"], ["fontColor"], ["horizontalRule"], ["link", "image"]]
    FORMATTING = [
        ["undo", "redo"],
        ["bold", "underline", "italic", "strike", "subscript", "superscript"],
        ["removeFormat"],
        ["outdent", "indent"],
        ["fullScreen", "showBlocks", "codeView"],
        ["preview", "print"],
    ]
    COMPLEX = [
        ["undo", "redo"],
        ["font", "fontSize", "formatBlock"],
        ["bold", "underline", "italic", "strike", "subscript", "superscript"],
        ["removeFormat"],
        "/",
        ["fontColor", "hiliteColor"],
        ["outdent", "indent"],
        ["align", "horizontalRule", "list", "table"],
        ["link", "image", "video"],
        ["fullScreen", "showBlocks", "codeView"],
        ["preview", "print"],
        ["save", "template"],
    ]

class EditorOptions(Base):
    default_tag: Optional[str]
    mode: Optional[str]
    rtl: Optional[bool]
    button_list: Optional[List[Union[List[str], str]]]

class Editor(NoSSRComponent):
    def add_imports(self) -> ImportDict: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        lang: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal[
                            "en",
                            "da",
                            "de",
                            "es",
                            "fr",
                            "ja",
                            "ko",
                            "pt_br",
                            "ru",
                            "zh_cn",
                            "ro",
                            "pl",
                            "ckb",
                            "lv",
                            "se",
                            "ua",
                            "he",
                            "it",
                        ],
                        dict,
                    ]
                ],
                Literal[
                    "en",
                    "da",
                    "de",
                    "es",
                    "fr",
                    "ja",
                    "ko",
                    "pt_br",
                    "ru",
                    "zh_cn",
                    "ro",
                    "pl",
                    "ckb",
                    "lv",
                    "se",
                    "ua",
                    "he",
                    "it",
                ],
                dict,
            ]
        ] = None,
        name: Optional[Union[reflex.vars.Var[str], str]] = None,
        default_value: Optional[Union[reflex.vars.Var[str], str]] = None,
        width: Optional[Union[reflex.vars.Var[str], str]] = None,
        height: Optional[Union[reflex.vars.Var[str], str]] = None,
        placeholder: Optional[Union[reflex.vars.Var[str], str]] = None,
        auto_focus: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        set_options: Optional[Union[reflex.vars.Var[Dict], Dict]] = None,
        set_all_plugins: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        set_contents: Optional[Union[reflex.vars.Var[str], str]] = None,
        append_contents: Optional[Union[reflex.vars.Var[str], str]] = None,
        set_default_style: Optional[Union[reflex.vars.Var[str], str]] = None,
        disable: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        hide: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        hide_toolbar: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        disable_toolbar: Optional[Union[reflex.vars.Var[bool], bool]] = None,
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
        on_copy: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_cut: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_input: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_load: Optional[
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
        on_paste: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_resize_editor: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        toggle_code_view: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        toggle_full_screen: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Editor":
        """Create an instance of Editor. No children allowed.

        Args:
            set_options(Optional[EditorOptions]): Configuration object to further configure the instance.
            lang: Language of the editor.  Alternatively to a string, a dict of your language can be passed to this prop.  Please refer to the library docs for this.  options: "en" | "da" | "de" | "es" | "fr" | "ja" | "ko" | "pt_br" |   "ru" | "zh_cn" | "ro" | "pl" | "ckb" | "lv" | "se" | "ua" | "he" | "it"  default : "en"
            name: This is used to set the HTML form name of the editor.  This means on HTML form submission,  it will be submitted together with contents of the editor by the name provided.
            default_value: Sets the default value of the editor.  This is useful if you don't want the on_change method to be called on render.  If you want the on_change method to be called on render please use the set_contents prop
            width: Sets the width of the editor.  px and percentage values are accepted, eg width="100%" or width="500px"  default: 100%
            height: Sets the height of the editor.  px and percentage values are accepted, eg height="100%" or height="100px"
            placeholder: Sets the placeholder of the editor.
            auto_focus: Should the editor receive focus when initialized?
            set_options: Pass an EditorOptions instance to modify the behaviour of Editor even more.
            set_all_plugins: Whether all SunEditor plugins should be loaded.  default: True
            set_contents: Set the content of the editor.  Note: To set the initial contents of the editor  without calling the on_change event,  please use the default_value prop.  set_contents is used to set the contents of the editor programmatically.  You must be aware that, when the set_contents's prop changes,  the on_change event is triggered.
            append_contents: Append editor content
            set_default_style: Sets the default style of the editor's edit area
            disable: Disable the editor  default: False
            hide: Hide the editor  default: False
            hide_toolbar: Hide the editor toolbar  default: False
            disable_toolbar: Disable the editor toolbar  default: False
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Any properties to be passed to the Editor

        Returns:
            An Editor instance.

        Raises:
            ValueError: If set_options is a state Var.
        """
        ...
