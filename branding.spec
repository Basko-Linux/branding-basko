%define theme office-server
%define Theme OfficeServer
%define codename none 
%define brand altlinux
%define Brand ALT Linux
%define status alpha 
%define variants altlinux-office-desktop altlinux-desktop altlinux-lite


Name: branding-%brand-%theme
Version: 5.0.0
Release: alt3
BuildArch: noarch

BuildRequires: cpio gfxboot >= 4 fonts-ttf-dejavu
BuildRequires: design-bootloader-source >= 5.0-alt2

BuildRequires(pre): libqt4-core 
BuildRequires: libalternatives-devel
BuildRequires: libqt4-devel

BuildRequires: ImageMagick fontconfig

Packager: Anton V. Boyarshinov <boyarsh at altlinux dot org>

Source: %name-%version.tar

Group: Graphics
Summary: System/Base
License: GPL

%description
Distro-specific packages with design and texts

%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for lilo and syslinux
License: GPL

PreReq: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootloader ";done )

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

%package bootsplash
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: design-bootsplash design-bootsplash-%theme  branding-alt-%theme-bootsplash
Requires: bootsplash >= 3.3
Obsoletes:  branding-alt-%theme-bootsplash

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootsplash ";done )
%description bootsplash
This package contains graphics for boot process
(needs console splash screen enabled)

%package alterator
Summary: Design for alterator for %Brand %Theme 
License: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshiniv <boyarsh@altlinux.org>
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt  branding-altlinux-%theme-browser-qt

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-browser-qt ";done )
Conflicts: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server 
PreReq(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %Brand %Theme 


%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business
%package release

Summary: %distribution %Theme release file
Copyright: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list  branding-alt-%theme-release
Conflicts: %conflicts_list
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-release ";done )

%description release
%distribution %version %Theme release file.

%package notes
Provides: alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary: Distribution license and release notes
License: Distributable
Group: Documentation
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-notes ";done )

%description notes
Distribution license and release notes


%package slideshow

Summary: Slideshow for %Brand %version %Theme installer
License: Distributable
Group: System/Configuration/Other 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-slideshow ";done )

%description slideshow
Slideshow for %Brand %version %Theme installer

%package indexhtml

Summary: %name -- ALT Linux html welcome page
License: distributable
Group: System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop

Conflicts: indexhtml-sisyphus
Conflicts: indexhtml-school_junior
Conflicts: indexhtml-school_lite
Conflicts: indexhtml-school_master
Conflicts: indexhtml-school_terminal
Conflicts: indexhtml-small_business
Conflicts: indexhtml-school-server

Requires: xdg-utils 
Requires(post): indexhtml-common

%description indexhtml
ALT Linux index.html welcome page.

%prep
%setup -q


%build
autoconf
THEME=%theme NAME='%Theme' BRAND_FNAME='ALT Linux' STATUS=%status VERSION=%version ./configure 
make

#bootloader
    pushd design-bootloader-source/
    DEFAULT_LANG='--lang-to-subst--' PATH=$PATH:/usr/sbin %make
    popd

#altarator
    pushd alterator
    %make_build
    popd

%install
#bootloader
    pushd design-bootloader-source
    install -d -m 755 %buildroot/boot/splash/%theme
    install -d -m 755 %buildroot/%_datadir/gfxboot/%theme
    install -m 644 message %buildroot/boot/splash/%theme
    install -m 644 bootlogo %buildroot%_datadir/gfxboot/%theme
    popd

#bootsplash
## create directory structure
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/bootsplash/themes/%theme
cp -a bootsplash/* $RPM_BUILD_ROOT%_sysconfdir/bootsplash/themes/%theme

pushd $RPM_BUILD_ROOT%_sysconfdir/bootsplash/themes/%theme/config
#for i in 1 2 3 4 5 11; do \
for i in 1; do \
 for f in bootsplash-*.cfg; do \
    res=`echo "$f"| sed 's|.*\-\(.*\)\.cfg|\1|'`
    ln -s $f vt${i}-${res}.cfg
 done
done
popd

#alterator
pushd alterator
mkdir -p %buildroot/usr/share/alterator-browser-qt/design

install theme.rcc %buildroot/usr/share/alterator-browser-qt/design/%theme.rcc


mkdir -p %buildroot/usr/share/alterator/design/
cp -a images %buildroot/usr/share/alterator/design/
popd

mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name-browser-qt <<__EOF__
/etc/alterator/design-browser-qt	/usr/share/alterator-browser-qt/design/%theme.rcc 50
__EOF__

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
echo "%distribution %version %Theme %status (%codename)" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done

#notes
pushd notes
%makeinstall
popd


#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install slideshow/*  %buildroot/usr/share/install2/slideshow/

#indexhtml
%define _altdocsdir %_defaultdocdir/alt-docs
%define _indexhtmldir %_altdocsdir/indexhtml
pushd indexhtml
mkdir -p %buildroot{%_indexhtmldir/,%_desktopdir/}
cp -r * %buildroot%_indexhtmldir/
rm -f %buildroot%_indexhtmldir/*.in
touch %buildroot%_indexhtmldir/index.html
popd
install -m644 indexhtml.desktop %buildroot%_desktopdir/

#bootloader
%pre bootloader
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:

%post bootloader
%__ln_s -nf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message



%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
%_datadir/gfxboot/%theme
/boot/splash/%theme

#bootsplash
%post bootsplash
%__ln_s -nf %theme %_sysconfdir/bootsplash/themes/current

%preun bootsplash
[ $1 = 0 ] || exit 0
[ "`readlink %_sysconfdir/bootsplash/themes/current`" != %theme ] ||
    %__rm -f %_sysconfdir/bootsplash/themes/current


%files alterator
%config %_altdir/%name-browser-qt
/usr/share/alterator-browser-qt/design/%theme.rcc
/usr/share/alterator/design/images


%files bootsplash
%_sysconfdir/bootsplash/themes/%theme/


%files release
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*


%files slideshow
/usr/share/install2/slideshow

%files indexhtml
%ghost %_indexhtmldir/index.html
%_indexhtmldir/*
%_desktopdir/*

%changelog
* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt3
- conflicts for -alterator subpackages added
- design for web alterator changed

* Mon Mar 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt2
- -browser-qt subpackage remaned to -alterator as it really is

* Fri Mar 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- addes \%status to altlinux-release
- images for verbose bootsplash mode from one source

* Wed Mar 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt10
- added versioned provides for indexhtml 
- indexhtml subpackage added 
- other images for browser-qt added
- conflicts bitween different brandings added
- steps icons added 
- sample slideshow added

* Fri Feb 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt9
- merge with desktop branch 


* Tue Feb 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt8
- merge desktop branch
- added adderesses into notes

* Tue Feb 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt6
- merge with desktop branch
- unneded subpackages deleted

* Fri Jan 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt5
- added 'notes' subpackage 

* Thu Jan 15 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt4
- fixed problem with owerwritten alternative 

* Wed Jan 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- release subpackage added 

* Fri Dec 26 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- colors integration
- graphics package added

* Thu Dec 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- initial sceleton 

