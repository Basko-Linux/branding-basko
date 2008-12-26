AC_INIT( [branding], [0.1], [http://bugzilla.altlinux.ru] )

AC_ARG_WITH(theme,
	    AC_HELP_STRING([--with-theme=theme],
			   [base theme, e.g '--with-theme=lite' ]),
			   [
			    if test -n "$with_theme"  ; then
				    THEME="$with_theme"
			    fi
			       ],
				    [
				     THEME="theme"
				     ]
				    )
AC_ARG_WITH(name,
	    AC_HELP_STRING([--with-name=name],
			   [Human readable name, e.g '--with-name="Small Business"' ]),
			   [
			    if test -n "$with_name"  ; then
				    NAME="$with_name"
			    fi
			       ],
				    [
				     NAME="name"
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
AC_ARG_WITH(brand,
	    AC_HELP_STRING([--with-status=brand],
			   [brand, e.g '--with-brand="ALT Linux"']),
			   [
			    if test -n "$with_brand"  ; then
				    BRAND_FNAME="$with_brand"
			    fi
			       ],
				    [
				     BRAND_FNAME=""
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


PROGRESS_COLOR=`./fetch_color selectBackground`
TITLE_COLOR=`./fetch_color handle`
INACTIVE_COLOR=`./fetch_color inactiveTitleBtnBg`


AC_SUBST(THEMEMC)
AC_SUBST(THEMELC)
AC_SUBST(THEME)
AC_SUBST(BRAND_FNAME)
AC_SUBST(STATUS)
AC_SUBST(VERSION)
AC_SUBST(PROGRESS_COLOR)
AC_SUBST(TITLE_COLOR)
AC_SUBST(INACTIVE_COLOR)

AC_CONFIG_FILES([
		 Makefile
		 bootloader/config
		 bootsplash/config/bootsplash-640x480.cfg
		 bootsplash/config/bootsplash-800x600.cfg
		 browser-qt/design/design.ini
		 bootloader/gfxboot.cfg
		 kde3-settings/apps/kdisplay/color-schemes/scheme.kcsrc
])
AC_OUTPUT
