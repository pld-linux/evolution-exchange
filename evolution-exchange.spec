# 
# configure: WARNING:
# No NTLM support in OpenLDAP; Plaintext password authentication will be
# used when connecting to the Global Catalog server. Consider installing
# the evo-openldap package, or building OpenLDAP with the patch in
# docs/openldap-ntlm.diff
#
%define	filterout_ld	-Wl,--as-needed
Summary:	Microsoft Exchange support for Evolution
Summary(pl.UTF-8):	Wsparcie dla Microsoft Exchange w Evolution
Name:		evolution-exchange
Version:	2.8.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/evolution-exchange/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	8a6be6640c7824285088f6a2e98f12a4
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.8.3
BuildRequires:	evolution-devel >= 2.8.3
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	heimdal-devel >= 0.7
BuildRequires:	intltool >= 0.35.4
BuildRequires:	libbonobo-devel >= 2.16.0
BuildRequires:	libglade2-devel >= 2.6.0
BuildRequires:	libgnomeprint-devel >= 2.12.1
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libsoup-devel >= 2.2.99
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2 >= 2.16.0
Requires:	evolution >= 2.8.3
Requires:	gtk+2 >= 2:2.10.9
Obsoletes:	ximian-connector
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package adds support for Microsoft Exchange 2000 and 2003 to
Evolution.

%description -l pl.UTF-8
Ten pakiet dodaje do Evolution obsługę Microsoft Exchange 2000 i 2003.

%prep
%setup -q

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

%find_lang %{name}-2.8

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-2.8.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/exchange-connector-setup-*
%attr(755,root,root) %{_libdir}/evolution-data-server-*/camel-providers/*.so
%attr(755,root,root) %{_libdir}/evolution/*/evolution-exchange-storage
%{_datadir}/%{name}
%{_gtkdocdir}/*
%{_libdir}/bonobo/servers/*
%{_libdir}/evolution-data-server-*/camel-providers/*.urls
