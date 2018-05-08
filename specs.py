import z3
from libirpy import util
import datatype.datatypes as dt


#specification

    
def inc(old):
    cond = z3.ULT(old.counter, dt.MAX_UINT)
    new = old.copy()
    new.counter += 1
    return cond, util.If(cond, new, old)

def dec(old):
    cond = z3.UGT(old.counter, 0)
    new = old.copy()
    new.counter -= 1
    return cond, util.If(cond, new, old)

def iszero(old):
    if old.counter == 0:
        return z3.BoolVal(True), old
    else:
        return z3.BoolVal(False), old

def state_equiv(ctx, state):
	conj = []
	conj.append(state.counter == util.global_value(ctx, '@counter'))
	return z3.And(*conj)
