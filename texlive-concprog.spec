# revision 18791
# category Package
# catalog-ctan /macros/latex/contrib/concprog
# catalog-date 2007-01-01 11:39:06 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-concprog
Version:	20070101
Release:	6
Summary:	Concert programmes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/concprog
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concprog.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concprog.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class which provides the necessary macros to prepare a
(classical) concert programme; a sample is provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/concprog/ConcProg.cls
%doc %{_texmfdistdir}/doc/latex/concprog/program.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070101-2
+ Revision: 750421
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070101-1
+ Revision: 718117
- texlive-concprog
- texlive-concprog
- texlive-concprog
- texlive-concprog

