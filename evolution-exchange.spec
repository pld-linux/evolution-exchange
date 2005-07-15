Summary:	Microsoft Exchange support for Evolution
Summary(pl):	Obs³uga Microsoft Exchange dla Evolution
Name:		evolution-exchange
Version:	2.3.5
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/evolution-exchange/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	c482766dd37172d59bca602fd1d02a2d
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.3.1
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	heimdal-devel >= 0.7
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.11.0
BuildRequires:	libsoup-devel >= 2.2.3
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	evolution >= 2.3.5
Requires:	gtk+2 >= 2:2.6.4
Obsoletes:	ximian-connector
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package adds support for Microsoft Exchange 2000 and 2003 to
Evolution.

%description -l pl
Ten pakiet dodaje do Evolution obs³ugê Microsoft Exchange 2000 i 2003.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-openlda-=/usr \
	--with-krb5=/usr \
	--disable-schemas-install \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-*/camel-providers/*.{la,a}

%find_lang %{name}-2.4

%clean
rm -rf $RPM_BUILD_ROOT

#post
#gconf_schema_install evolution-webcal.schemas

#preun
#gconf_schema_uninstall evolution-webcal.schemas

%files -f %{name}-2.4.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/ximian-connector-setup-*
%attr(755,root,root) %{_libdir}/evolution/*/evolution-exchange-storage
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/evolution-data-server-*/camel-providers/*.so
#%attr(755,root,root) %{_libdir}/evolution/*/*.so.*
%{_libdir}/evolution-data-server-*/camel-providers/*.urls
%{_datadir}/%{name}
%{_gtkdocdir}/*
