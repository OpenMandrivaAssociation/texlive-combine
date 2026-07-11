%global tl_name combine
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7a
Release:	%{tl_revision}.1
Summary:	Bundle individual documents into a single document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/combine
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The combine class lets you bundle individual documents into a single
document, such as when preparing a conference proceedings. The auxiliary
combinet package puts the titles and authors from \maketitle commands
into the main document's Table of Contents. The package cooperates with
the abstract and titling packages.

