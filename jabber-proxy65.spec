%include /usr/lib/rpm/macros.python
Summary:	A SOCKS5 Bytestreaming Component
Summary(pl):	Komponent strumieniowania bajtów SOCKS5
Name:		jabber-proxy65
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	proxy65-20040523.tar.bz2
# Source0-md5:	b2b8a422da099a73d7dfa1305189959e
Requires:	python-Twisted
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
URL:		http://proxy65.jabberstudio.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proxy65 is a server-side component that enables you to add a SOCKS5
bytestreaming service to a standard Jabber server, mainly to be used
for out-of-band file transfer. For a full definition of the
functionality, please read JEP-0065. It is written in Python and built
on top of the Twisted framework.

%description -l pl
Proxy65 jest komponentem instalowanym po stronie serwera, który
pozwala dodaæ do serwera Jabbera us³ugê SOCKS5, u¿ywan± g³ównie do
transferu plików. Pe³en opis funkcjonalno¶ci znajduje siê w dokumencie
JEP-0065. Proxy65 jest napisane w Pythonie i zbudowane na szkielecie
Twisted.

%prep
%setup -q -n proxy65

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/proxy65
