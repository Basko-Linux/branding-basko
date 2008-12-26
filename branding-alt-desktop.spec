%define theme desktop
%define brand alt
%define status alpha

Name: branding-%brand-%theme
Version: 5.0
Release: alt2
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
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

%package bootsplash
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: design-bootsplash design-bootsplash-%theme
Requires: bootsplash >= 3.3

%description bootsplash
This package contains graphics for boot process
(needs console splash screen enabled)

%package browser-qt
Summary: Design for QT alterator for Desktop version
License: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshiniv <boyarsh@altlinux.org>
Provides: design-alterator-browser-%theme

Requires: alterator-browser-qt
PreReq(post,preun): alternatives >= 0.2

%description browser-qt
Design for QT alterator for Desktop version

%package graphics
Summary: design for ALT
License: Different licenses
Group: Graphics

Provides: design-graphics-%theme
PreReq(post,preun): alternatives >= 0.2

%description graphics
This package contains some graphics for ALT design.


%prep
%setup -q


%build
autoconf
THEME=%theme NAME='Desktop' BRAND_FNAME='ALT Linux' STATUS=%status VERSION=%version ./configure 
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
cat >%buildroot/%_altdir/%name <<__EOF__
/etc/alterator/design-browser-qt	/usr/share/alterator-browser-qt/design/desktop.rcc 50
__EOF__
popd

#graphicks
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
cp -ar graphics/* %buildroot/%_datadir/design/%theme

pushd %buildroot/%_datadir/design/%theme
    pushd backgrounds
	ln -sf ../../../wallpapers more
    popd
popd

install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name <<__EOF__
%_datadir/artworks	%_datadir/design/%theme 10	
%_datadir/design-current	%_datadir/design/%theme	10
__EOF__



#bootloader
%pre bootloader
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:

%post bootloader
%__ln_s -nf %theme/message /boot/splash/message
%__ln_s -nf /boot/splash/%theme /boot/splash/%theme
%__ln_s -nf %_datadir/gfxboot/%theme %_datadir/gfxboot/%theme


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
%config %_altdir/%name
/usr/share/alterator-browser-qt/design/desktop.rcc


%files graphics
%config /etc/alternatives/packages.d/%name
%_datadir/design

%files bootsplash
%_sysconfdir/bootsplash/themes/%theme/


%changelog
* Fri Dec 26 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- colors integration
- graphics package added

* Thu Dec 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- initial sceleton 

