Name:		coq
Version:	8.3pl3
Release:	%mkrel 1
Summary:	The Coq Proof Assistant
Group:		Sciences/Computer science
License:	LGPL
URL:		http://coq.inria.fr
Source:		http://coq.inria.fr/distrib/V%{version}/files/%{name}-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	camlp5
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	ncurses-devel
BuildRequires:	hevea

%description
Coq is a proof assistant which:
  - allows to handle calculus assertions,
  - check mechanically proofs of these assertions,
  - helps to find formal proofs,
  - extracts a certified program from the constructive proof
    of its formal specification.

%package	ide
Summary:	The Coq Integrated Development Interface
Group:		Sciences/Computer science
Requires:	%{name} = %{version}

%description	ide
The Coq Integrated Development Interface is a graphical interface for the
Coq proof assistant.

%prep
%setup -q

%build
./configure -mandir %{_mandir} \
            -bindir %{_bindir} \
            -libdir %{_libdir}/coq \
            -emacslib %{_datadir}/emacs/site-lisp \
            -coqdocdir %{_datadir}/texmf/tex/latex/misc \
            -docdir %{_datadir}/doc/%{name} \
            -browser "xdg-open %s" \
            -opt
make world

%clean
%__rm -rf %{buildroot}

%install
%__rm -rf %{buildroot}
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
