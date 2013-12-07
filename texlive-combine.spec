# revision 19361
# category Package
# catalog-ctan /macros/latex/contrib/combine
# catalog-date 2010-07-10 16:18:55 +0200
# catalog-license lppl1.3
# catalog-version 0.7a
Name:		texlive-combine
Version:	0.7a
Release:	4
Summary:	Bundle individual documents into a single document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/combine
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/combine.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7a-2
+ Revision: 750382
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7a-1
+ Revision: 718104
- texlive-combine
- texlive-combine
- texlive-combine
- texlive-combine

