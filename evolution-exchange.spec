#
%define	filterout_ld	-Wl,--as-needed
Summary:	Microsoft Exchange support for Evolution
Summary(pl.UTF-8):	Wsparcie dla Microsoft Exchange w Evolution
Name:		evolution-exchange
Version:	2.28.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-exchange/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	82f70761960c7e9efdb24650c1b3229b
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 2.28.2
BuildRequires:	evolution-devel >= 2.28.2
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.1
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonobo-devel >= 2.22.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	evolution >= 2.28.2
Requires:	gtk+2 >= 2:2.12.8
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-openldap=/usr \
	--disable-schemas-install \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-*/camel-providers/*.{la,a}

%find_lang %{name}-2.28

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_exchange_addressbook-2.28.schemas

%preun
%gconf_schema_uninstall apps_exchange_addressbook-2.28.schemas

%files -f %{name}-2.28.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/apps_exchange_addressbook-2.28.schemas
%attr(755,root,root) %{_bindir}/exchange-connector-setup-2.28
%attr(755,root,root) %{_libdir}/evolution-data-server-1.2/camel-providers/libcamelexchange.so
%attr(755,root,root) %{_libdir}/evolution/2.28/evolution-exchange-storage
%{_datadir}/evolution-exchange
%{_libdir}/bonobo/servers/GNOME_Evolution_Exchange_Storage_2.28.server
%{_libdir}/evolution-data-server-1.2/camel-providers/libcamelexchange.urls

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/evolution-exchange
