%define beta 0

%if %beta
%define pre pre1
%endif

Summary: Patches utilities 
Name:    patchutils
Version: 0.3.0
%if %beta
Release: %mkrel 0.1%{pre}
%else
Release: %mkrel 1
%endif
%if %beta
Source0: %name-%version%pre.tar.bz2
%else
Source0: %name-%version.tar.bz2
Source1: %name-%version.tar.bz2.sig
%endif
Patch: patchutils-0.2.11-editdiff-man.diff.bz2
URL: http://cyberelk.net/tim/patchutils/
License: GPL
Group: Text tools
BuildRoot: %_tmppath/%name-buildroot
Provides: interdiff
Obsoletes: interdiff
Requires: patch diffutils

%description
Patchutils contains interdiff and filterdiff.

You can use interdiff to create an incremental patch between two patches
that are against a common source tree.

Filterdiff is for extracting or excluding patches from a patch set based
on modified files matching shell wildcards.

%prep
%if %beta
%setup -q -n %name-%version%pre
%else
%setup -q
%endif
%patch0 -p1 -b .editdiff_addman

%build
%configure
%make
make tests

%install
%makeinstall
install -m 644 editdiff.1 $RPM_BUILD_ROOT%_mandir/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS ChangeLog TODO COPYING
%_bindir/*
%_mandir/man1/*
