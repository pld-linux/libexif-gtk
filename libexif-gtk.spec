#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	gtk2		# GTK+ 2.x version
%bcond_without	gtk3		# GTK+ 3.x version
#
Summary:	GTK+ widgets for libexif
Summary(pl.UTF-8):	Widgety GTK+ do libexif
Name:		libexif-gtk
Version:	0.5.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
#Source0Download: https://github.com/libexif/libexif-gtk/releases
Source0:	https://github.com/libexif/libexif-gtk/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	2bc72a49531cb86096e9038941ec6bda
Patch0:		%{name}-am.patch
URL:		https://libexif.github.io/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.14.1
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.4}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	libexif-devel >= 1:0.6.16
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-common = %{version}-%{release}
Requires:	gtk+2 >= 2:2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of GTK+ widgets for libexif.

%description -l pl.UTF-8
Biblioteka widgetów GTK+ do libexif.

%package devel
Summary:	Development files for libexif-gtk (GTK+ 2.x version)
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libexif-gtk (wersja dla GTK+ 2.x)
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-devel-common = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4

%description devel
Development files for libexif-gtk (GTK+ 2.x version).

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki libexif-gtk (wersja dla GTK+ 2.x).

%package static
Summary:	Static libexif-gtk library (GTK+ 2.x version)
Summary(pl.UTF-8):	Statyczna biblioteka libexif-gtk (wersja dla GTK+ 2.x)
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libexif-gtk library (GTK+ 2.x version).

%description static -l pl.UTF-8
Statyczna biblioteka libexif-gtk (wersja dla GTK+ 2.x).

%package common
Summary:	Common files for both libexif-gtk (GTK+ 2.x/3.x) versions
Summary(pl.UTF-8):	Pliki wspólne dla obu wersji libexif-gtk (GTK+ 2.x/3.x)
Group:		Libraries
Requires:	libexif >= 1:0.6.16

%description common
Common files for both libexif-gtk (GTK+ 2.x/3.x) versions.

%description common -l pl.UTF-8
Pliki wspólne dla obu wersji libexif-gtk (GTK+ 2.x/3.x).

%package devel-common
Summary:	Header files common for both libexif-gtk (GTK+ 2.x/3.x) versions
Summary(pl.UTF-8):	Pliki nagłówkowe wspólne dla obu wersji libexif-gtk (GTK+ 2.x/3.x)
Group:		Development/Libraries
Requires:	%{name}-common = %{version}-%{release}
Requires:	libexif-devel >= 1:0.6.16

%description devel-common
Header files common for both libexif-gtk (GTK+ 2.x/3.x) versions.

%description devel-common -l pl.UTF-8
Pliki nagłówkowe wspólne dla obu wersji libexif-gtk (GTK+ 2.x/3.x).

%package -n libexif-gtk3
Summary:	GTK+ 3.x widgets for libexif
Summary(pl.UTF-8):	Widgety GTK+ 3.x do libexif
Group:		X11/Libraries
Requires:	%{name}-common = %{version}-%{release}
Requires:	gtk+3 >= 3.0

%description -n libexif-gtk3
GTK+ 3.x widgets for libexif.

%description -n libexif-gtk3 -l pl.UTF-8
Widgety GTK+ 3.x do libexif.

%package -n libexif-gtk3-devel
Summary:	Development files for libexif-gtk (GTK+ 3.x version)
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libexif-gtk (wersja dla GTK+ 3.x)
Group:		X11/Development/Libraries
Requires:	%{name}-devel-common = %{version}-%{release}
Requires:	libexif-gtk3 = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0

%description -n libexif-gtk3-devel
Development files for libexif-gtk (GTK+ 3.x version).

%description -n libexif-gtk3-devel -l pl.UTF-8
Pliki programistyczne biblioteki libexif-gtk (wersja dla GTK+ 3.x).

%package -n libexif-gtk3-static
Summary:	Static libexif-gtk library (GTK+ 3.x version)
Summary(pl.UTF-8):	Statyczna biblioteka libexif-gtk (wersja dla GTK+ 3.x)
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n libexif-gtk3-static
Static libexif-gtk library (GTK+ 3.x version).

%description -n libexif-gtk3-static -l pl.UTF-8
Statyczna biblioteka libexif-gtk (wersja dla GTK+ 3.x).

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I auto-m4 -I m4m
%{__autoconf}
%{__autoheader}
%{__automake}

%if %{with gtk2}
install -d gtk2
cd gtk2
../%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}
cd ..
%endif

%if %{with gtk3}
install -d gtk3
cd gtk3
../%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--with-gtk3
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with gtk2}
%{__make} -C gtk2 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libexif-gtk.la
%endif

%if %{with gtk2}
%{__make} -C gtk3 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libexif-gtk3.la
%endif

%find_lang %{name}-5

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n libexif-gtk3 -p /sbin/ldconfig
%postun	-n libexif-gtk3 -p /sbin/ldconfig

%if %{with gtk2}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexif-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexif-gtk.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexif-gtk.so
%{_pkgconfigdir}/libexif-gtk.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libexif-gtk.a
%endif
%endif

%files common -f %{name}-5.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README

%files devel-common
%defattr(644,root,root,755)
%{_includedir}/libexif-gtk

%if %{with gtk3}
%files -n libexif-gtk3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexif-gtk3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexif-gtk3.so.5

%files -n libexif-gtk3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexif-gtk3.so
%{_pkgconfigdir}/libexif-gtk3.pc

%if %{with static_libs}
%files -n libexif-gtk3-static
%defattr(644,root,root,755)
%{_libdir}/libexif-gtk3.a
%endif
%endif
