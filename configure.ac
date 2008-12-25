AC_INIT( [branding], [0.1], [http://bugzilla.altlinux.ru] )

AC_ARG_WITH(distro,
	    AC_HELP_STRING([--with-distro=distro],
			   [base distro, e.g '--with-distro=lite' ]),
			   [
			    if test -n "$with_distro"  ; then
				    THEME="$with_distro"
				    THEMEMC=`echo "$with_distro" | sed 's/^./\u&/'`
				    THEMEUC=`echo "$with_distro" | sed 's/./\u&/'`
			    fi
			       ],
				    [
				     THEME="theme"
				     THEMEMC="Theme"
				     THEMEUC="THEME"
				     ]
				    )

AC_ARG_WITH(status,
	    AC_HELP_STRING([--with-status=beta],
			   [status, e.g '--with-status=beta']),
			   [
			    if test -n "$with_status"  ; then
				    STATUS="$with_status"
			    fi
			       ],
				    [
				     STATUS=""
				     ])

AC_ARG_WITH(version,
	    AC_HELP_STRING([--with-version=5.0],
			   [version, e.g '--with-version=5.0']),
			   [
			    if test -n "$with_version"  ; then
				    VERSION="$with_version"
			    fi
			       ],
				    [
				     VERSION=""
				     ])


AC_SUBST(THEMEMC)
AC_SUBST(THEMELC)
AC_SUBST(THEME)
AC_SUBST(STATUS)
AC_SUBST(VERSION)


AC_CONFIG_FILES([
		 Makefile
		 bootloader/config
		 bootsplash/config/bootsplash-640x480.cfg
		 bootsplash/config/bootsplash-800x600.cfg
])
AC_OUTPUT
