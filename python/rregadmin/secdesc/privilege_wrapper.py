# generated by 'xml2py'
# flags '-c -d -v -k defst -lrregadmin -m rregadmin.util.glib_wrapper -m rregadmin.util.icu_wrapper -m rregadmin.util.path_wrapper -m rregadmin.util.icu_wrapper -m rregadmin.util.path_info_wrapper -m rregadmin.util.ustring_wrapper -m rregadmin.util.offset_wrapper -m rregadmin.util.value_wrapper -m rregadmin.util.ustring_list_wrapper -r ^sec_privilege -r ^sec_privilege_.* -o privilege_wrapper.py privilege_wrapper.xml'
from ctypes import *

_libraries = {}
_libraries['librregadmin.so.1'] = CDLL('librregadmin.so.1')
STRING = c_char_p
from rregadmin.util.glib_wrapper import guint64



# values for enumeration 'sec_privilege'
SEC_PRIV_SECURITY = 1
SEC_PRIV_BACKUP = 2
SEC_PRIV_RESTORE = 3
SEC_PRIV_SYSTEMTIME = 4
SEC_PRIV_SHUTDOWN = 5
SEC_PRIV_REMOTE_SHUTDOWN = 6
SEC_PRIV_TAKE_OWNERSHIP = 7
SEC_PRIV_DEBUG = 8
SEC_PRIV_SYSTEM_ENVIRONMENT = 9
SEC_PRIV_SYSTEM_PROFILE = 10
SEC_PRIV_PROFILE_SINGLE_PROCESS = 11
SEC_PRIV_INCREASE_BASE_PRIORITY = 12
SEC_PRIV_LOAD_DRIVER = 13
SEC_PRIV_CREATE_PAGEFILE = 14
SEC_PRIV_INCREASE_QUOTA = 15
SEC_PRIV_CHANGE_NOTIFY = 16
SEC_PRIV_UNDOCK = 17
SEC_PRIV_MANAGE_VOLUME = 18
SEC_PRIV_IMPERSONATE = 19
SEC_PRIV_CREATE_GLOBAL = 20
SEC_PRIV_ENABLE_DELEGATION = 21
SEC_PRIV_INTERACTIVE_LOGON = 22
SEC_PRIV_NETWORK_LOGON = 23
SEC_PRIV_REMOTE_INTERACTIVE_LOGON = 24
sec_privilege = c_int # enum
# ../../../rregadmin/secdesc/privilege.h 68
sec_privilege_name = _libraries['librregadmin.so.1'].sec_privilege_name
sec_privilege_name.restype = STRING
# sec_privilege_name(privilege)
sec_privilege_name.argtypes = [sec_privilege]
sec_privilege_name.__doc__ = \
"""unknown * sec_privilege_name(sec_privilege privilege)
../../../rregadmin/secdesc/privilege.h:68"""
# ../../../rregadmin/secdesc/privilege.h 74
sec_privilege_display_name = _libraries['librregadmin.so.1'].sec_privilege_display_name
sec_privilege_display_name.restype = STRING
# sec_privilege_display_name(privilege)
sec_privilege_display_name.argtypes = [sec_privilege]
sec_privilege_display_name.__doc__ = \
"""unknown * sec_privilege_display_name(sec_privilege privilege)
../../../rregadmin/secdesc/privilege.h:74"""
# ../../../rregadmin/secdesc/privilege.h 80
sec_privilege_id = _libraries['librregadmin.so.1'].sec_privilege_id
sec_privilege_id.restype = sec_privilege
# sec_privilege_id(name)
sec_privilege_id.argtypes = [STRING]
sec_privilege_id.__doc__ = \
"""sec_privilege sec_privilege_id(unknown * name)
../../../rregadmin/secdesc/privilege.h:80"""
# ../../../rregadmin/secdesc/privilege.h 86
sec_privilege_mask = _libraries['librregadmin.so.1'].sec_privilege_mask
sec_privilege_mask.restype = guint64
# sec_privilege_mask(privilege)
sec_privilege_mask.argtypes = [sec_privilege]
sec_privilege_mask.__doc__ = \
"""guint64 sec_privilege_mask(sec_privilege privilege)
../../../rregadmin/secdesc/privilege.h:86"""
__all__ = ['sec_privilege', 'SEC_PRIV_LOAD_DRIVER',
           'SEC_PRIV_PROFILE_SINGLE_PROCESS',
           'sec_privilege_display_name', 'sec_privilege_name',
           'SEC_PRIV_INCREASE_QUOTA', 'SEC_PRIV_DEBUG',
           'SEC_PRIV_TAKE_OWNERSHIP', 'SEC_PRIV_INTERACTIVE_LOGON',
           'SEC_PRIV_SYSTEMTIME', 'SEC_PRIV_SECURITY',
           'SEC_PRIV_CREATE_PAGEFILE', 'SEC_PRIV_CREATE_GLOBAL',
           'SEC_PRIV_NETWORK_LOGON', 'SEC_PRIV_IMPERSONATE',
           'SEC_PRIV_UNDOCK', 'SEC_PRIV_BACKUP', 'SEC_PRIV_RESTORE',
           'SEC_PRIV_INCREASE_BASE_PRIORITY', 'sec_privilege_id',
           'SEC_PRIV_MANAGE_VOLUME',
           'SEC_PRIV_REMOTE_INTERACTIVE_LOGON',
           'SEC_PRIV_ENABLE_DELEGATION', 'SEC_PRIV_CHANGE_NOTIFY',
           'SEC_PRIV_REMOTE_SHUTDOWN', 'sec_privilege_mask',
           'SEC_PRIV_SYSTEM_ENVIRONMENT', 'SEC_PRIV_SYSTEM_PROFILE',
           'SEC_PRIV_SHUTDOWN']
