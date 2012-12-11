Summary:	Patches utilities 
Name:		patchutils
Version:	0.3.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Text tools
URL:		http://cyberelk.net/tim/software/patchutils/
Source0:	http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
Patch0:		patchutils-0.3.1-format_not_a_string_literal_and_no_format_arguments.patch
Requires:	patch
Requires:	diffutils
Provides:	interdiff
Obsoletes:	interdiff < 0.3.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Patchutils contains interdiff and filterdiff.

You can use interdiff to create an incremental patch between two patches
that are against a common source tree.

Filterdiff is for extracting or excluding patches from a patch set based
on modified files matching shell wildcards.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%check
make tests

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS ChangeLog TODO COPYING
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Tue Mar 01 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.3.2-1mdv2011.0
+ Revision: 641129
- update to 0.3.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-2mdv2010.0
+ Revision: 440497
- rebuild

* Sun Jan 25 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 333527
- Patch0: fix build with -Werror=format-security flag
- update to new version 0.3.1
- spec file clean

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 241337
- new release

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.31-4mdv2009.0
+ Revision: 241136
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.2.31-2mdv2008.0
+ Revision: 43123
- use %%mkrel
- Import patchutils



* Thu Jun 16 2005 Lenny Cartier <lenny@mandriva.com> 0.2.31-1mdk
- 0.2.31

* Fri Jul 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2.30-1mdk
- 0.2.30

* Tue Apr 06 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.29-1mdk
- new release

* Tue Jan 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2.26-1mdk
- 0.2.26

* Wed Dec 17 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.25-1mdk
- new release

* Sun Jul 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2.24-1mdk
- 0.2.24

* Fri Jun 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2.23-1mdk
- 0.2.23

* Fri Apr 04 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.22-1mdk
- new release

* Mon Feb 03 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.20-1mdk
- new release

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.18-1mdk
- new release

* Mon Oct 14 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.17-1mdk
- new release

* Fri Aug 16 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.16-1mdk
- new release:
	o a new option (--annotate) was added to filterdiff
	o interdiff can now strip context lines from patches

* Wed Jul 10 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.15-1mdk
- 0.2.15

* Tue May 21 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.14-1mdk
- new release

* Fri May 10 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.13-1mdk
- 0.2.13

* Sat Apr 20 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.12-1mdk
- new release:
	- new interdiff option (--debug)
	- describe new usages of filterdiff
	- stricter checking in tests
	- fix offset in interdiff

* Wed Apr 17 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.12-0.1pre1mdk
- new release:
   - more tests
   - -q (quiet) option
   - document basic usage
   - interdiff remove temp files on evasive action (typically when patches're
     too different)
   - Handle GNU diff's output format, which differs slightly from the one
     described in SuSV2.
   - default number of lines of context is 3, not 2.
- remove useless prefix
- run tests

* Fri Apr 12 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.11-1mdk
- new release
- add editdiff(1) manpage

* Mon Mar 04 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.10-1mdk
- update

* Mon Feb 25 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.9-1mdk
- new release (bug fix in cvs diff handling)

* Thu Jan 31 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.8-1mdk
- new release

* Sun Jan 20 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.7-2mdk
- Requires: patch diffutils

* Wed Dec 19 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.7-1mdk
- new release

* Mon Dec 03 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.5-1mdk
- new release

* Thu Nov 29 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.4-2mdk
- fix %%url (chmouel)

* Wed Nov 28 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.4-1mdk
- new release

* Thu Nov 22 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.3-1mdk
- new release

* Tue Nov 20 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.2-1mdk
- new release

* Tue Nov 13 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.0-1mdk
- new release

* Tue Oct 23 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.5-1mdk
- new release

* Wed Oct 17 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.4-1mdk
- new release

* Tue Oct 16 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.3-1mdk
- initial release
- obsoletes interdiff
- macroize
- more docs
