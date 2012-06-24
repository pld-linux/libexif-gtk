# Revision: 1.21 $, $Date: 2008-11-09 18:41:05 $
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	GTK+ widgets for libexif
Summary(pl.UTF-8):	Widgety GTK+ do libexif
Name:		libexif-gtk
Version:	0.3.5
Release:	7
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/libexif/%{name}-%{version}.tar.bz2
# Source0-md5:	0ecdba41f3e0f20a11b8555bd2dd2a07
Source1:	%{name}-pl.po
Patch0:		%{name}-ac.patch
Patch1:		%{name}-allow-deprecated.patch
URL:		http://libexif.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libexif-devel >= 1:0.6.16
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libexif >= 1:0.6.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of GTK+ widgets for libexif.

%description -l pl.UTF-8
Biblioteka widgetów GTK+ do libexif.

%package devel
Summary:	Header files for libexif-gtk
Summary(pl.UTF-8):	Pliki nagłówkowe do libexif-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel
Requires:	libexif-devel >= 1:0.6.16

%description devel
Header files for libexif-gtk.

%description devel -l pl.UTF-8
Pliki nagłówkowe do libexif-gtk.

%package static
Summary:	Static libexif-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka libexif-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libexif-gtk library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libexif-gtk.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

cp %{SOURCE1} po/pl.po
%{__perl} -pi -e 's/es fr ru/es fr pl ru/' configure.in
rm -f po/stamp-po

%build
%{__gettextize}
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libexif-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexif-gtk.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexif-gtk.so
%{_libdir}/libexif-gtk.la
%{_includedir}/libexif-gtk
%{_pkgconfigdir}/libexif-gtk.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libexif-gtk.a
%endif
