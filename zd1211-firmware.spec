%define snap 2007-03-19
Name:		zd1211-firmware
Version:	1.4
Release:	4%{?dist}
Summary:	Firmware for wireless devices based on zd1211 chipset
Group:		System Environment/Kernel
License:	GPLv2
URL:		http://zd1211.wiki.sourceforge.net
Source0:	http://downloads.sourceforge.net/zd1211/zd1211-firmware-%{version}.tar.bz2
Patch0:		zd1211-firmware-1.4-build__from_headers.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch


%description
This package contains the firmware required to work with the zd1211 chipset.


%prep
%setup -q -n %{name}
%patch0 -p1
sed -i 's/\r//' *.h

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install FW_DIR=$RPM_BUILD_ROOT/lib/firmware/zd1211 


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING
%dir /lib/firmware/zd1211
/lib/firmware/zd1211/*


%changelog
* Thu Jan  7 2010 John W. Linville <linville@redhat.com> - 1.4-4
- Add dist tag

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 12 2007 kwizart < kwizart at gmail.com > - 1.4-1
- Update to 1.4

* Tue Aug 14 2007 kwizart < kwizart at gmail.com > - 1.3-5
- Drop the dist tag
- Update URL
- Fix directory ownership

* Mon Mar 19 2007 kwizart < kwizart at gmail.com > - 1.3-4
- Update to snap 2007-03-19 but still no changes from Dec 26 2006.
- Drop devel is not usefull
- Use patch for sudo and zd1211b install
- Fix description/summary

* Sun Feb 23 2007 kwizart < kwizart at gmail.com > - 1.3-3
- Update to the snapshot source zd1211rw_fw_2007-02-23
 Timestramp didn't changed from 26-12-2006 so don't think date
 will tell anything in that case. I Prefer to wait for release tarball
 to fix any number version is that necessary.
- Uses of $RPM_OPT_FLAGS in place of CFLAGS += -Wall

* Sun Feb 11 2007 kwizart < kwizart at gmail.com > - 1.3-2
- Bundle the original vendor driver used to generate the firmware.

* Sat Jan  6 2007 kwizart < kwizart at gmail.com > - 1.3-1
- Update to 1.3

* Wed Oct 11 2006 kwizart < kwizart at gmail.com > - 1.2-1_FC5
- inital release.
