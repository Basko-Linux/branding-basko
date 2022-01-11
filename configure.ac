AC_INIT( [branding], [0.1], [http://bugzilla.altlinux.ru] )


PROGRESS_COLOR=0093d7
TITLE_COLOR=5C96CC
INACTIVE_COLOR=DFDFE0
LIGHT_COLOR_HEX=F5F2E7
MIDDLE_COLOR_HEX=E9E6DC
DARK_COLOR_HEX=848481
LIGHT_LABELS_HEX=FFFFFF
DARK_LABELS_HEX=000000
MIDDLE_LABELS_HEX=798491
LIGHT_COLOR_DEC=`./color_dec ${LIGHT_COLOR_HEX}`
MIDDLE_COLOR_DEC=`./color_dec ${MIDDLE_COLOR_HEX}`
DARK_COLOR_DEC=`./color_dec ${DARK_COLOR_HEX}`

DOCDIR=documentation

AC_SUBST(THEME)
AC_SUBST(NAME)
AC_SUBST(BRAND)
AC_SUBST(BRAND_FNAME)
AC_SUBST(STATUS)
AC_SUBST(STATUS_EN)
AC_SUBST(VERSION)
AC_SUBST(PRODUCT_NAME)
AC_SUBST(CODENAME)
AC_SUBST(DOCDIR)
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
AC_SUBST(URL)

AC_CONFIG_FILES([
		 Makefile
		 components/bootloader/config
		 components/bootsplash/theme.plymouth
		 components/bootsplash/theme.script
		 components/browser-qt/design/design.ini
		 components/browser-qt/design/design.qss
		 components/bootloader/gfxboot.cfg
		 notes/release-notes.ru.html
		 notes/release-notes.all.html
		 notes/license.ru.html
		 notes/license.all.html
		 notes/index-ru.html
		 notes/index-en.html
		 components/indexhtml/indexhtml.desktop
		 components/indexhtml/index.css
		 components/ahttpd/styles/alterator.css
		 components/systemd/os-release
])
AC_OUTPUT
