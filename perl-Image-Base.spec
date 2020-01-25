#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Image
%define		pnam	Base
Summary:	Image::Base perl module
Summary(pl.UTF-8):	Moduł perla Image::Base
Name:		perl-Image-Base
Version:	1.16
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	493dad8c06dcab2a65e5ff717e8da80e
URL:		http://search.cpan.org/dist/Image-Base/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base class for loading, manipulating and saving images.

%description -l pl.UTF-8
Bazowa klasa do ładowania, manipulowania i zapisywania obrazków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Image/*
%{_mandir}/man[3]/*
