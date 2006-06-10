# 
# configure: WARNING:
# No NTLM support in OpenLDAP; Plaintext password authentication will be
# used when connecting to the Global Catalog server. Consider installing
# the evo-openldap package, or building OpenLDAP with the patch in
# docs/openldap-ntlm.diff
#
Summary:	Microsoft Exchange support for Evolution
Summary(pl):	Wsparcie dla Microsoft Exchange w Evolution
Name:		evolution-exchange
Version:	2.6.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/evolution-exchange/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	027cc03c5d8f95f4eb26603781e49816
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.6.0
BuildRequires:	evolution-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2:2.8.12
BuildRequires:	heimdal-devel >= 0.7
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libsoup-devel >= 2.2.7
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	evolution >= 2.6.0
Requires:	gtk+2 >= 2:2.8.12
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
%{__intltoolize}
%{__glib_gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-openlda-=/usr \
	--with-krb5=/usr \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-*/camel-providers/*.{la,a}

%find_lang %{name}-2.6

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-2.6.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/ximian-connector-setup-*
%attr(755,root,root) %{_libdir}/evolution-data-server-*/camel-providers/*.so
%attr(755,root,root) %{_libdir}/evolution/*/evolution-exchange-storage
%{_datadir}/%{name}
%{_gtkdocdir}/*
%{_libdir}/bonobo/servers/*
%{_libdir}/evolution-data-server-*/camel-providers/*.urls
