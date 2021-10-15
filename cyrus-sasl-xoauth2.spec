%define debug_package %{nil}
Name:           cyrus-sasl-xoauth2
Version:        0.2
Release:        1%{?dist}
Summary:        xoauth2 plugin for cyrus-sasl

License:        MIT
URL:            https://github.com/moriyoshi/cyrus-sasl-xoauth2
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  cyrus-sasl-devel
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  sqlite-devel
Requires:       cyrus-sasl

%description
This is a plugin implementation of XOAUTH2.

FYI: if you are forced to use XOAUTH2-enabled SMTP / IMAP servers
by your employer and want to keep using your favorite *nix MUA locally,
the following detailed document should help a lot:
 http://mmogilvi.users.sourceforge.net/software/oauthbearer.html
(DISCLAIMER: in contrast to the document's author, I'd rather read and
write emails on my browser a lot. I haven't tested it personally)

%prep
%setup -q
./autogen.sh

%build
./configure --prefix=/usr --libdir=%{_libdir} --with-plugindir=%{_libdir}/sasl2
sed -i 's%pkglibdir = ${CYRUS_SASL_PREFIX}/lib/sasl2%pkglibdir = ${CYRUS_SASL_PREFIX}/lib64/sasl2%' Makefile
%{make_build}

%install
%{make_install}
libtool --finish %{_libdir}/sasl2

%files
%{_libdir}/sasl2/
%{_libdir}/sasl2/libxoauth2.a
%{_libdir}/sasl2/libxoauth2.la
%{_libdir}/sasl2/libxoauth2.so
%{_libdir}/sasl2/libxoauth2.so.0
%{_libdir}/sasl2/libxoauth2.so.0.0.0

%changelog
* Tue Jun 16 2020 Nurmukhamed Artykaly <nurmukhamed.artykaly@hdfilm.kz> - 0.2
- Initial commit
