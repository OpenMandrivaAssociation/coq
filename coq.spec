%define	debug_package	%nil
Name:           coq
Version:        8.4
Release:        3
Summary:        The Coq Proof Assistant
Group:          Sciences/Computer science
License:        LGPLv2
URL:            https://coq.inria.fr
Source0:        http://coq.inria.fr/distrib/V%{version}/files/%{name}-%{version}.tar.gz
Source1:        http://coq.inria.fr/distrib/V8.4/files/Tutorial.pdf
Source2:        http://coq.inria.fr/distrib/V8.4/files/Reference-Manual.pdf
# Patch0 for compatibility with lablgtk 2.16 (from Gentoo)
Patch0:         coq-8.4-lablgtk-2.16-compat.patch
BuildRequires:	ocaml
BuildRequires:	camlp5
BuildRequires:	camlp4
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	ncurses-devel
BuildRequires:	hevea


%description
Coq is a proof assistant which: 
  - allows to handle calculus assertions, 
  - check mechanically proofs of these assertions, 
  - helps to find formal proofs, 
  - extracts a certified program from the constructive proof
    of its formal specification, 


%package ide
Summary:        The Coq Integrated Development Interface
Group:          Sciences/Computer science
Requires:       %{name} = %{version}

%description ide
The Coq Integrated Development Interface is a graphical interface for the 
Coq proof assistant 


%package doc
Summary:        Documentation for %{name}
Group:          Sciences/Computer science
License:        Open Publication License
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation for %{name}.

%prep
%setup -q
%patch0 -p 1

cp %{SOURCE1} \
   %{SOURCE2} .

%build
./configure \
        -mandir %{_mandir} \
        -bindir %{_bindir} \
        -libdir %{_libdir}/coq \
        -emacslib %{_datadir}/emacs/site-lisp \
        -coqdocdir %{_datadir}/texmf/tex/latex/misc \
        -configdir %{_sysconfdir}/xdg/coq \
        -docdir %{_datadir}/doc/%{name} \
        -datadir %{_datadir}/pixmaps \
        -browser "xdg-open %s" \
        -usecamlp4 \
        -opt

make world


%install
rm -rf %{buildroot}
make COQINSTALLPREFIX=%{buildroot} install-coq
make COQINSTALLPREFIX=%{buildroot} install-coqide
export EXCLUDE_FROM_STRIP=%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CoqIDE
Comment=Coq integrated developpment environment
Exec=%{_bindir}/coqide
Icon=coq
Type=Application
Categories=Education;Science;Math;
EOF


%files
%doc CHANGES COPYRIGHT README CREDITS INSTALL LICENSE
%{_bindir}/*
%{_libdir}/coq
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/*
%{_datadir}/texmf/tex/latex/misc/*
%{_datadir}/pixmaps/coq.png
%exclude %{_bindir}/coqide*
%exclude %{_libdir}/coq/ide

%files ide
%doc INSTALL.ide
%{_sysconfdir}/xdg/coq/coqide-gtk2rc
%{_datadir}/applications/%{name}.desktop
%{_bindir}/coqide*
%{_libdir}/coq/ide

%files doc
%doc Tutorial.pdf
%doc Reference-Manual.pdf
