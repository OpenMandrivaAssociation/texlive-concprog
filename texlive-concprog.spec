Name:		texlive-concprog
Version:	18791
Release:	2
Summary:	Concert programmes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/concprog
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concprog.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concprog.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
