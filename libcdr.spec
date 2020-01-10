%global apiversion 0.0

Name: libcdr
Version: 0.0.14
Release: 1%{?dist}
Summary: A library providing ability to interpret and import Corel Draw drawings

Group: System Environment/Libraries
License: GPLv2+ or LGPLv2+ or MPLv1.1
URL: http://www.freedesktop.org/wiki/Software/libcdr
Source: http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: lcms2-devel
BuildRequires: libicu-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: zlib-devel

%description
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
Group: Documentation
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary: Tools to transform Corel Draw drawings into other formats
Group: Applications/Publishing
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Corel Draw drawings into other formats.
Currently supported: XHTML, text, raw.


%prep
%setup -q


%build
%configure --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog COPYING.* README
%{_libdir}/%{name}-%{apiversion}.so.*


%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc


%files doc
%doc COPYING.*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html


%files tools
%{_bindir}/cdr2raw
%{_bindir}/cdr2text
%{_bindir}/cdr2xhtml
%{_bindir}/cmx2raw
%{_bindir}/cmx2text
%{_bindir}/cmx2xhtml


%changelog
* Fri May 17 2013 David Tardon <dtardon@redhat.com> - 0.0.14-1
- new release

* Tue Apr 23 2013 David Tardon <dtardon@redhat.com> - 0.0.13-1
- new relese

* Mon Apr 08 2013 David Tardon <dtardon@redhat.com> - 0.0.12-1
- new release

* Sat Mar 02 2013 David Tardon <dtardon@redhat.com> - 0.0.11-1
- new release

* Thu Jan 31 2013 David Tardon <dtardon@redhat.com> - 0.0.10-2
- rebuild for ICU change

* Mon Jan 28 2013 David Tardon <dtardon@redhat.com> - 0.0.10-1
- new release

* Tue Jan 08 2013 David Tardon <dtardon@redhat.com> - 0.0.9-2
- Resolves: rhbz#891082 libreoffice Impress constantly crashes

* Mon Oct 08 2012 David Tardon <dtardon@redhat.com> - 0.0.9-1
- new upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 David Tardon <dtardon@redhat.com> 0.0.8-1
- new upstream release
- adds basic initial primitive uncomplete text support

* Thu Apr 26 2012 David Tardon <dtardon@redhat.com> 0.0.7-1
- new upstream release

* Tue Apr 03 2012 David Tardon <dtardon@redhat.com> 0.0.6-1
- new upstream release

* Mon Mar 19 2012 David Tardon <dtardon@redhat.com> 0.0.5-1
- new upstream release
- fix license

* Sat Mar 10 2012 David Tardon <dtardon@redhat.com> 0.0.3-2
- remove Requires: of main package from -doc subpackage

* Thu Mar 01 2012 David Tardon <dtardon@redhat.com> 0.0.3-1
- initial import
