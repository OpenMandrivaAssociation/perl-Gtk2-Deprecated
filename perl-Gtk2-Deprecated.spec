%define module Gtk2-Deprecated
%define fmodule Gtk2/Deprecated

Summary: Perl module for deprecated gtk+-2.x widgets
Name:    perl-%module
Version: 0.05
Release: %mkrel 5
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  http://asofyet.org/muppet/software/gtk2-perl/%module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: gtk+2-devel perl-devel perl-ExtUtils-Depends perl-Gtk2 > 1.00
BuildRequires: glitz-devel

%description
This module provides perl access to the widgets that were deprecated
in gtk+2.x.


%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%{_mandir}/*/*
%{perl_vendorarch}/%fmodule
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule
%{perl_vendorarch}/Gtk2/*.pod

