# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: component_information/component_information.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1component_information/component_information.proto\x12 mavsdk.rpc.component_information\x1a\x14mavsdk_options.proto\"\xc7\x01\n\nFloatParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11short_description\x18\x02 \x01(\t\x12\x18\n\x10long_description\x18\x03 \x01(\t\x12\x0c\n\x04unit\x18\x04 \x01(\t\x12\x16\n\x0e\x64\x65\x63imal_places\x18\x05 \x01(\x05\x12\x13\n\x0bstart_value\x18\x06 \x01(\x02\x12\x15\n\rdefault_value\x18\x07 \x01(\x02\x12\x11\n\tmin_value\x18\x08 \x01(\x02\x12\x11\n\tmax_value\x18\t \x01(\x02\"\x1a\n\x18\x41\x63\x63\x65ssFloatParamsRequest\"\xbd\x01\n\x19\x41\x63\x63\x65ssFloatParamsResponse\x12\x62\n\x1c\x63omponent_information_result\x18\x01 \x01(\x0b\x32<.mavsdk.rpc.component_information.ComponentInformationResult\x12<\n\x06params\x18\x02 \x03(\x0b\x32,.mavsdk.rpc.component_information.FloatParam\"/\n\x10\x46loatParamUpdate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"\x1c\n\x1aSubscribeFloatParamRequest\"^\n\x12\x46loatParamResponse\x12H\n\x0cparam_update\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.component_information.FloatParamUpdate\"\xcd\x01\n\x1a\x43omponentInformationResult\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.mavsdk.rpc.component_information.ComponentInformationResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"F\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x03\x32\xc6\x02\n\x1b\x43omponentInformationService\x12\x92\x01\n\x11\x41\x63\x63\x65ssFloatParams\x12:.mavsdk.rpc.component_information.AccessFloatParamsRequest\x1a;.mavsdk.rpc.component_information.AccessFloatParamsResponse\"\x04\x80\xb5\x18\x01\x12\x91\x01\n\x13SubscribeFloatParam\x12<.mavsdk.rpc.component_information.SubscribeFloatParamRequest\x1a\x34.mavsdk.rpc.component_information.FloatParamResponse\"\x04\x80\xb5\x18\x00\x30\x01\x42<\n\x1fio.mavsdk.component_informationB\x19\x43omponentInformationProtob\x06proto3')



_FLOATPARAM = DESCRIPTOR.message_types_by_name['FloatParam']
_ACCESSFLOATPARAMSREQUEST = DESCRIPTOR.message_types_by_name['AccessFloatParamsRequest']
_ACCESSFLOATPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['AccessFloatParamsResponse']
_FLOATPARAMUPDATE = DESCRIPTOR.message_types_by_name['FloatParamUpdate']
_SUBSCRIBEFLOATPARAMREQUEST = DESCRIPTOR.message_types_by_name['SubscribeFloatParamRequest']
_FLOATPARAMRESPONSE = DESCRIPTOR.message_types_by_name['FloatParamResponse']
_COMPONENTINFORMATIONRESULT = DESCRIPTOR.message_types_by_name['ComponentInformationResult']
_COMPONENTINFORMATIONRESULT_RESULT = _COMPONENTINFORMATIONRESULT.enum_types_by_name['Result']
FloatParam = _reflection.GeneratedProtocolMessageType('FloatParam', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAM,
  '__module__' : 'component_information.component_information_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information.FloatParam)
  })
_sym_db.RegisterMessage(FloatParam)

AccessFloatParamsRequest = _reflection.GeneratedProtocolMessageType('AccessFloatParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSFLOATPARAMSREQUEST,
  '__module__' : 'component_information.component_information_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information.AccessFloatParamsRequest)
  })
_sym_db.RegisterMessage(AccessFloatParamsRequest)

AccessFloatParamsResponse = _reflection.GeneratedProtocolMessageType('AccessFloatParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSFLOATPARAMSRESPONSE,
  '__module__' : 'component_information.component_information_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information.AccessFloatParamsResponse)
  })
_sym_db.RegisterMessage(AccessFloatParamsResponse)

FloatParamUpdate = _reflection.GeneratedProtocolMessageType('FloatParamUpdate', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAMUPDATE,
  '__module__' : 'component_information.component_information_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information.FloatParamUpdate)
  })
_sym_db.RegisterMessage(FloatParamUpdate)

SubscribeFloatParamRequest = _reflection.GeneratedProtocolMessageType('SubscribeFloatParamRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEFLOATPARAMREQUEST,
  '__module__' : 'component_information.component_information_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information.SubscribeFloatParamRequest)
  })
_sym_db.RegisterMessage(SubscribeFloatParamRequest)

FloatParamResponse = _reflection.GeneratedProtocolMessageType('FloatParamResponse', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAMRESPONSE,
  '__module__' : 'component_information.component_information_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information.FloatParamResponse)
  })
_sym_db.RegisterMessage(FloatParamResponse)

ComponentInformationResult = _reflection.GeneratedProtocolMessageType('ComponentInformationResult', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENTINFORMATIONRESULT,
  '__module__' : 'component_information.component_information_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.component_information.ComponentInformationResult)
  })
_sym_db.RegisterMessage(ComponentInformationResult)

_COMPONENTINFORMATIONSERVICE = DESCRIPTOR.services_by_name['ComponentInformationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037io.mavsdk.component_informationB\031ComponentInformationProto'
  _COMPONENTINFORMATIONSERVICE.methods_by_name['AccessFloatParams']._options = None
  _COMPONENTINFORMATIONSERVICE.methods_by_name['AccessFloatParams']._serialized_options = b'\200\265\030\001'
  _COMPONENTINFORMATIONSERVICE.methods_by_name['SubscribeFloatParam']._options = None
  _COMPONENTINFORMATIONSERVICE.methods_by_name['SubscribeFloatParam']._serialized_options = b'\200\265\030\000'
  _FLOATPARAM._serialized_start=110
  _FLOATPARAM._serialized_end=309
  _ACCESSFLOATPARAMSREQUEST._serialized_start=311
  _ACCESSFLOATPARAMSREQUEST._serialized_end=337
  _ACCESSFLOATPARAMSRESPONSE._serialized_start=340
  _ACCESSFLOATPARAMSRESPONSE._serialized_end=529
  _FLOATPARAMUPDATE._serialized_start=531
  _FLOATPARAMUPDATE._serialized_end=578
  _SUBSCRIBEFLOATPARAMREQUEST._serialized_start=580
  _SUBSCRIBEFLOATPARAMREQUEST._serialized_end=608
  _FLOATPARAMRESPONSE._serialized_start=610
  _FLOATPARAMRESPONSE._serialized_end=704
  _COMPONENTINFORMATIONRESULT._serialized_start=707
  _COMPONENTINFORMATIONRESULT._serialized_end=912
  _COMPONENTINFORMATIONRESULT_RESULT._serialized_start=842
  _COMPONENTINFORMATIONRESULT_RESULT._serialized_end=912
  _COMPONENTINFORMATIONSERVICE._serialized_start=915
  _COMPONENTINFORMATIONSERVICE._serialized_end=1241
# @@protoc_insertion_point(module_scope)