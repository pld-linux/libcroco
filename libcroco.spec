#
# Conditional build:
%bcond_without	gnome	# without layout engine (which requires libgnomeui)
#
# NOTE: layeng could be separated, but pkg-config --libs libcroco returns
#	all built libraries together...
#
Summary:	A CSS2 parsing library
Summary(pl):	Biblioteka analizuj±ca CSS2
Name:		libcroco
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libcroco/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	0bb1d64abdd4d0b85f2896e01d67b214
Patch0:		%{name}-link.patch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.3.3.1-2}
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	pango-devel >= 1.0.4
BuildRequires:	pkgconfig >= 0.8
Requires:	glib2 >= 2.0
Requires:	libxml2 >= 2.4.23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSS2 parsing and manipulation library for GNOME.

%description -l pl
Biblioteka analizuj±ca i obrabiaj±ca CSS2 dla GNOME.

%package devel
Summary:	Header files for developing with libcroco
Summary(pl):	Pliki nag³ówkowe do tworzenia programów u¿ywaj±cych libcroco
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel >= 2.0
# for seleng (but always reported by *-config)
Requires:	libxml2-devel >= 2.4.23
# for layeng (but always reported by *-config)
%{?with_gnome:Requires:	libgnomeui-devel >= 2.3.3.1-2}

%description devel
This package provides the necessary header files files to allow you
to develop with libcroco.

%description devel -l pl
Ten pakiet dostarcza pliki nag³ówkowe potrzebne do tworzenia
oprogramowania korzystaj±cego z libcroco.

%package static
Summary:	Static version of libcroco library
Summary(pl):	Statyczna wersja biblioteki libcroco
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libcroco library.

%description static -l pl
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
	--enable-seleng=yes \
	--enable-layeng=%{?with_gnome:yes}%{!?with_gnome:no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install docs/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/csslint
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/csslint.1*

%files devel
%defattr(644,root,root,755)
%doc docs/usage.txt
%attr(755,root,root) %{_bindir}/croco-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libcroco
%{_pkgconfigdir}/libcroco.pc
%{_mandir}/man1/croco-config.1*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
