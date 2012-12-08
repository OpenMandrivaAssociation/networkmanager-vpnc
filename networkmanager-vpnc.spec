%define nm_version          0.9.6.0
%define vpnc_version        0.4
%define shared_mime_version 0.16-3

Summary:	NetworkManager VPN integration for vpnc
Name:		networkmanager-vpnc
Epoch:		1
Version:	0.9.6.0
Release:	2
License:	GPLv2+
Group:		System/Base
URL:		http://www.gnome.org/projects/NetworkManager/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-vpnc/NetworkManager-vpnc-%{version}.tar.xz
# ubuntu
Patch0:	gtk_table_to_gtk_grid.patch

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
%apply_patches

%build
%configure2_5x --disable-static --enable-more-warnings=yes --with-gtkver=3 --with-tests=yes


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
%{_datadir}/applications/nm-vpnc-auth-dialog.desktop
%{_datadir}/icons/hicolor/48x48/apps/gnome-mime-application-x-cisco-vpn-settings.png


%changelog
* Wed Aug 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 1:0.9.6.0-1
+ Revision: 812540
- update to new version 0.9.6.0

* Sat Feb 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1:0.9.2.0-1
+ Revision: 780668
- added p0 to fix gtk3 deprecation build failures
- move to build 0.9.2.0

* Sun Nov 13 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.8.6.0-1
+ Revision: 730417
- 0.8.6.0
- 0.9.2.0

* Thu Apr 21 2011 Funda Wang <fwang@mandriva.org> 1:0.8.4-1
+ Revision: 656420
- new version 0.8.4
- revert changed
- update to new version 0.8.996

* Sat Mar 05 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8.3.995-1
+ Revision: 642105
- update to 0.8.4-beta1

* Fri Nov 05 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8.2-1mdv2011.0
+ Revision: 593783
- 0.8.2 final

* Thu Nov 04 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8.1.999-1mdv2011.0
+ Revision: 593134
- update to 0.8.2-rc1

  + Funda Wang <fwang@mandriva.org>
    - new version 0.8.1

* Sat Jul 17 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8.0.997-1mdv2011.0
+ Revision: 554753
- new version 0.8.1-beta1

* Fri Feb 26 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.8-1mdv2010.1
+ Revision: 511454
- desktop file is disabled upstream for now
- new version

* Sat Jan 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.7.999-1mdv2010.1
+ Revision: 495351
- new version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1:0.7.0-2mdv2010.0
+ Revision: 440328
- rebuild

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1:0.7.0-1mdv2009.1
+ Revision: 308381
- 0.7.0 final

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Mon May 19 2008 David Walluck <walluck@mandriva.org> 1:0.7.0-0.7.7.svn3627.1mdv2009.0
+ Revision: 209009
- import networkmanager-vpnc


* Thu May 01 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-7.7.svn3627
- Update for compat with new NM bits

* Wed Apr 09 2008 Dan Williams <dcbw@redhat.com> 1:0.7.0-6.7.svn3549
- Update for compat with new NM bits

* Tue Mar 25 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.7.svn3502
- Send suggested MTU to NetworkManager

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.7.0-0.7.7.svn3204
- Autorebuild for GCC 4.3

* Fri Jan  4 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.7.svn3204
- Support new vpnc 0.4 Cisco UDP Encapsulation option
- Fix another crash in the properties applet
- Remove upstreamed pcfimport patch

* Mon Nov 26 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.3.svn3109
- Rebuild for updated NetworkManager

* Tue Nov 13 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.2.svn3083
- Rebuild for updated NetworkManager

* Sat Oct 27 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.4.svn3030
- Fix a crash when editing VPN properties a second time

* Tue Oct 23 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn3014
- Rebuild

* Wed Oct 17 2007 Bill Nottingham <notting@redhat.com> - 1:0.7.0-0.3.svn2970
- rebuild (#336261)

* Wed Oct 10 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.2.svn2970
- Fix default username

* Thu Sep 28 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.1.svn2914
- Fix .name file on 64-bit systems

* Fri Sep 28 2007 Jesse Keating <jkeating@redhat.com> - 1:0.7.0-0.2.svn2910
- BuildRequire NetworkManager-glib-devel

* Thu Sep 27 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.1.svn2910
- New snapshot; ported to NM 0.7 API

* Fri Aug 17 2007 Denis Leroy <denis@poolshark.org> - 1:0.6.4-4
- Updated License tag
- Added patch to make properties multilib friendly (#243535)

* Thu Mar 22 2007 Denis Leroy <denis@poolshark.org> - 1:0.6.4-3
- Added patch to improve configuration GUI, add NAT traversal and single DES options

* Sun Feb 18 2007 Denis Leroy <denis@poolshark.org> - 1:0.6.4-2
- Readded NAT-keepalive support patch from SVN branch

* Wed Feb 14 2007 Denis Leroy <denis@poolshark.org> - 1:0.6.4-1
- Downgrading to 1:0.6.4 to keep par with core NM version

* Mon Dec  4 2006 Dan Williams <dcbw@redhat.com> - 0.7.0-0.cvs20061204
- Allow "NAT-Keepalive packet interval" config option

* Sat Oct 21 2006 Denis Leroy <denis@poolshark.org> - 0.7.0-0.cvs20060929.3
- Added patch to support saving group password only

* Thu Oct  5 2006 Denis Leroy <denis@poolshark.org> - 0.7.0-0.cvs20060929.2
- Leave .so link alone, needed by nm

* Fri Sep 29 2006 Denis Leroy <denis@poolshark.org> - 0.7.0-0.cvs20060929.1
- Update to CVS snapshot 060929
- Some rpmlint cleanups

* Fri Sep 29 2006 Denis Leroy <denis@poolshark.org> - 0.7.0-0.cvs20060529.4
- Added XML::Parser BR

* Fri Sep 29 2006 Denis Leroy <denis@poolshark.org> - 0.7.0-0.cvs20060529.3
- Added gettext BR

* Wed Sep 27 2006 Warren Togami <wtogami@redhat.com> - 0.7.0-0.cvs20060529.2
- rebuild for FC6

* Thu Jul 20 2006 Warren Togami <wtogami@redhat.com> - 0.7.0-0.cvs20060529.1
- rebuild for new dbus

* Mon May 29 2006 Dan Williams <dcbw@redhat.com> - 0.7.0-0.cvs20060529
- Gnome.org #336913: HIG tweaks for vpn properties pages

* Sun May 21 2006 Dan Williams <dcbw@redhat.com> 0.7.0-0.cvs20060521
- Update to CVS snapshot
- Honor user-specified rekeying intervals

* Mon May 15 2006 Dan Williams <dcbw@redhat.com> 0.6.2-1
- New release for NM 0.6.2 compat

* Fri Apr 21 2006 Dan Williams <dcbw@redhat.com> 0.6.0-3
- Add dist tag to RPM release

* Wed Apr 12 2006 Christopher Aillon <caillon@redhat.com> 0.6.0-2
- Rekey every 2 hours

* Tue Mar 14 2006 Dan Williams <dcbw@redhat.com> - 0.6.0-1
- Update to CVS snapshot of 0.6 for NM compatibility

* Fri Jan 27 2006 Dan Williams <dcbw@redhat.com> - 0.5.0-1
- CVS snapshot for compatibility new NetworkManager

* Tue Dec  6 2005 Jeremy Katz <katzj@redhat.com> - 0.3-3
- rebuild for new dbus

* Mon Oct 17 2005 Dan Williams <dcbw@redhat.com> 0.3-2
- Rebuild to test new Extras buildsystem

* Thu Aug 18 2005 David Zeuthen <davidz@redhat.com> 0.3-1
- New upstream release
- Bump some versions for deps

* Fri Jul  1 2005 David Zeuthen <davidz@redhat.com> 0.2-2
- Add missing changelog entry for last commit
- Temporarily BuildReq libpng-devel as it is not pulled in by gtk2-devel
  (should be fixed in Core shortly)
- Pull in latest D-BUS (which features automatic reloading of policy files)
  so users do not have to restart the messagebus after installing this package

* Thu Jun 30 2005 David Zeuthen <davidz@redhat.com> 0.2-1
- New upsteam version
- Add the new gnome-mime-application-x-cisco-vpn-settings.png icon and call
  gtk-update-icon-cache as appropriate

* Fri Jun 17 2005 David Zeuthen <davidz@redhat.com> 0.1-2.cvs20050617
- Add Prereq: /usr/bin/update-desktop-database
- Nuke .la and .a files
- Use find_lang macro to handle locale files properly
- Add Requires for suitable version of shared-mime-info since our desktop
  file depends on the application/x-cisco-vpn-settings MIME-type

* Fri Jun 17 2005 David Zeuthen <davidz@redhat.com> 0.1-1.cvs20050617
- Latest CVS snapshot

* Thu Jun 16 2005 David Zeuthen <davidz@redhat.com> 0.1-1
- Initial build
