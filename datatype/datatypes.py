import sys
import z3
import copy

import libirpy
from libirpy import util
from base import BaseStruct, Struct, Map, Refcnt, Refcnt2


def _populate_enums():
    module = sys.modules[__name__]
    ctx = libirpy.newctx()
    import counter
    counter._init_metadata(ctx)
    for k, v in ctx.metadata.items():
        if isinstance(v, tuple) and v[0] == 'DICompositeType':
            if v[1].get('tag') == 'DW_TAG_enumeration_type':
                name = v[1].get('name')
                size = v[1].get('size')
                elements = v[1].get('elements')

                if name is None or size is None or elements is None:
                    continue

                setattr(module, name + '_t', z3.BitVecSort(size))
                enum = {}

                for element in ctx.metadata.get(elements):
                    element = ctx.metadata.get(element)
                    assert element[0] == 'DIEnumerator'
                    element_name = element[1].get('name')
                    element_value = element[1].get('value')
                    enum[element_name] = z3.BitVecVal(element_value, size)

                setattr(module, name, type(name, (), enum))


# These are populated from llvm metadata info
page_type_t = None
file_type_t = None
proc_state_t = None
intremap_state_t = None


# Fetch the enums from the llvm metadata and populate this module with their values
_populate_enums()


#assert page_type_t is not None
#assert file_type_t is not None
#assert proc_state_t is not None

bool_t = z3.BoolSort()

size_t = z3.BitVecSort(64)
uint64_t = z3.BitVecSort(64)
uint32_t = z3.BitVecSort(32)
uint16_t = z3.BitVecSort(16)
uint8_t = z3.BitVecSort(8)

ssize_t = z3.BitVecSort(64)
int64_t = z3.BitVecSort(64)
int32_t = z3.BitVecSort(32)
int16_t = z3.BitVecSort(16)
int8_t = z3.BitVecSort(8)
int = int32_t
MAX_UINT = z3.BitVecVal(100,32)
"""
Global machine state
"""
class CounterState(object):
	def __init__(self):        	
        	self.counter = z3.BitVecVal(0,32)
	def copy(self):
		return copy.deepcopy(self)

