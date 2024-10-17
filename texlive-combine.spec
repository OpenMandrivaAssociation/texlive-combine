Name:		texlive-combine
Version:	19361
Release:	2
Summary:	Bundle individual documents into a single document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/combine
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The combine class lets you bundle individual documents into a
single document, such as when preparing a conference
proceedings. The auxiliary combinet package puts the titles and
authors from \maketitle commands into the main document's Table
of Contents. The package cooperates with the abstract and
titling packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/combine/combcite.sty
%{_texmfdistdir}/tex/latex/combine/combine.cls
%{_texmfdistdir}/tex/latex/combine/combinet.sty
%{_texmfdistdir}/tex/latex/combine/combnat.sty
%doc %{_texmfdistdir}/doc/latex/combine/README
%doc %{_texmfdistdir}/doc/latex/combine/combine.pdf
#- source
%doc %{_texmfdistdir}/source/latex/combine/combine.dtx
%doc %{_texmfdistdir}/source/latex/combine/combine.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
