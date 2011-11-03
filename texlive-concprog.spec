# revision 18791
# category Package
# catalog-ctan /macros/latex/contrib/concprog
# catalog-date 2007-01-01 11:39:06 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-concprog
Version:	20070101
Release:	1
Summary:	Concert programmes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/concprog
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concprog.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concprog.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
A class which provides the necessary macros to prepare a
(classical) concert programme; a sample is provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/concprog/ConcProg.cls
%doc %{_texmfdistdir}/doc/latex/concprog/program.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
