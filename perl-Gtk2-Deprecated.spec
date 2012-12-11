%define module Gtk2-Deprecated
%define fmodule Gtk2/Deprecated

Summary:	Perl module for deprecated gtk+-2.x widgets
Name:		perl-%{module}
Version:	0.05
Release:	11
License: 	GPL or Artistic
Group:		Development/GNOME and GTK+
URL:		http://gtk2-perl.sf.net/
Source:		http://asofyet.org/muppet/software/gtk2-perl/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel	
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(Gtk2)
BuildRequires:	glitz-devel

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

%files
%{_mandir}/*/*
%{perl_vendorarch}/%{fmodule}
%{perl_vendorarch}/%{fmodule}.pm
%{perl_vendorarch}/auto/%{fmodule}
%{perl_vendorarch}/Gtk2/*.pod



%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.05-10
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.05-9mdv2011.0
+ Revision: 430461
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-8mdv2009.0
+ Revision: 257135
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.05-6mdv2008.1
+ Revision: 152103
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.05-5mdv2008.0
+ Revision: 43105
- rebuild


* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-4mdk
- buildrequires fix

* Wed Dec 15 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-3mdk
- rebuild for new perl

* Fri Aug 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-2mdk
- rebuild for perl-5.8.5

* Mon Apr 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-1mdk
- new release

* Thu Apr 01 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.03-1mdk
- new release

* Mon Jan 12 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-1mdk
- new release
- remove patch 0 (merged upstream)

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-1mdk
- initial release

