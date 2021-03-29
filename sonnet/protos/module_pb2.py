# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="module.proto",
    package="sonnet",
    syntax="proto3",
    serialized_pb=_b(
        '\n\x0cmodule.proto\x12\x06sonnet"\xb1\x05\n\nNestedData\x12\x0f\n\x05value\x18\x01 \x01(\tH\x00\x12\'\n\x04list\x18\x02 \x01(\x0b\x32\x17.sonnet.NestedData.ListH\x00\x12)\n\x05tuple\x18\x03 \x01(\x0b\x32\x18.sonnet.NestedData.TupleH\x00\x12\'\n\x04\x64ict\x18\x04 \x01(\x0b\x32\x17.sonnet.NestedData.DictH\x00\x12\x34\n\x0bnamed_tuple\x18\x05 \x01(\x0b\x32\x1d.sonnet.NestedData.NamedTupleH\x00\x12\x36\n\x0cspecial_type\x18\x06 \x01(\x0b\x32\x1e.sonnet.NestedData.SpecialTypeH\x00\x1a)\n\x05Tuple\x12 \n\x04list\x18\x01 \x03(\x0b\x32\x12.sonnet.NestedData\x1a(\n\x04List\x12 \n\x04list\x18\x01 \x03(\x0b\x32\x12.sonnet.NestedData\x1au\n\x04\x44ict\x12-\n\x03map\x18\x01 \x03(\x0b\x32 .sonnet.NestedData.Dict.MapEntry\x1a>\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.sonnet.NestedData:\x02\x38\x01\x1a\x8f\x01\n\nNamedTuple\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x03map\x18\x02 \x03(\x0b\x32&.sonnet.NestedData.NamedTuple.MapEntry\x1a>\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.sonnet.NestedData:\x02\x38\x01\x1a?\n\x0bSpecialType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12"\n\x06object\x18\x02 \x01(\x0b\x32\x12.sonnet.NestedDataB\x08\n\x06one_of"\x82\x02\n\x0cSonnetModule\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x12\n\nscope_name\x18\x02 \x01(\t\x12\x12\n\nclass_name\x18\x04 \x01(\t\x12\x43\n\x13\x63onnected_subgraphs\x18\x03 \x03(\x0b\x32&.sonnet.SonnetModule.ConnectedSubgraph\x1ap\n\x11\x43onnectedSubgraph\x12\x12\n\nname_scope\x18\x01 \x01(\t\x12"\n\x06inputs\x18\x02 \x01(\x0b\x32\x12.sonnet.NestedData\x12#\n\x07outputs\x18\x03 \x01(\x0b\x32\x12.sonnet.NestedDatab\x06proto3'  # noqa: E501
    ),
)


_NESTEDDATA_TUPLE = _descriptor.Descriptor(
    name="Tuple",
    full_name="sonnet.NestedData.Tuple",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="list",
            full_name="sonnet.NestedData.Tuple.list",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=291,
    serialized_end=332,
)

_NESTEDDATA_LIST = _descriptor.Descriptor(
    name="List",
    full_name="sonnet.NestedData.List",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="list",
            full_name="sonnet.NestedData.List.list",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=334,
    serialized_end=374,
)

_NESTEDDATA_DICT_MAPENTRY = _descriptor.Descriptor(
    name="MapEntry",
    full_name="sonnet.NestedData.Dict.MapEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="sonnet.NestedData.Dict.MapEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="sonnet.NestedData.Dict.MapEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b("8\001")),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=431,
    serialized_end=493,
)

_NESTEDDATA_DICT = _descriptor.Descriptor(
    name="Dict",
    full_name="sonnet.NestedData.Dict",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="map",
            full_name="sonnet.NestedData.Dict.map",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[
        _NESTEDDATA_DICT_MAPENTRY,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=376,
    serialized_end=493,
)

_NESTEDDATA_NAMEDTUPLE_MAPENTRY = _descriptor.Descriptor(
    name="MapEntry",
    full_name="sonnet.NestedData.NamedTuple.MapEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="sonnet.NestedData.NamedTuple.MapEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="sonnet.NestedData.NamedTuple.MapEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b("8\001")),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=431,
    serialized_end=493,
)

_NESTEDDATA_NAMEDTUPLE = _descriptor.Descriptor(
    name="NamedTuple",
    full_name="sonnet.NestedData.NamedTuple",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="sonnet.NestedData.NamedTuple.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="map",
            full_name="sonnet.NestedData.NamedTuple.map",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[
        _NESTEDDATA_NAMEDTUPLE_MAPENTRY,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=496,
    serialized_end=639,
)

_NESTEDDATA_SPECIALTYPE = _descriptor.Descriptor(
    name="SpecialType",
    full_name="sonnet.NestedData.SpecialType",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="sonnet.NestedData.SpecialType.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="object",
            full_name="sonnet.NestedData.SpecialType.object",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=641,
    serialized_end=704,
)

_NESTEDDATA = _descriptor.Descriptor(
    name="NestedData",
    full_name="sonnet.NestedData",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="sonnet.NestedData.value",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="list",
            full_name="sonnet.NestedData.list",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="tuple",
            full_name="sonnet.NestedData.tuple",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="dict",
            full_name="sonnet.NestedData.dict",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="named_tuple",
            full_name="sonnet.NestedData.named_tuple",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="special_type",
            full_name="sonnet.NestedData.special_type",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[
        _NESTEDDATA_TUPLE,
        _NESTEDDATA_LIST,
        _NESTEDDATA_DICT,
        _NESTEDDATA_NAMEDTUPLE,
        _NESTEDDATA_SPECIALTYPE,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="one_of",
            full_name="sonnet.NestedData.one_of",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=25,
    serialized_end=714,
)


_SONNETMODULE_CONNECTEDSUBGRAPH = _descriptor.Descriptor(
    name="ConnectedSubgraph",
    full_name="sonnet.SonnetModule.ConnectedSubgraph",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name_scope",
            full_name="sonnet.SonnetModule.ConnectedSubgraph.name_scope",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="inputs",
            full_name="sonnet.SonnetModule.ConnectedSubgraph.inputs",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="outputs",
            full_name="sonnet.SonnetModule.ConnectedSubgraph.outputs",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=863,
    serialized_end=975,
)

_SONNETMODULE = _descriptor.Descriptor(
    name="SonnetModule",
    full_name="sonnet.SonnetModule",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="module_name",
            full_name="sonnet.SonnetModule.module_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="scope_name",
            full_name="sonnet.SonnetModule.scope_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="class_name",
            full_name="sonnet.SonnetModule.class_name",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="connected_subgraphs",
            full_name="sonnet.SonnetModule.connected_subgraphs",
            index=3,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[
        _SONNETMODULE_CONNECTEDSUBGRAPH,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=717,
    serialized_end=975,
)

_NESTEDDATA_TUPLE.fields_by_name["list"].message_type = _NESTEDDATA
_NESTEDDATA_TUPLE.containing_type = _NESTEDDATA
_NESTEDDATA_LIST.fields_by_name["list"].message_type = _NESTEDDATA
_NESTEDDATA_LIST.containing_type = _NESTEDDATA
_NESTEDDATA_DICT_MAPENTRY.fields_by_name["value"].message_type = _NESTEDDATA
_NESTEDDATA_DICT_MAPENTRY.containing_type = _NESTEDDATA_DICT
_NESTEDDATA_DICT.fields_by_name["map"].message_type = _NESTEDDATA_DICT_MAPENTRY
_NESTEDDATA_DICT.containing_type = _NESTEDDATA
_NESTEDDATA_NAMEDTUPLE_MAPENTRY.fields_by_name["value"].message_type = _NESTEDDATA
_NESTEDDATA_NAMEDTUPLE_MAPENTRY.containing_type = _NESTEDDATA_NAMEDTUPLE
_NESTEDDATA_NAMEDTUPLE.fields_by_name["map"].message_type = _NESTEDDATA_NAMEDTUPLE_MAPENTRY
_NESTEDDATA_NAMEDTUPLE.containing_type = _NESTEDDATA
_NESTEDDATA_SPECIALTYPE.fields_by_name["object"].message_type = _NESTEDDATA
_NESTEDDATA_SPECIALTYPE.containing_type = _NESTEDDATA
_NESTEDDATA.fields_by_name["list"].message_type = _NESTEDDATA_LIST
_NESTEDDATA.fields_by_name["tuple"].message_type = _NESTEDDATA_TUPLE
_NESTEDDATA.fields_by_name["dict"].message_type = _NESTEDDATA_DICT
_NESTEDDATA.fields_by_name["named_tuple"].message_type = _NESTEDDATA_NAMEDTUPLE
_NESTEDDATA.fields_by_name["special_type"].message_type = _NESTEDDATA_SPECIALTYPE
_NESTEDDATA.oneofs_by_name["one_of"].fields.append(_NESTEDDATA.fields_by_name["value"])
_NESTEDDATA.fields_by_name["value"].containing_oneof = _NESTEDDATA.oneofs_by_name["one_of"]
_NESTEDDATA.oneofs_by_name["one_of"].fields.append(_NESTEDDATA.fields_by_name["list"])
_NESTEDDATA.fields_by_name["list"].containing_oneof = _NESTEDDATA.oneofs_by_name["one_of"]
_NESTEDDATA.oneofs_by_name["one_of"].fields.append(_NESTEDDATA.fields_by_name["tuple"])
_NESTEDDATA.fields_by_name["tuple"].containing_oneof = _NESTEDDATA.oneofs_by_name["one_of"]
_NESTEDDATA.oneofs_by_name["one_of"].fields.append(_NESTEDDATA.fields_by_name["dict"])
_NESTEDDATA.fields_by_name["dict"].containing_oneof = _NESTEDDATA.oneofs_by_name["one_of"]
_NESTEDDATA.oneofs_by_name["one_of"].fields.append(_NESTEDDATA.fields_by_name["named_tuple"])
_NESTEDDATA.fields_by_name["named_tuple"].containing_oneof = _NESTEDDATA.oneofs_by_name["one_of"]
_NESTEDDATA.oneofs_by_name["one_of"].fields.append(_NESTEDDATA.fields_by_name["special_type"])
_NESTEDDATA.fields_by_name["special_type"].containing_oneof = _NESTEDDATA.oneofs_by_name["one_of"]
_SONNETMODULE_CONNECTEDSUBGRAPH.fields_by_name["inputs"].message_type = _NESTEDDATA
_SONNETMODULE_CONNECTEDSUBGRAPH.fields_by_name["outputs"].message_type = _NESTEDDATA
_SONNETMODULE_CONNECTEDSUBGRAPH.containing_type = _SONNETMODULE
_SONNETMODULE.fields_by_name["connected_subgraphs"].message_type = _SONNETMODULE_CONNECTEDSUBGRAPH
DESCRIPTOR.message_types_by_name["NestedData"] = _NESTEDDATA
DESCRIPTOR.message_types_by_name["SonnetModule"] = _SONNETMODULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NestedData = _reflection.GeneratedProtocolMessageType(
    "NestedData",
    (_message.Message,),
    dict(
        Tuple=_reflection.GeneratedProtocolMessageType(
            "Tuple",
            (_message.Message,),
            dict(
                DESCRIPTOR=_NESTEDDATA_TUPLE,
                __module__="module_pb2"
                # @@protoc_insertion_point(class_scope:sonnet.NestedData.Tuple)
            ),
        ),
        List=_reflection.GeneratedProtocolMessageType(
            "List",
            (_message.Message,),
            dict(
                DESCRIPTOR=_NESTEDDATA_LIST,
                __module__="module_pb2"
                # @@protoc_insertion_point(class_scope:sonnet.NestedData.List)
            ),
        ),
        Dict=_reflection.GeneratedProtocolMessageType(
            "Dict",
            (_message.Message,),
            dict(
                MapEntry=_reflection.GeneratedProtocolMessageType(
                    "MapEntry",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_NESTEDDATA_DICT_MAPENTRY,
                        __module__="module_pb2"
                        # @@protoc_insertion_point(class_scope:sonnet.NestedData.Dict.MapEntry)
                    ),
                ),
                DESCRIPTOR=_NESTEDDATA_DICT,
                __module__="module_pb2"
                # @@protoc_insertion_point(class_scope:sonnet.NestedData.Dict)
            ),
        ),
        NamedTuple=_reflection.GeneratedProtocolMessageType(
            "NamedTuple",
            (_message.Message,),
            dict(
                MapEntry=_reflection.GeneratedProtocolMessageType(
                    "MapEntry",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_NESTEDDATA_NAMEDTUPLE_MAPENTRY,
                        __module__="module_pb2"
                        # @@protoc_insertion_point(class_scope:sonnet.NestedData.NamedTuple.MapEntry)
                    ),
                ),
                DESCRIPTOR=_NESTEDDATA_NAMEDTUPLE,
                __module__="module_pb2"
                # @@protoc_insertion_point(class_scope:sonnet.NestedData.NamedTuple)
            ),
        ),
        SpecialType=_reflection.GeneratedProtocolMessageType(
            "SpecialType",
            (_message.Message,),
            dict(
                DESCRIPTOR=_NESTEDDATA_SPECIALTYPE,
                __module__="module_pb2"
                # @@protoc_insertion_point(class_scope:sonnet.NestedData.SpecialType)
            ),
        ),
        DESCRIPTOR=_NESTEDDATA,
        __module__="module_pb2"
        # @@protoc_insertion_point(class_scope:sonnet.NestedData)
    ),
)
_sym_db.RegisterMessage(NestedData)
_sym_db.RegisterMessage(NestedData.Tuple)
_sym_db.RegisterMessage(NestedData.List)
_sym_db.RegisterMessage(NestedData.Dict)
_sym_db.RegisterMessage(NestedData.Dict.MapEntry)
_sym_db.RegisterMessage(NestedData.NamedTuple)
_sym_db.RegisterMessage(NestedData.NamedTuple.MapEntry)
_sym_db.RegisterMessage(NestedData.SpecialType)

SonnetModule = _reflection.GeneratedProtocolMessageType(
    "SonnetModule",
    (_message.Message,),
    dict(
        ConnectedSubgraph=_reflection.GeneratedProtocolMessageType(
            "ConnectedSubgraph",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SONNETMODULE_CONNECTEDSUBGRAPH,
                __module__="module_pb2"
                # @@protoc_insertion_point(class_scope:sonnet.SonnetModule.ConnectedSubgraph)
            ),
        ),
        DESCRIPTOR=_SONNETMODULE,
        __module__="module_pb2"
        # @@protoc_insertion_point(class_scope:sonnet.SonnetModule)
    ),
)
_sym_db.RegisterMessage(SonnetModule)
_sym_db.RegisterMessage(SonnetModule.ConnectedSubgraph)


_NESTEDDATA_DICT_MAPENTRY.has_options = True
_NESTEDDATA_DICT_MAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b("8\001"))
_NESTEDDATA_NAMEDTUPLE_MAPENTRY.has_options = True
_NESTEDDATA_NAMEDTUPLE_MAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b("8\001"))
# @@protoc_insertion_point(module_scope)
