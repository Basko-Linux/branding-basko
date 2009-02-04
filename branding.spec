%define theme desktop 
%define Theme Desktop
%define codename Inula Helenium 
%define brand altlinux
%define status alpha

Name: branding-%brand-%theme
Version: 5.0
Release: alt7
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

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

%package bootsplash
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: design-bootsplash design-bootsplash-%theme  branding-alt-%theme-bootsplash
Requires: bootsplash >= 3.3
Obsoletes:  branding-alt-%theme-bootsplash

%description bootsplash
This package contains graphics for boot process
(needs console splash screen enabled)

%package browser-qt
Summary: Design for QT alterator for Desktop version
License: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshiniv <boyarsh@altlinux.org>
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt
Obsoletes:  branding-alt-%theme-browser-qt

Requires: alterator-browser-qt
PreReq(post,preun): alternatives >= 0.2

%description browser-qt
Design for QT alterator for Desktop version

%package graphics
Summary: design for ALT
License: Different licenses
Group: Graphics

Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes:  branding-alt-%theme-graphics
PreReq(post,preun): alternatives >= 0.2

%description graphics
This package contains some graphics for ALT design.


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

%description release
%distribution %version %Theme release file.

%package notes
Provides: alt-license-desktop = %version
Obsoletes: alt-license-desktop

Summary: Distribution license and release notes
License: Distributable
Group: Documentation
Provides: alt-notes-%theme
Obsoletes: alt-notes-%theme
Conflicts: alt-notes-children alt-notes-desktop alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal 

%description notes
Distribution license and release notes

%prep
%setup -q


%build
autoconf
THEME=%theme NAME='%Theme' BRAND_FNAME='ALT Linux' STATUS=%status VERSION=%version ./configure 
make

#bootloader
    pushd design-bootloader-source/
    PATH=$PATH:/usr/sbin %make
    popd

#browser-qt
    pushd browser-qt
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

#browser-qt
pushd browser-qt
mkdir -p %buildroot/usr/share/alterator-browser-qt/design

install theme.rcc %buildroot/usr/share/alterator-browser-qt/design/%theme.rcc

mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name-browser-qt <<__EOF__
/etc/alterator/design-browser-qt	/usr/share/alterator-browser-qt/design/%theme.rcc 50
__EOF__
popd

#graphics
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
cp -ar graphics/* %buildroot/%_datadir/design/%theme

pushd %buildroot/%_datadir/design/%theme
    pushd backgrounds
	ln -sf ../../../wallpapers more
    popd
popd

install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/artworks	%_datadir/design/%theme 10	
%_datadir/design-current	%_datadir/design/%theme	10
__EOF__

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
echo "%distribution %version %Theme (%codename)" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done

pushd notes
%makeinstall
popd


#bootloader
%pre bootloader
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:

%post bootloader
%__ln_s -nf %theme/message /boot/splash/message


%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

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


%files browser-qt
%config %_altdir/%name-browser-qt
/usr/share/alterator-browser-qt/design/%theme.rcc


%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design

%files bootsplash
%_sysconfdir/bootsplash/themes/%theme/


%files release
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%changelog
* Wed Feb 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt7
- added conflicts for notes 

* Mon Jan 26 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt6
- xdm background fixed 

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

