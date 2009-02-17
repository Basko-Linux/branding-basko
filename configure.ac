AC_INIT( [branding], [0.1], [http://bugzilla.altlinux.ru] )


PROGRESS_COLOR=`./fetch_color selectBackground`
TITLE_COLOR=`./fetch_color handle`
INACTIVE_COLOR=`./fetch_color inactiveTitleBtnBg`


AC_SUBST(THEME)
AC_SUBST(NAME)
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
		 notes/release-notes.ru.html
		 notes/release-notes.all.html
		 notes/license.ru.html
		 notes/license.all.html
])
AC_OUTPUT
