Summary:	GTK-widgets for libexif
Summary(pl):	Widgety GTK do libexif
Name:		libexif-gtk
Version:	0.3.3
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/libexif/%{name}-%{version}.tar.bz2
URL:		http://libexif.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libexif-devel >= 0.5.9
Requires:	libexif >= 0.5.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Library of GTK-widgets for libexif.

%description -l pl
Biblioteka widgetów GTK do libexif.

%package devel
Summary:	Header files for libexif-gtk
Summary(pl):	Pliki nag³ówkowe do libexif-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel
Requires:	libexif-devel >= 0.5.9

%description devel
Header files for libexif-gtk.

%description devel -l pl
Pliki nag³ówkowe do libexif-gtk.

%package static
Summary:	Static libexif-gtk library
Summary(pl):	Statyczna biblioteka libexif-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libexif-gtk library.

%description static -l pl
Statyczna wersja biblioteki libexif-gtk.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libexif-gtk
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
