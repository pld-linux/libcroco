Summary:	A CSS2 parsing library
Summary(pl):	Biblioteka analizująca CSS2
Name:		libcroco
Version:	0.5.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	19e016a5533449a769662a116df7237c
Patch0:		%{name}-link.patch
BuildRequires:	autoconf >= 2.5
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	pkgconfig >= 0.8
Requires:	glib2 >= 2.0
Requires:	libxml2 >= 2.4.23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSS2 parsing and manipulation library for GNOME.

%description -l pl
Biblioteka analizująca i obrabiająca CSS2 dla GNOME.

%package devel
Summary:	Header files for developing with libcroco
Summary(pl):	Pliki nagłówkowe do tworzenia programów używających libcroco
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	libxml2-devel >= 2.4.23

%description devel
This package provides the necessary header files files to allow you
to develop with libcroco.

%description devel -l pl
Ten pakiet dostarcza pliki nagłówkowe potrzebne do tworzenia
oprogramowania korzystającego z libcroco.

%package static
Summary:	Static version of libcroco library
Summary(pl):	Statyczna wersja biblioteki libcroco
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install docs/examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
