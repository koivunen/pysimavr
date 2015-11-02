# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_hd44780', [dirname(__file__)])
        except ImportError:
            import _hd44780
            return _hd44780
        if fp is not None:
            try:
                _mod = imp.load_module('_hd44780', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _hd44780 = swig_import_helper()
    del swig_import_helper
else:
    import _hd44780
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


IRQ_HD44780_ALL = _hd44780.IRQ_HD44780_ALL
IRQ_HD44780_RS = _hd44780.IRQ_HD44780_RS
IRQ_HD44780_RW = _hd44780.IRQ_HD44780_RW
IRQ_HD44780_E = _hd44780.IRQ_HD44780_E
IRQ_HD44780_D0 = _hd44780.IRQ_HD44780_D0
IRQ_HD44780_D1 = _hd44780.IRQ_HD44780_D1
IRQ_HD44780_D2 = _hd44780.IRQ_HD44780_D2
IRQ_HD44780_D3 = _hd44780.IRQ_HD44780_D3
IRQ_HD44780_D4 = _hd44780.IRQ_HD44780_D4
IRQ_HD44780_D5 = _hd44780.IRQ_HD44780_D5
IRQ_HD44780_D6 = _hd44780.IRQ_HD44780_D6
IRQ_HD44780_D7 = _hd44780.IRQ_HD44780_D7
IRQ_HD44780_INPUT_COUNT = _hd44780.IRQ_HD44780_INPUT_COUNT
IRQ_HD44780_BUSY = _hd44780.IRQ_HD44780_BUSY
IRQ_HD44780_ADDR = _hd44780.IRQ_HD44780_ADDR
IRQ_HD44780_DATA_IN = _hd44780.IRQ_HD44780_DATA_IN
IRQ_HD44780_DATA_OUT = _hd44780.IRQ_HD44780_DATA_OUT
IRQ_HD44780_COUNT = _hd44780.IRQ_HD44780_COUNT
HD44780_FLAG_F = _hd44780.HD44780_FLAG_F
HD44780_FLAG_N = _hd44780.HD44780_FLAG_N
HD44780_FLAG_D_L = _hd44780.HD44780_FLAG_D_L
HD44780_FLAG_R_L = _hd44780.HD44780_FLAG_R_L
HD44780_FLAG_S_C = _hd44780.HD44780_FLAG_S_C
HD44780_FLAG_B = _hd44780.HD44780_FLAG_B
HD44780_FLAG_C = _hd44780.HD44780_FLAG_C
HD44780_FLAG_D = _hd44780.HD44780_FLAG_D
HD44780_FLAG_S = _hd44780.HD44780_FLAG_S
HD44780_FLAG_I_D = _hd44780.HD44780_FLAG_I_D
HD44780_FLAG_LOWNIBBLE = _hd44780.HD44780_FLAG_LOWNIBBLE
HD44780_FLAG_BUSY = _hd44780.HD44780_FLAG_BUSY
HD44780_FLAG_REENTRANT = _hd44780.HD44780_FLAG_REENTRANT
HD44780_FLAG_DIRTY = _hd44780.HD44780_FLAG_DIRTY
HD44780_FLAG_CRAM_DIRTY = _hd44780.HD44780_FLAG_CRAM_DIRTY
VRAM_SIZE = _hd44780.VRAM_SIZE
class hd44780_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hd44780_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hd44780_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["irq"] = _hd44780.hd44780_t_irq_set
    __swig_getmethods__["irq"] = _hd44780.hd44780_t_irq_get
    if _newclass:irq = _swig_property(_hd44780.hd44780_t_irq_get, _hd44780.hd44780_t_irq_set)
    __swig_setmethods__["avr"] = _hd44780.hd44780_t_avr_set
    __swig_getmethods__["avr"] = _hd44780.hd44780_t_avr_get
    if _newclass:avr = _swig_property(_hd44780.hd44780_t_avr_get, _hd44780.hd44780_t_avr_set)
    __swig_setmethods__["w"] = _hd44780.hd44780_t_w_set
    __swig_getmethods__["w"] = _hd44780.hd44780_t_w_get
    if _newclass:w = _swig_property(_hd44780.hd44780_t_w_get, _hd44780.hd44780_t_w_set)
    __swig_setmethods__["h"] = _hd44780.hd44780_t_h_set
    __swig_getmethods__["h"] = _hd44780.hd44780_t_h_get
    if _newclass:h = _swig_property(_hd44780.hd44780_t_h_get, _hd44780.hd44780_t_h_set)
    __swig_setmethods__["cursor"] = _hd44780.hd44780_t_cursor_set
    __swig_getmethods__["cursor"] = _hd44780.hd44780_t_cursor_get
    if _newclass:cursor = _swig_property(_hd44780.hd44780_t_cursor_get, _hd44780.hd44780_t_cursor_set)
    __swig_setmethods__["vram"] = _hd44780.hd44780_t_vram_set
    __swig_getmethods__["vram"] = _hd44780.hd44780_t_vram_get
    if _newclass:vram = _swig_property(_hd44780.hd44780_t_vram_get, _hd44780.hd44780_t_vram_set)
    __swig_setmethods__["pinstate"] = _hd44780.hd44780_t_pinstate_set
    __swig_getmethods__["pinstate"] = _hd44780.hd44780_t_pinstate_get
    if _newclass:pinstate = _swig_property(_hd44780.hd44780_t_pinstate_get, _hd44780.hd44780_t_pinstate_set)
    __swig_setmethods__["datapins"] = _hd44780.hd44780_t_datapins_set
    __swig_getmethods__["datapins"] = _hd44780.hd44780_t_datapins_get
    if _newclass:datapins = _swig_property(_hd44780.hd44780_t_datapins_get, _hd44780.hd44780_t_datapins_set)
    __swig_setmethods__["readpins"] = _hd44780.hd44780_t_readpins_set
    __swig_getmethods__["readpins"] = _hd44780.hd44780_t_readpins_get
    if _newclass:readpins = _swig_property(_hd44780.hd44780_t_readpins_get, _hd44780.hd44780_t_readpins_set)
    __swig_setmethods__["flags"] = _hd44780.hd44780_t_flags_set
    __swig_getmethods__["flags"] = _hd44780.hd44780_t_flags_get
    if _newclass:flags = _swig_property(_hd44780.hd44780_t_flags_get, _hd44780.hd44780_t_flags_set)
    def __init__(self): 
        this = _hd44780.new_hd44780_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _hd44780.delete_hd44780_t
    __del__ = lambda self : None;
hd44780_t_swigregister = _hd44780.hd44780_t_swigregister
hd44780_t_swigregister(hd44780_t)


def hd44780_init(*args):
  return _hd44780.hd44780_init(*args)
hd44780_init = _hd44780.hd44780_init

def hd44780_print(*args):
  return _hd44780.hd44780_print(*args)
hd44780_print = _hd44780.hd44780_print

def hd44780_set_flag(*args):
  return _hd44780.hd44780_set_flag(*args)
hd44780_set_flag = _hd44780.hd44780_set_flag

def hd44780_get_flag(*args):
  return _hd44780.hd44780_get_flag(*args)
hd44780_get_flag = _hd44780.hd44780_get_flag

def hd44780_get_char(*args):
  return _hd44780.hd44780_get_char(*args)
hd44780_get_char = _hd44780.hd44780_get_char

def hd44780_reset(*args):
  return _hd44780.hd44780_reset(*args)
hd44780_reset = _hd44780.hd44780_reset
# This file is compatible with both classic and new-style classes.


