Summary:	Patches utilities 
Name:		patchutils
Version:	0.4.2
Release:	1
License:	GPLv2+
Group:		Text tools
URL:		http://cyberelk.net/tim/software/patchutils/
Source0:	http://cyberelk.net/tim/data/patchutils/stable/%{name}-%{version}.tar.xz
Requires:	patch
Requires:	diffutils
Provides:	interdiff
Obsoletes:	interdiff < 0.3.1
BuildRequires:	pkgconfig(libpcre2-posix)
BuildRequires:	xmlto

%description
Patchutils contains interdiff and filterdiff.

You can use interdiff to create an incremental patch between two patches
that are against a common source tree.

Filterdiff is for extracting or excluding patches from a patch set based
on modified files matching shell wildcards.

%prep
%autosetup -p1
%configure

%build
%make_build

%check
make tests

%install
%make_install

%files
%doc BUGS ChangeLog TODO COPYING
%{_bindir}/*
%{_mandir}/man1/*
