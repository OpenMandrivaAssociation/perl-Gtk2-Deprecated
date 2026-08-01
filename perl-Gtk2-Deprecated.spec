%define module Gtk2-Deprecated
%define fmodule Gtk2/Deprecated
Summary:	Perl module for deprecated gtk+-2.x widgets
Name:		perl-%{module}
Version:	0.06
Release:	6
License: 	GPL or Artistic
Group:		Development/GNOME and GTK+
URL:		https://gtk2-perl.sf.net/
Source:		http://asofyet.org/muppet/software/gtk2-perl/Gtk2-Deprecated-0.06.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel	
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(Gtk2)
%description
This module provides perl access to the widgets that were deprecated
in gtk+2.x.

%prep
%setup -q -n %{module}-%{version}
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="%{optflags}"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="%{optflags}"
#%make test || :

%install
%makeinstall_std

%check
make test || :

%files
%{_mandir}/*/*
%{perl_vendorarch}/%{fmodule}
%{perl_vendorarch}/%{fmodule}.pm
%{perl_vendorarch}/auto/%{fmodule}
%{perl_vendorarch}/Gtk2/*.pod
%{perl_vendorarch}/Gtk2/Gdk



