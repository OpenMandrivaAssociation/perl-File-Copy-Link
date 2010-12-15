%define upstream_name    File-Copy-Link
%define upstream_version 0.112

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Reading and resolving symbolic links
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Spec)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'File::Spec::Link' is an extension to 'File::Spec', adding methods for
resolving symbolic links; it was created to implement 'File::Copy::Link'.

* 'linked($link)'

  Returns the filename linked to by '$link': by 'readlink'ing '$link', and
  resolving that path relative to the directory of '$link'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/copylink
/usr/share/man/man1/copylink.1.xz

