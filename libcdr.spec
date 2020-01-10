%global apiversion 0.1

Name: libcdr
Version: 0.1.1
Release: 1%{?dist}
Summary: A library for import of CorelDRAW drawings

# the only Public Domain source is src/lib/CDRColorProfiles.h
License: MPLv2.0 and Public Domain
URL: http://wiki.documentfoundation.org/DLP/Libraries/libcdr
Source: http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: help2man
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(zlib)

%description
Libcdr is library providing ability to interpret and import CorelDRAW
drawings into various applications. You can find it being used in
libreoffice.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary: Tools to transform CorelDRAW drawings into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform CorelDRAW drawings into other formats.
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

export LD_LIBRARY_PATH=`pwd`/src/lib/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'debug the conversion library' -o cdr2raw.1 ./src/conv/raw/.libs/cdr2raw
help2man -N -n 'convert CorelDRAW document into HTML' -o cdr2xhtml.1 ./src/conv/svg/.libs/cdr2xhtml
help2man -N -n 'convert CorelDRAW document into plain text' -o cdr2text.1 ./src/conv/text/.libs/cdr2text
help2man -N -n 'debug the conversion library' -o cmx2raw.1 ./src/conv/raw/.libs/cmx2raw
help2man -N -n 'convert Corel Presentation Exchange file into HTML' -o cmx2xhtml.1 ./src/conv/svg/.libs/cmx2xhtml
help2man -N -n 'convert Corel Presentation Exchange file into plain text' -o cmx2text.1 ./src/conv/text/.libs/cmx2text

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
# rhbz#1001251 we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0644 cdr2*.1 cmx2*.1 %{buildroot}/%{_mandir}/man1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING.MPL README
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%doc COPYING.MPL
%doc docs/doxygen/html

%files tools
%{_bindir}/cdr2raw
%{_bindir}/cdr2text
%{_bindir}/cdr2xhtml
%{_bindir}/cmx2raw
%{_bindir}/cmx2text
%{_bindir}/cmx2xhtml
%{_mandir}/man1/cdr2raw.1*
%{_mandir}/man1/cdr2text.1*
%{_mandir}/man1/cdr2xhtml.1*
%{_mandir}/man1/cmx2raw.1*
%{_mandir}/man1/cmx2text.1*
%{_mandir}/man1/cmx2xhtml.1*

%changelog
* Fri Apr 17 2015 David Tardon <dtardon@redhat.com> - 0.1.1-1
- Resolves: rhbz#1207750 rebase to 0.1.1

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.0.14-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.0.14-2
- Mass rebuild 2013-12-27

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
