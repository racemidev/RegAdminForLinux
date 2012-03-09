dnl @synopsis AX_WITH_PYTHON([minimum-version], [value-if-not-found], [path])
dnl
dnl Locates an installed Python binary, placing the result in the
dnl precious variable $PYTHON. Accepts a present $PYTHON, then
dnl --with-python, and failing that searches for python in the given
dnl path (which defaults to the system path). If python is found,
dnl $PYTHON is set to the full path of the binary; if it is not found,
dnl $PYTHON is set to VALUE-IF-NOT-FOUND, which defaults to 'python'.
dnl
dnl Example:
dnl
dnl   AX_WITH_PYTHON(2.2, missing)
dnl
dnl @category InstalledPackages
dnl @author Dustin Mitchell <dustin@cs.uchicago.edu>
dnl @version 2005-01-22
dnl @license GPLWithACException

AC_DEFUN([AX_WITH_PYTHON],
[
  AC_ARG_VAR([PYTHON])

  dnl unless PYTHON was supplied to us (as a precious variable)
  if test -z "$PYTHON"
  then
    AC_MSG_CHECKING(for --with-python)
    AC_ARG_WITH(python,
                AC_HELP_STRING([--with-python=PYTHON],
                               [absolute path name of Python executable]),
                [ if test "$withval" != "yes"
                  then
                    PYTHON="$withval"
                    AC_MSG_RESULT($withval)
                  else
                    AC_MSG_RESULT(no)
                  fi
                ],
                [ AC_MSG_RESULT(no)
                ])
  fi

  dnl if it's still not found, check the paths, or use the fallback
  if test -z "$PYTHON"
  then
    AC_PATH_PROGS([PYTHON],
                  m4_ifval([$2],[$2],[python]),
                  m4_ifval([$3],[$3],[python]), $4)
  fi

  dnl check version if required
  m4_ifvaln([$1], [
    AC_MSG_CHECKING($PYTHON version >= $1)
    if test `$PYTHON -c ["import sys; print sys.version[:3] >= \"$1\" and \"OK\" or \"OLD\""]` = "OK"
    then
      AC_MSG_RESULT(ok)
    else
      AC_MSG_RESULT(no)
      PYTHON="$2"
    fi
    ])

])
