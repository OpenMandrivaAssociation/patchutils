Summary:	Patches utilities 
Name:		patchutils
Version:	0.3.1
Release:	%mkrel 1
License:	GPL
Group:		Text tools
URL:		http://cyberelk.net/tim/software/patchutils/
Source0:	http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
Provides:	interdiff
Obsoletes:	interdiff < 0.3.1
Requires:	patch
Requires:	diffutils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Patchutils contains interdiff and filterdiff.

You can use interdiff to create an incremental patch between two patches
that are against a common source tree.

Filterdiff is for extracting or excluding patches from a patch set based
on modified files matching shell wildcards.

%prep
%setup -q

%build
%configure2_5x
%make

%check
make tests

%install
rm -rf %{buildroot}
%makeinstall_std
#install -m 644 editdiff.1 $RPM_BUILD_ROOT%_mandir/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS ChangeLog TODO COPYING
%{_bindir}/*
%{_mandir}/man1/*
