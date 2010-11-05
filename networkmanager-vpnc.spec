%define nm_version          0.8.2
%define dbus_version        1.1
%define gtk2_version        2.10.0
%define vpnc_version        0.4
%define shared_mime_version 0.16-3

Summary:   NetworkManager VPN integration for vpnc
Name:      networkmanager-vpnc
Epoch:     1
Version:   0.8.2
Release:   %mkrel 1
License:   GPLv2+
Group:     System/Base
URL:       http://www.gnome.org/projects/NetworkManager/
Source:    http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-vpnc/0.8/NetworkManager-vpnc-%version.tar.bz2
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: libnm-util-devel >= %{nm_version}
BuildRequires: libnm-glib-devel >= %{nm_version}
BuildRequires: libnm-glib-vpn-devel >= %{nm_version}
BuildRequires: libGConf2-devel
BuildRequires: gnomeui2-devel
BuildRequires: libgnome-keyring-devel
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
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This package contains software for integrating the vpnc VPN software
with NetworkManager and the GNOME desktop

%prep
%setup -q -n NetworkManager-vpnc-%{version}

%build
%configure2_5x --disable-static
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la

%find_lang NetworkManager-vpnc

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion <200900
%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f NetworkManager-vpnc.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog
%{_libexecdir}/nm-vpnc-auth-dialog
%{_libexecdir}/nm-vpnc-service
%{_libexecdir}/nm-vpnc-service-vpnc-helper
%{_libdir}/NetworkManager/libnm-vpnc-properties.so
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-vpnc-service.conf
%config(noreplace) %{_sysconfdir}/NetworkManager/VPN/nm-vpnc-service.name
%{_datadir}/gnome-vpn-properties/vpnc/nm-vpnc-dialog.glade
# For now disabled in upstream
#{_datadir}/applications/nm-vpnc.desktop
%{_datadir}/icons/hicolor/48x48/apps/gnome-mime-application-x-cisco-vpn-settings.png
