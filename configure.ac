AC_INIT( [branding], [0.1], [http://bugzilla.altlinux.ru] )

AC_ARG_WITH(aptconf,
AC_ARG_WITH(distro,
	    AC_HELP_STRING([--with-distro=distro],
			   [base distro, e.g '--with-distro=lite' ]),
			   [
			    if test -n "$with_distro"  ; then
				    theme="$with_distro"
				    Theme=`echo "$with_distro" | sed 's/^./\u&/'`
				    THEME=`echo "$with_distro" | sed 's/./\u&/'`
			    fi
			       ],
				    [
				     theme="theme"
				     Theme="Theme"
				     THEME="THEME"
				     ]
				    )
			       ],
				    [
				     DESIGN=""
				     ])

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


AC_SUBST(theme)
AC_SUBST(Theme)
AC_SUBST(THEME)
AC_SUBST(STATUS)


AC_CONFIG_FILES([
		 Makefile
		 bootloader/config
		 bootsplash/config/bootsplash-640x480.cfg
		 bootsplash/config/bootsplash-800x600.cfg
])
AC_OUTPUT
