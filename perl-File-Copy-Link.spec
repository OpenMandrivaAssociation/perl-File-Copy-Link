%define upstream_name    File-Copy-Link
%define upstream_version 0.113

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.113
Release:	2

Summary:	Reading and resolving symbolic links
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/File-Copy-Link-0.113.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildArch:	noarch

%description
'File::Spec::Link' is an extension to 'File::Spec', adding methods for
resolving symbolic links; it was created to implement 'File::Copy::Link'.

* 'linked($link)'

  Returns the filename linked to by '$link': by 'readlink'ing '$link', and
  resolving that path relative to the directory of '$link'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{perl_vendorlib}/*
%{_bindir}/copylink
%{_mandir}/man3/*
%{_mandir}/man1/copylink.1.xz

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.112.0-2mdv2011.0
+ Revision: 656912
- rebuild for updated spec-helper

* Thu Dec 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.112.0-1mdv2011.0
+ Revision: 622194
- import perl-File-Copy-Link


