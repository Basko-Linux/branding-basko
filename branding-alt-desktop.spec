%define theme desktop
%define brand alt

Name: branding-%brand-%theme
Version: 5.0
Release: alt1
BuildArch: noarch
PreReq: coreutils
BuildRequires: cpio gfxboot >= 4 fonts-ttf-dejavu
BuildRequires: design-bootloader-source >= 5.0-alt2
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

Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.


%prep
%setup -q
# bootloader
    cp -a  /usr/src/design-bootloader-source ./
    cp -a bootloader/config  bootloader/data-boot/ bootloader/data-install/ design-bootloader-source/

%build
#bootloader
    pushd design-bootloader-source/
    PATH=$PATH:/usr/sbin %make
    popd

%install
#bootloader
    pushd design-bootloader-source
    install -d -m 755 %buildroot/boot/splash/%theme
    install -d -m 755 %buildroot/%_datadir/gfxboot/%theme
    install -m 644 message %buildroot/boot/splash/%theme
    install -m 644 bootlogo %buildroot%_datadir/gfxboot/%theme
    popd

%post bootloader
#bootloader
%__ln_s -nf %theme/message /boot/splash/message
%__ln_s -nf /boot/splash/%theme /boot/splash/%theme
%__ln_s -nf %_datadir/gfxboot/%theme %_datadir/gfxboot/%theme


%preun bootloader
#bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message


%files bootloader
%_datadir/gfxboot/%theme
/boot/splash/%theme


%changelog
* Thu Dec 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- initial sceleton 

