# generated by 'xml2py'
# flags '-c -d -v -k defst -lrregadmin -m rregadmin.util.glib_wrapper -m rregadmin.util.icu_wrapper -m rregadmin.util.path_wrapper -m rregadmin.util.icu_wrapper -m rregadmin.util.path_info_wrapper -m rregadmin.util.ustring_wrapper -m rregadmin.util.offset_wrapper -m rregadmin.util.value_wrapper -m rregadmin.util.ustring_list_wrapper -m rregadmin.hive.types_wrapper -r ^security_descriptor_cell_.* -o security_descriptor_cell_wrapper.py security_descriptor_cell_wrapper.xml'
from ctypes import *

from rregadmin.hive.types_wrapper import SecurityDescriptorCell
from rregadmin.hive.types_wrapper import Hive
from rregadmin.util.offset_wrapper import offset
_libraries = {}
_libraries['librregadmin.so.1'] = CDLL('librregadmin.so.1')
from rregadmin.util.ustring_list_wrapper import gboolean
from rregadmin.hive.types_wrapper import Cell
from rregadmin.util.ustring_list_wrapper import ustring


# ../../../rregadmin/secdesc/security_descriptor.h 62
class SecurityDescriptor_(Structure):
    pass
SecurityDescriptor = SecurityDescriptor_
# ../../../rregadmin/hive/security_descriptor_cell.h 50
security_descriptor_cell_alloc = _libraries['librregadmin.so.1'].security_descriptor_cell_alloc
security_descriptor_cell_alloc.restype = POINTER(SecurityDescriptorCell)
# security_descriptor_cell_alloc(in_hive, p, in_secdesc)
security_descriptor_cell_alloc.argtypes = [POINTER(Hive), offset, POINTER(SecurityDescriptor)]
security_descriptor_cell_alloc.__doc__ = \
"""SecurityDescriptorCell * security_descriptor_cell_alloc(Hive * in_hive, offset p, unknown * in_secdesc)
../../../rregadmin/hive/security_descriptor_cell.h:50"""
# ../../../rregadmin/hive/security_descriptor_cell.h 56
security_descriptor_cell_unalloc = _libraries['librregadmin.so.1'].security_descriptor_cell_unalloc
security_descriptor_cell_unalloc.restype = gboolean
# security_descriptor_cell_unalloc(in_sdc)
security_descriptor_cell_unalloc.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_unalloc.__doc__ = \
"""gboolean security_descriptor_cell_unalloc(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:56"""
# ../../../rregadmin/hive/security_descriptor_cell.h 62
security_descriptor_cell_from_cell = _libraries['librregadmin.so.1'].security_descriptor_cell_from_cell
security_descriptor_cell_from_cell.restype = POINTER(SecurityDescriptorCell)
# security_descriptor_cell_from_cell(p)
security_descriptor_cell_from_cell.argtypes = [POINTER(Cell)]
security_descriptor_cell_from_cell.__doc__ = \
"""SecurityDescriptorCell * security_descriptor_cell_from_cell(Cell * p)
../../../rregadmin/hive/security_descriptor_cell.h:62"""
# ../../../rregadmin/hive/security_descriptor_cell.h 69
security_descriptor_cell_to_cell = _libraries['librregadmin.so.1'].security_descriptor_cell_to_cell
security_descriptor_cell_to_cell.restype = POINTER(Cell)
# security_descriptor_cell_to_cell(in_sdc)
security_descriptor_cell_to_cell.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_to_cell.__doc__ = \
"""Cell * security_descriptor_cell_to_cell(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:69"""
# ../../../rregadmin/hive/security_descriptor_cell.h 75
security_descriptor_cell_get_use_count = _libraries['librregadmin.so.1'].security_descriptor_cell_get_use_count
security_descriptor_cell_get_use_count.restype = c_int
# security_descriptor_cell_get_use_count(in_sdc)
security_descriptor_cell_get_use_count.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_get_use_count.__doc__ = \
"""int security_descriptor_cell_get_use_count(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:75"""
# ../../../rregadmin/hive/security_descriptor_cell.h 82
security_descriptor_cell_increment_use_count = _libraries['librregadmin.so.1'].security_descriptor_cell_increment_use_count
security_descriptor_cell_increment_use_count.restype = gboolean
# security_descriptor_cell_increment_use_count(in_sdc)
security_descriptor_cell_increment_use_count.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_increment_use_count.__doc__ = \
"""gboolean security_descriptor_cell_increment_use_count(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:82"""
# ../../../rregadmin/hive/security_descriptor_cell.h 89
security_descriptor_cell_decrement_use_count = _libraries['librregadmin.so.1'].security_descriptor_cell_decrement_use_count
security_descriptor_cell_decrement_use_count.restype = gboolean
# security_descriptor_cell_decrement_use_count(in_sdc)
security_descriptor_cell_decrement_use_count.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_decrement_use_count.__doc__ = \
"""gboolean security_descriptor_cell_decrement_use_count(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:89"""
# ../../../rregadmin/hive/security_descriptor_cell.h 96
security_descriptor_cell_get_prev = _libraries['librregadmin.so.1'].security_descriptor_cell_get_prev
security_descriptor_cell_get_prev.restype = POINTER(SecurityDescriptorCell)
# security_descriptor_cell_get_prev(in_sdc)
security_descriptor_cell_get_prev.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_get_prev.__doc__ = \
"""SecurityDescriptorCell * security_descriptor_cell_get_prev(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:96"""
# ../../../rregadmin/hive/security_descriptor_cell.h 103
security_descriptor_cell_get_next = _libraries['librregadmin.so.1'].security_descriptor_cell_get_next
security_descriptor_cell_get_next.restype = POINTER(SecurityDescriptorCell)
# security_descriptor_cell_get_next(in_sdc)
security_descriptor_cell_get_next.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_get_next.__doc__ = \
"""SecurityDescriptorCell * security_descriptor_cell_get_next(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:103"""
# ../../../rregadmin/hive/security_descriptor_cell.h 110
security_descriptor_cell_get_secdesc = _libraries['librregadmin.so.1'].security_descriptor_cell_get_secdesc
security_descriptor_cell_get_secdesc.restype = POINTER(SecurityDescriptor)
# security_descriptor_cell_get_secdesc(in_sdc)
security_descriptor_cell_get_secdesc.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_get_secdesc.__doc__ = \
"""unknown * security_descriptor_cell_get_secdesc(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:110"""
# ../../../rregadmin/hive/security_descriptor_cell.h 119
security_descriptor_cell_debug_print = _libraries['librregadmin.so.1'].security_descriptor_cell_debug_print
security_descriptor_cell_debug_print.restype = None
# security_descriptor_cell_debug_print(in_sdc)
security_descriptor_cell_debug_print.argtypes = [POINTER(SecurityDescriptorCell)]
security_descriptor_cell_debug_print.__doc__ = \
"""void security_descriptor_cell_debug_print(SecurityDescriptorCell * in_sdc)
../../../rregadmin/hive/security_descriptor_cell.h:119"""
# ../../../rregadmin/hive/security_descriptor_cell.h 122
security_descriptor_cell_get_xml_output = _libraries['librregadmin.so.1'].security_descriptor_cell_get_xml_output
security_descriptor_cell_get_xml_output.restype = gboolean
# security_descriptor_cell_get_xml_output(in_sdc, in_output)
security_descriptor_cell_get_xml_output.argtypes = [POINTER(SecurityDescriptorCell), POINTER(ustring)]
security_descriptor_cell_get_xml_output.__doc__ = \
"""gboolean security_descriptor_cell_get_xml_output(SecurityDescriptorCell * in_sdc, ustring * in_output)
../../../rregadmin/hive/security_descriptor_cell.h:122"""
SecurityDescriptor_._fields_ = [
    # ../../../rregadmin/secdesc/security_descriptor.h 62
]
__all__ = ['security_descriptor_cell_get_next',
           'security_descriptor_cell_increment_use_count',
           'security_descriptor_cell_debug_print',
           'security_descriptor_cell_get_use_count',
           'SecurityDescriptor_', 'security_descriptor_cell_get_prev',
           'SecurityDescriptor',
           'security_descriptor_cell_get_secdesc',
           'security_descriptor_cell_get_xml_output',
           'security_descriptor_cell_unalloc',
           'security_descriptor_cell_decrement_use_count',
           'security_descriptor_cell_from_cell',
           'security_descriptor_cell_to_cell',
           'security_descriptor_cell_alloc']
