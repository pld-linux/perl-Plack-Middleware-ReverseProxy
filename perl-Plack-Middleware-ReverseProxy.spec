#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Plack
%define		pnam	Middleware-ReverseProxy
Summary:	Plack::Middleware::ReverseProxy - Supports app to run as a reverse proxy backend
Name:		perl-Plack-Middleware-ReverseProxy
Version:	0.11
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Plack/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	99748914ad37508ff8a122903e6da2b6
URL:		http://search.cpan.org/dist/Plack-Middleware-ReverseProxy/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Plack
BuildRequires:	perl-Test-Base
BuildRequires:	perl-YAML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plack::Middleware::ReverseProxy resets some HTTP headers, which
changed by reverse-proxy. You can specify the reverse proxy address
and stop fake requests using 'enable_if' directive in your app.psgi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Plack/Middleware/*.pm
%{_mandir}/man3/*
