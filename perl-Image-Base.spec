%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Base
Summary:	Image::Base perl module
Summary(pl):	Modu³ perla Image::Base
Name:		perl-Image-Base
Version:	1.07
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	49e524c89ccdf197b7b73b148d8e27e6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base class for loading, manipulating and saving images.

%description -l pl
Bazowa klasa do ³adowania, manipulowania i zapisywania obrazków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Image/*
%{_mandir}/man[3]/*
