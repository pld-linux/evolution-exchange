#
%define	filterout_ld	-Wl,--as-needed
Summary:	Microsoft Exchange support for Evolution
Summary(pl.UTF-8):	Wsparcie dla Microsoft Exchange w Evolution
Name:		evolution-exchange
Version:	3.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-exchange/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	990806e5baf55be0411f1fdf5a67f601
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= 3.2.0
BuildRequires:	evolution-devel >= 3.2.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	nss-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,preun):	GConf2
Requires:	evolution >= 3.2.0
Requires:	gtk+3 >= 3.0.0
Obsoletes:	ximian-connector
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package adds support for Microsoft Exchange 2000 and 2003 to
Evolution.

%description -l pl.UTF-8
Ten pakiet dodaje do Evolution obsługę Microsoft Exchange 2000 i 2003.

%package apidocs
Summary:	Microsoft Exchange support for Evolution API documentation
Summary(pl.UTF-8):	Dokumentacja API wsparcia Microsoft Exchange w Evolution
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Microsoft Exchange support for Evolution API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API wsparcia Microsoft Exchange w Evolution.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-openldap=/usr \
	--disable-schemas-install \
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution-data-server/{addressbook-backends,calendar-backends,camel-providers}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution-exchange/3.2/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/*/plugins/*.la

%find_lang %{name}-3.2

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_exchange_addressbook-3.2.schemas

%preun
%gconf_schema_uninstall apps_exchange_addressbook-3.2.schemas

%files -f %{name}-3.2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/apps_exchange_addressbook-3.2.schemas
%attr(755,root,root) %{_bindir}/exchange-connector-setup-3.2
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendexchange.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendexchange.so
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelexchange.so
%{_libdir}/evolution-data-server/camel-providers/libcamelexchange.urls
%dir %{_libdir}/evolution-exchange
%dir %{_libdir}/evolution-exchange/3.2
%attr(755,root,root) %{_libdir}/evolution-exchange/3.2/libevolution-exchange-shared.so
%attr(755,root,root) %{_libdir}/evolution-exchange/3.2/libexchange-storage.so
%attr(755,root,root) %{_libdir}/evolution-exchange/3.2/libexchange.so*
%attr(755,root,root) %{_libdir}/evolution-exchange/3.2/libxntlm.so*
%attr(755,root,root) %{_libdir}/evolution/3.2/plugins/liborg-gnome-exchange-operations.so
%{_libdir}/evolution/3.2/plugins/org-gnome-exchange-operations.eplug
%{_datadir}/evolution/3.2/errors/org-gnome-exchange-operations.error
%{_datadir}/evolution-exchange

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/evolution-exchange
