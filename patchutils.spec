Summary:	Patches utilities 
Name:		patchutils
Version:	0.3.2
Release:	3
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
%makeinstall_std

%files
%doc BUGS ChangeLog TODO COPYING
%{_bindir}/*
%{_mandir}/man1/*
