%define nm_version          1:0.7.0-0.9.3.svn3623
%define dbus_version        1.1
%define gtk2_version        2.10.0
%define vpnc_version        0.4
%define shared_mime_version 0.16-3

%define svn_snapshot svn3627

Summary:   NetworkManager VPN integration for vpnc
Name:      networkmanager-vpnc
Epoch:     1
Version:   0.7.0
Release:   %mkrel 0.7.7.%{svn_snapshot}.1
License:   GPLv2+
Group:     System/Base
URL:       http://www.gnome.org/projects/NetworkManager/
Source:    NetworkManager-vpnc-%{version}.%{svn_snapshot}.tar.gz
Patch0:    NetworkManager-vpnc-0.7.0-gppasswd.patch
Patch1:    NetworkManager-vpnc-0.7.0-desktop.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel             >= %{gtk2_version}
BuildRequires: dbus-devel             >= %{dbus_version}
BuildRequires: NetworkManager-devel   >= %{nm_version}
BuildRequires: NetworkManager-glib-devel >= %{nm_version}
BuildRequires: libGConf2-devel
BuildRequires: gnomeui2-devel
BuildRequires: gnome-keyring-devel
BuildRequires: libglade2.0-devel
BuildRequires: libpng-devel
BuildRequires: intltool gettext

Requires: gtk2             >= %{gtk2_version}
Requires: dbus             >= %{dbus_version}
Requires: NetworkManager   >= %{nm_version}
Requires: vpnc             >= %{vpnc_version}
Requires: shared-mime-info >= %{shared_mime_version}
Requires: GConf2
Requires: gnome-keyring


Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
This package contains software for integrating the vpnc VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -q -n NetworkManager-vpnc-%{version}
%patch0 -p1 -b .grouppswd
%patch1 -p1 -b .desktop


%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/lib*.la
rm -f %{buildroot}%{_libdir}/lib*.a

%find_lang NetworkManager-vpnc


%clean
rm -rf $RPM_BUILD_ROOT


%post
%{update_desktop_database}
%update_icon_cache hicolor


%postun
%{clean_desktop_database}
%clean_icon_cache hicolor


%files -f NetworkManager-vpnc.lang
%defattr(-, root, root)

%doc AUTHORS ChangeLog
%{_libdir}/lib*.so*
%{_libexecdir}/nm-vpnc-auth-dialog
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-vpnc-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-vpnc-service.name
%{_bindir}/nm-vpnc-service
%{_bindir}/nm-vpnc-service-vpnc-helper
%{_datadir}/gnome-vpn-properties/vpnc/nm-vpnc-dialog.glade
%{_datadir}/applications/nm-vpnc.desktop
%{_datadir}/icons/hicolor/48x48/apps/gnome-mime-application-x-cisco-vpn-settings.png

