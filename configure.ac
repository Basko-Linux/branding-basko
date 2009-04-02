AC_INIT( [branding], [0.1], [http://bugzilla.altlinux.ru] )


PROGRESS_COLOR=`./fetch_color selectBackground`
TITLE_COLOR=`./fetch_color handle`
INACTIVE_COLOR=`./fetch_color inactiveTitleBtnBg`
LIGHT_COLOR_DEC="223,223,224"
MIDDLE_COLOR_DEC="200,201,203"
DARK_COLOR_DEC="144,145,149"


AC_SUBST(THEME)
AC_SUBST(NAME)
AC_SUBST(BRAND_FNAME)
AC_SUBST(STATUS)
AC_SUBST(VERSION)
AC_SUBST(PROGRESS_COLOR)
AC_SUBST(LIGHT_COLOR_DEC)
AC_SUBST(MIDDLE_COLOR_DEC)
AC_SUBST(DARK_COLOR_DEC)
AC_SUBST(TITLE_COLOR)
AC_SUBST(INACTIVE_COLOR)

AC_CONFIG_FILES([
		 Makefile
		 bootloader/config
		 bootsplash/config/bootsplash-640x480.cfg
		 bootsplash/config/bootsplash-800x600.cfg
		 alterator/design/design.ini
		 alterator/design/design.qss
		 bootloader/gfxboot.cfg
		 kde3-settings/apps/kdisplay/color-schemes/scheme.kcsrc
		 notes/release-notes.ru.html
		 notes/release-notes.all.html
		 notes/license.ru.html
		 notes/license.all.html
		 indexhtml.desktop
		 indexhtml/index-ru.html
		 indexhtml/index-uk.html
		 indexhtml/index-en.html
])
AC_OUTPUT
