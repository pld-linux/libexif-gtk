Summary:	GTK+ widgets for libexif
Summary(pl):	Widgety GTK+ do libexif
Name:		libexif-gtk
Version:	0.3.5
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/libexif/%{name}-%{version}.tar.bz2
# Source0-md5:	0ecdba41f3e0f20a11b8555bd2dd2a07
URL:		http://libexif.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libexif-devel >= 1:0.6.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libexif >= 1:0.6.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of GTK+ widgets for libexif.

%description -l pl
Biblioteka widget�w GTK+ do libexif.

%package devel
Summary:	Header files for libexif-gtk
Summary(pl):	Pliki nag��wkowe do libexif-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel
Requires:	libexif-devel >= 1:0.6.9

%description devel
Header files for libexif-gtk.

%description devel -l pl
Pliki nag��wkowe do libexif-gtk.

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
