#
%define	filterout_ld	-Wl,--as-needed
Summary:	Microsoft Exchange support for Evolution
Summary(pl.UTF-8):	Wsparcie dla Microsoft Exchange w Evolution
Name:		evolution-exchange
Version:	2.12.3
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-exchange/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	1bdda76724a17fb7606abcdfdb6ec170
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.12.0
BuildRequires:	evolution-devel >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	krb5-devel
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonobo-devel >= 2.20.0
BuildRequires:	libglade2-devel >= 2.6.2
BuildRequires:	libgnomeprint-devel >= 2.18.0
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libsoup-devel >= 2.2.100
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	sed >= 4.0
Requires(post,preun):	GConf2
Requires:	evolution >= 2.12.0
Requires:	gtk+2 >= 2:2.12.0
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

sed -i -e s#sr\@Latn#sr\@latin# po/LINGUAS
mv po/sr\@{Latn,latin}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-openldap=/usr \
	--with-krb5=/usr \
	--disable-schemas-install \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-*/camel-providers/*.{la,a}

%find_lang %{name}-2.12

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_exchange_addressbook-2.12.schemas

%preun
%gconf_schema_uninstall apps_exchange_addressbook-2.12.schemas

%files -f %{name}-2.12.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/apps_exchange_addressbook-2.12.schemas
%attr(755,root,root) %{_bindir}/exchange-connector-setup-*
%attr(755,root,root) %{_libdir}/evolution-data-server-*/camel-providers/*.so
%attr(755,root,root) %{_libdir}/evolution/*/evolution-exchange-storage
%{_datadir}/%{name}
%{_libdir}/bonobo/servers/*
%{_libdir}/evolution-data-server-*/camel-providers/*.urls

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/*
