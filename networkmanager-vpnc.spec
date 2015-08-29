%define	url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	NetworkManager VPN integration for vpnc
Name:		networkmanager-vpnc
Epoch:		1
Version:	1.0.6
Release:	1
License:	GPLv2+
Group:		System/Base
Url:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-vpnc/%{url_ver}/NetworkManager-vpnc-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libnm-gtk) >= 1.0.5
BuildRequires:	pkgconfig(libsecret-unstable)
Requires:	gtk+3
Requires:	dbus
Requires:	NetworkManager
Requires:	vpnc
Requires:	shared-mime-info
Requires:	gnome-keyring
Requires(post,postun): desktop-file-utils

%description
This package contains software for integrating the vpnc VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -qn NetworkManager-vpnc-%{version}
%apply_patches

%build
%configure \
	--enable-more-warnings=yes \
	--with-gtkver=3 \
	--with-tests=yes

%make

%install
%makeinstall_std

%find_lang NetworkManager-vpnc

%files -f NetworkManager-vpnc.lang
%doc AUTHORS ChangeLog
%{_libexecdir}/nm-vpnc-auth-dialog
%{_libexecdir}/nm-vpnc-service
%{_libexecdir}/nm-vpnc-service-vpnc-helper
%{_libdir}/NetworkManager/libnm-vpnc-properties.so
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-vpnc-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-vpnc-service.name
%{_datadir}/gnome-vpn-properties/vpnc/nm-vpnc-dialog.ui
%{_datadir}/applications/nm-vpnc-auth-dialog.desktop
%{_iconsdir}/hicolor/48x48/apps/gnome-mime-application-x-cisco-vpn-settings.png

