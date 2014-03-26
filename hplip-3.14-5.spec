# Remsnet Spec file for package snort ( for snort 2.9 build )
#
# Copyright (c) 1995-2008 Remsnet Netzwerk Service OhG , D-73630 Remshalden
# Copyright (c) 2008-2014 Remsnet Consullting & Internet Services LTD , D-40476 Duesseldorf


# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/remsnet/OpenSuSE-hplip
#

#
%define        lp_gid 9
%define cups_ver %(cups-config --api-version)
Name:          hplip
Version:       3.14.3
Release:       1.5_rcis
Summary:       A printer driver for HP inkjet devices
Group:         System/Spooling
Vendor:        Hewlet Packard -  printer drivers
Distribution:  OpenSuse
Packager:      Horst venzke <horst.venzke@remsnet.de>
URL:           http://hplipopensource.com/hplip-web/index.html
Source:        http://downloads.sourceforge.net/sourceforge/hplip/hplip-%{version}.tar.gz
License:       BSD, LGPL

BuildRequires: coreutils automake autoconf flex bison gettext libtool pkg-config
BuildRequires: cups-devel
BuildRequires: glibc-devel
BuildRequires: dbus-1-devel libedbus1 e_dbus-devel
BuildRequires: libgcc_s1
BuildRequires: libjpeg-devel
BuildRequires: libopenssl-devel libgnutls-openssl-devel
BuildRequires: sane-backends-devel sane-backends-autoconfig
BuildRequires: libstdc++-devel
BuildRequires: libusb-1_0-devel usbip usbprog-devel usbredir-devel
BuildRequires: python-cupshelpers python-cups
BuildRequires: python-devel
BuildRequires: perl-Devel-FindPerl perl
BuildRequires: gcc >= 4.4.4
BuildRequires: gcc-fortran >= 4.4.4
BuildRequires: gcc-locale >= 4.4.4
BuildRequires: gcc-obj-c++ >= 4.4.4
BuildRequires: gcc-ranlib >= 4.4.4
BuildRequires: gcc-ar >= 4.4.4
BuildRequires: gcc-nm >= 4.4.4
BuildRequires: libieee1284-devel
BuildRequires: libgphoto2-devel libexif-devel libjpeg62-devel
##BuildRequires: libssp-devel
Obsoletes:     hpijs
Requires:      cups
Requires:      sane
Requires:      python-cups python-cupshelpers

BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Requires(pre): libsane-backends >= 1.0.16
Provides:      hpijs = %{version}

%description
A printer driver for HP inkjet devices.
Provides printing support for more than 300 printer models, including, DeskJet, OfficeJet, Photosmart, Business Inkjet and some LaserJet.

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
A printer driver for HP inkjet devices.
This package contains static libraries and header files need for development.

%prep
%setup -q

#sed -i "s|SYSFS{|ATTRS{|g" data/rules/55-hpmud.rules data/rules/56-hpmud_support.rules
#sed -i "s|sysfs{|ATTR{|g" data/rules/55-hpmud.rules data/rules/56-hpmud_support.rules

sed -i "s|chgrp \"lp\"|/bin/true \"lp\"|" Makefile.in
sed -i "s|chmod 774|/bin/true 774|" Makefile.in

%build
%configure \
   --prefix=/usr \
   --enable-scan-build \
   --enable-network-build \
   --enable-foomatic-ppd-install \
   --enable-policykit \
   --disable-gui-build \
   --enable-new-hpcups \
   --with-cupsbackenddir=/usr/lib/cups/backend \
   --with-cupsfilterdir=/usr/lib/cups/filter \
   --enable-foomatic-drv-install \
   --enable-foomatic-ppd-install \
   --enable-foomatic-rip-hplip-install \
   --enable-hpijs-install \
   --enable-hpcups-install \
   --enable-cups-drv-install \
   --enable-cups-ppd-install \
   --with-hpppddir=%{_datadir}/cups/model/HP \
   PYTHON=%{__python}

%__make %{?_smp_mflags}

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%makeinstall

# remove conflict with libsane-backends
#mv %{buildroot}%{_sysconfdir}/sane.d/dll.conf  %{buildroot}%{_sysconfdir}/sane.d/dll.conf.samples.disabled

# remove udev automatic printer configuration conflicting with system-config-printer
# mv %{buildroot}%{_sysconfdir}/udev/rules.d/56-hpmud_add_printer.rules %{buildroot}%{_sysconfdir}/udev/rules.d/56-hpmud_add_printer.rules.samples.disabled

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"


%pre
if [ $1 -ge 1 ]; then
/usr/sbin/groupadd lp -g %{lp_gid} &>/dev/null
/usr/sbin/useradd lp -d /dev/null -s /bin/false \
   -u %{lp_uid} -g %{lp_gid} &>/dev/null
fi
exit 0

%preun
# erase
if [ $1 -eq 0 ]; then
   /sbin/chkconfig --del hplip
   /usr/sbin/groupdel lp &>/dev/null
   /usr/sbin/userdel lp &>/dev/null
#   service hplip stop
#   service cups restart
fi
/sbin/ldconfig
:

%postun
# update
#if [ $1 -eq 1 ]; then
#   service hplip restart
#   service cups restart
#fi
[ -e %{_sysconfdir}/sane.d/dll.conf ] || exit 1
grep hpaio %{_sysconfdir}/sane.d/dll.conf >/dev/null ||
   echo "hpaio" >> %{_sysconfdir}/sane.d/dll.conf
/sbin/ldconfig
:

%files
%defattr(-,root,root)
%{_sysconfdir}/udev/rules.d/56-hpmud.rules
#%{_sysconfdir}/xdg/autostart/hplip-systray.desktop
%dir %{_sysconfdir}/hp
%{_sysconfdir}/hp/hplip.conf
#%{_sysconfdir}/cron.daily/hplip_cron
%{_bindir}/hp-*
%{_bindir}/hpijs
%{_prefix}/lib/cups/backend/hp*
%{_prefix}/lib/cups/filter/foomatic-rip-hplip
#%{_prefix}/lib/cups/filter/hpcac
%{_prefix}/lib/cups/filter/hpcups
%{_prefix}/lib/cups/filter/hpcupsfax
#%{_prefix}/lib/cups/filter/hplipjs
%{_prefix}/lib/cups/filter/hpps
%{_prefix}/lib/cups/filter/pstotiff
#%{_prefix}/lib/systemd/system/hplip-printer@...
%{_libdir}/libhpip.so.*
%{_libdir}/libhpmud.so.*
%{_libdir}/sane/libsane-hpaio.so.*
%{_libdir}/sane/libsane-hpaio.so
#%{_libdir}/menu/hplip
%{python_sitearch}/*.so
%{python_sitearch}/cupsext.la
%{python_sitearch}/hpmudext.la
%{python_sitearch}/scanext.la
%{python_sitearch}/pcardext.la
#%{_datadir}/applications/hplip.desktop
%{_datadir}/cups/drv/hp/hpijs.drv
%{_datadir}/cups/drv/hp/hpcups.drv
%if "%{cups_ver}" == "1.4"
%{_sysconfdir}/cups/pstotiff.*
%else
%{_datadir}/cups/mime/pstotiff.*
%endif
%dir %{_datadir}/hplip
%{_datadir}/hplip/*
%{_datadir}/cups/model/HP/*
%{_datadir}/hal/fdi/preprobe/10osvendor/20-hplip-devices.fdi
%dir %attr(0755,root,lp) /var/lib/hp
#%config(noreplace) /var/lib/hp/hplip.state
#%dir %attr(0774,root,lp) /var/log/hp
#
# systemd printer setup for hplip
%{_sysconfdir}/dbus-1/system.d/com.hp.hplip.conf
%{_sysconfdir}/sane.d/dll.conf
%{_libdir}/systemd/system/hplip-printer@.service
%{_datadir}/dbus-1/system-services/com.hp.hplip.service
%{_datadir}/polkit-1/actions/com.hp.hplip.policy



%files devel
%defattr(-,root,root)
%{_libdir}/libhpip.la
%{_libdir}/libhpip.so
%{_libdir}/libhpmud.la
%{_libdir}/libhpmud.so
%{_libdir}/sane/libsane-hpaio.la
%{_datadir}/doc/*

%changelog
* Wed Mar 26  2014 build -5
- added systemd  files
* Wed Mar 26  2014 build 2
- inital rebuild release hplip-3.14.3.run on oss 13.1 RPI
- updated Requires and BuildRequires
- disabled GUI build due headless printer server with CUPS+Samba
