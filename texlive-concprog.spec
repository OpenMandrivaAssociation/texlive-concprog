%global tl_name concprog
%global tl_revision 18791

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Concert programmes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/concprog
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concprog.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concprog.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A class which provides the necessary macros to prepare a (classical)
concert programme; a sample is provided.

