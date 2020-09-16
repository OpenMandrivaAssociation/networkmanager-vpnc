%define	url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for vpnc
Name:		networkmanager-vpnc
Epoch:		1
Version:	1.2.6
Release:	3
License:	GPLv2+
Group:		System/Base
Url:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-vpnc/%{url_ver}/NetworkManager-vpnc-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libsecret-unstable)
BuildRequires:	pkgconfig(libnma)
Requires:	gtk+3
Requires:	dbus
Requires:	NetworkManager
Requires:	vpnc
Requires:	shared-mime-info
Requires(post,postun): desktop-file-utils

%description
This package contains software for integrating the vpnc VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -qn NetworkManager-vpnc-%{version}
%autopatch -p1

%build
%configure \
	--enable-more-warnings=yes \
	--with-gtkver=3 \
	--with-tests=yes \
	--without-libnm-glib

%make_build

%install
%make_install

%find_lang NetworkManager-vpnc

%files -f NetworkManager-vpnc.lang
%doc AUTHORS ChangeLog
%{_libexecdir}/nm-vpnc-auth-dialog
%{_libexecdir}/nm-vpnc-service
%{_libexecdir}/nm-vpnc-service-vpnc-helper
%{_libdir}/NetworkManager/*.so
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-vpnc-service.conf
%{_datadir}/gnome-vpn-properties/vpnc/nm-vpnc-dialog.ui
%{_prefix}/lib/NetworkManager/VPN/nm-vpnc-service.name
%{_datadir}/appdata/network-manager-vpnc.metainfo.xml
