Summary:	GTK-widgets for libexif
Summary(pl):	Widgety GTK do libexif
Name:		libexif-gtk
Version:	0.3.3
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/libexif/%{name}-%{version}.tar.bz2
# Source0-md5:	8b3e9bfba3432d29374320fc6f352652
Patch0:		%{name}-gtk24.patch
Patch1:		%{name}-libexif06.patch
URL:		http://libexif.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libexif-devel >= 0.5.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libexif-gtk library.

%description static -l pl
Statyczna wersja biblioteki libexif-gtk.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1

%build
%{__gettextize}
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libexif-gtk
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
