#
# Conditional build:
%bcond_without	static_libs	# don't build static library

%define		mver	0.6
Summary:	A CSS2 parsing library
Summary(pl.UTF-8):	Biblioteka analizująca CSS2
Name:		libcroco
Version:	0.6.8
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libcroco/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	767e73c4174f75b99695d4530fd9bb80
BuildRequires:	autoconf >= 2.5
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtk-doc-automake >= 1.0
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig >= 1:0.8
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--with-html-dir=%{_gtkdocdir}
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
%attr(755,root,root) %{_bindir}/csslint-%{mver}
%attr(755,root,root) %{_libdir}/libcroco-%{mver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcroco-%{mver}.so.3

%files devel
%defattr(644,root,root,755)
%doc docs/usage.txt
%attr(755,root,root) %{_bindir}/croco-%{mver}-config
%attr(755,root,root) %{_libdir}/libcroco-%{mver}.so
%{_includedir}/libcroco-%{mver}
%{_libdir}/libcroco-%{mver}.la
%{_pkgconfigdir}/libcroco-%{mver}.pc
%{_examplesdir}/%{name}-%{version}
%{_gtkdocdir}/libcroco

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcroco-%{mver}.a
%endif
