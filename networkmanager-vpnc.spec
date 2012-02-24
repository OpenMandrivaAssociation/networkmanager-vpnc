%define nm_version          0.9.2.0
%define vpnc_version        0.4
%define shared_mime_version 0.16-3

Summary:	NetworkManager VPN integration for vpnc
Name:		networkmanager-vpnc
Epoch:		1
Version:	0.9.2.0
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-vpnc/0.9/NetworkManager-vpnc-%{version}.tar.xz

BuildRequires: gettext
BuildRequires: intltool
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libnm-util) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib) >= %{nm_version}
BuildRequires: pkgconfig(libnm-glib-vpn) >= %{nm_version}
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libpng15)
Requires: gtk+3
Requires: dbus
Requires: NetworkManager	>= %{nm_version}
Requires: vpnc				>= %{vpnc_version}
Requires: shared-mime-info	>= %{shared_mime_version}
Requires: GConf2
Requires: gnome-keyring
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
This package contains software for integrating the vpnc VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -qn NetworkManager-vpnc-%{version}

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la

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
# For now disabled in upstream
#{_datadir}/applications/nm-vpnc.desktop
%{_datadir}/icons/hicolor/48x48/apps/gnome-mime-application-x-cisco-vpn-settings.png
