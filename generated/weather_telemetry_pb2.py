# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weather_telemetry.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17weather_telemetry.proto\x12\x0bweatherdata\"\x9d\x01\n\x10WeatherTelemetry\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\x12\x10\n\x08humidity\x18\x03 \x01(\x01\x12\x11\n\twindSpeed\x18\x04 \x01(\x01\x12\x15\n\rwindDirection\x18\x05 \x01(\x01\x12\x10\n\x08pressure\x18\x06 \x01(\x01\x12\x13\n\x0bwaterAmount\x18\x07 \x01(\x01\x42\x0fZ\r./weatherdatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'weather_telemetry_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\r./weatherdata'
  _globals['_WEATHERTELEMETRY']._serialized_start=41
  _globals['_WEATHERTELEMETRY']._serialized_end=198
# @@protoc_insertion_point(module_scope)
