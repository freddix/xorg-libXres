Summary:	X Resource usage extension library
Name:		xorg-libXres
Version:	1.0.7
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.bz2
# Source0-md5:	45ef29206a6b58254c81bea28ec6c95f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel >= 1.3.2
BuildRequires:	xorg-proto >= 7.7
BuildRequires:	xorg-util-macros
Requires:	xorg-libXext >= 1.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Resource usage extension library.

%package devel
Summary:	Header files for libXres library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Resource usage extension library.

This package contains the header files needed to develop programs that
use libXres.

%prep
%setup -qn libXres-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXRes.so.?
%attr(755,root,root) %{_libdir}/libXRes.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXRes.so
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xres.pc
%{_mandir}/man3/*.3x*

