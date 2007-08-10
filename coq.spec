%define name	coq
%define version	8.0pl3
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	The Coq Proof Assistant
Group:		Sciences/Computer science
License:	LGPL
URL:		http://coq.inria.fr
Source:		ftp://ftp.inria.fr/INRIA/coq/V%{version}/%{name}-%{version}.tar.bz2
Patch:		ftp://ftp.inria.fr/INRIA/coq/V8.0pl3/patch-coq-8.0pl3-ocaml-3.09.bz2
BuildRequires:	ocaml >= 3.06
BuildRequires:	camlp4
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	ncurses-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Coq is a proof assistant which: 
  - allows to handle calculus assertions, 
  - check mechanically proofs of these assertions, 
  - helps to find formal proofs, 
  - extracts a certified program from the constructive proof
    of its formal specification, 

%package ide
Summary:	The Coq Integrated Development Interface
Group:		Sciences/Computer science
Requires:	%{name} = %{version}

%description ide
The Coq Integrated Development Interface is a graphical interface for the 
Coq proof assistant 

%prep
%setup -q
%patch -p0

%build
./configure --mandir %{_mandir} \
            --bindir %{_bindir} \
            --libdir %{_libdir}/coq \
            --emacslib %{_datadir}/emacs/site-lisp \
            --coqdocdir %{_datadir}/texmf/tex/latex/misc \
            --reals all \
            --opt
%make world

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
make COQINSTALLPREFIX=%{buildroot} install-coq
make COQINSTALLPREFIX=%{buildroot} install-coqide
export EXCLUDE_FROM_STRIP=%{_bindir}

%files
%defattr(-,root,root)
%doc CHANGES COPYRIGHT README CREDITS INSTALL LICENSE
%{_bindir}/*
%{_libdir}/coq
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/*
%{_datadir}/texmf/tex/latex/misc/*
%exclude %{_bindir}/coqide*
%exclude %{_libdir}/coq/ide

%files ide
%doc INSTALL.ide
%defattr(-,root,root)
%{_bindir}/coqide*
%{_libdir}/coq/ide
