AC_INIT( [branding], [0.1], [http://bugzilla.altlinux.ru] )


PROGRESS_COLOR=`./fetch_color selectBackground` #MIDDLE_COLOR_DEC
TITLE_COLOR=`./fetch_color handle`
INACTIVE_COLOR=`./fetch_color inactiveTitleBtnBg`
LIGHT_COLOR_HEX=DFDFE0
MIDDLE_COLOR_HEX=C8C9CB
DARK_COLOR_HEX=909195
LIGHT_LABELS_HEX=FFFFFF
DARK_LABELS_HEX=000000
MIDDLE_LABELS_HEX=4d4d4f
LIGHT_COLOR_DEC=`./color_dec ${LIGHT_COLOR_HEX}`
MIDDLE_COLOR_DEC=`./color_dec ${MIDDLE_COLOR_HEX}`
DARK_COLOR_DEC=`./color_dec ${DARK_COLOR_HEX}`

AC_SUBST(THEME)
AC_SUBST(NAME)
AC_SUBST(BRAND)
AC_SUBST(BRAND_FNAME)
AC_SUBST(STATUS)
AC_SUBST(STATUS_EN)
AC_SUBST(VERSION)
AC_SUBST(PROGRESS_COLOR)
AC_SUBST(LIGHT_COLOR_HEX)
AC_SUBST(MIDDLE_COLOR_HEX)
AC_SUBST(DARK_COLOR_HEX)
AC_SUBST(LIGHT_LABELS_HEX)
AC_SUBST(DARK_LABELS_HEX)
AC_SUBST(MIDDLE_LABELS_HEX)
AC_SUBST(LIGHT_COLOR_DEC)
AC_SUBST(MIDDLE_COLOR_DEC)
AC_SUBST(DARK_COLOR_DEC)
AC_SUBST(TITLE_COLOR)
AC_SUBST(INACTIVE_COLOR)

AC_CONFIG_FILES([
		 Makefile
		 components/bootloader/config
		 components/bootsplash/config/bootsplash-640x480.cfg
		 components/bootsplash/config/bootsplash-800x600.cfg
		 components/bootsplash/config/bootsplash-1024x768.cfg
		 components/browser-qt/design/design.ini
		 components/browser-qt/design/design.qss
		 components/bootloader/gfxboot.cfg
		 kde3-settings/apps/kdisplay/color-schemes/scheme.kcsrc
		 notes/release-notes.ru.html
		 notes/release-notes.all.html
		 notes/license.ru.html
		 notes/license.all.html
		 notes/index-ru.html
		 notes/index-uk.html
		 notes/index-en.html
		 components/indexhtml/indexhtml.desktop
		 components/indexhtml/index.css
		 gnome-settings/gtkrc
		 gnome-settings/index.theme
		 gnome-settings/metacity-theme-1.xml
		 components/ahttpd/styles/alterator.css
		 kde3-styles-splash/Theme.rc
		 xfce-settings/xinitrc
])
AC_OUTPUT
