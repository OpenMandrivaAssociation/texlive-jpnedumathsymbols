Name:		texlive-jpnedumathsymbols
Version:	72959
Release:	1
Summary:	Mathematical equation representation in Japanese education
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jpnedumathsymbols
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jpnedumathsymbols.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jpnedumathsymbols.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Mathematical equation representation in Japanese education
differs somewhat from the standard LaTeX writing style. This
package introduces mathematical equation representation in
Japanese education.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jpnedumathsymbols
%doc %{_texmfdistdir}/doc/latex/jpnedumathsymbols

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
