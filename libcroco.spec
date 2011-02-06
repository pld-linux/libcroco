#
# Conditional build:
%bcond_without	static_libs	# don't build static library

%define		_mver	0.6
Summary:	A CSS2 parsing library
Summary(pl.UTF-8):	Biblioteka analizująca CSS2
Name:		libcroco
Version:	0.6.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libcroco/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	1429c597aa4b75fc610ab3a542c99209
Patch0:		%{name}-link.patch
BuildRequires:	autoconf >= 2.5
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig >= 1:0.8
Requires:	glib2 >= 1:2.12.0
Requires:	libxml2 >= 1:2.6.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSS2 parsing and manipulation library for GNOME.

%description -l pl.UTF-8
Biblioteka analizująca i obrabiająca CSS2 dla GNOME.

%package devel
Summary:	Header files for developing with libcroco
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów używających libcroco
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.0
Requires:	libxml2-devel >= 1:2.6.26

%description devel
This package provides the necessary header files files to allow you to
develop with libcroco.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki nagłówkowe potrzebne do tworzenia
oprogramowania korzystającego z libcroco.

%package static
Summary:	Static version of libcroco library
Summary(pl.UTF-8):	Statyczna wersja biblioteki libcroco
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libcroco library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libcroco.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install docs/examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/csslint-%{_mver}
%attr(755,root,root) %{_libdir}/libcroco-%{_mver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcroco-%{_mver}.so.3

%files devel
%defattr(644,root,root,755)
%doc docs/usage.txt
%attr(755,root,root) %{_bindir}/croco-%{_mver}-config
%attr(755,root,root) %{_libdir}/libcroco-%{_mver}.so
%{_libdir}/libcroco-%{_mver}.la
%{_includedir}/libcroco-%{_mver}
%{_pkgconfigdir}/libcroco-%{_mver}.pc
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcroco-%{_mver}.a
%endif
