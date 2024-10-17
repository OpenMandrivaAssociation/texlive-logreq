Name:		texlive-logreq
Version:	53003
Release:	2
Summary:	Support for automation of the LaTeX workflow
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/logreq
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logreq.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logreq.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package helps to automate a typical LaTeX workflow that
involves running LaTeX several times, running tools such as
BibTeX or makeindex, and so on. It will log requests like
"please rerun LaTeX" or "please run BibTeX on file X" to an
external XML file which lists all open tasks in a machine-
readable format. Compiler scripts and integrated LaTeX editing
environments may parse this file to determine the next steps in
the workflow in a way that is more efficient than parsing the
main log file. In sum, the package will do two things: 1)
enable package authors to use LaTeX commands to issue requests,
2) collect all requests from all packages and write them to an
external XML file at the end of the document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/logreq/logreq.def
%{_texmfdistdir}/tex/latex/logreq/logreq.sty
%doc %{_texmfdistdir}/doc/latex/logreq/README
%doc %{_texmfdistdir}/doc/latex/logreq/examples/01-basic.run.xml
%doc %{_texmfdistdir}/doc/latex/logreq/examples/01-basic.tex
%doc %{_texmfdistdir}/doc/latex/logreq/examples/02-index.run.xml
%doc %{_texmfdistdir}/doc/latex/logreq/examples/02-index.tex
%doc %{_texmfdistdir}/doc/latex/logreq/examples/03-biblatex+bibtex8.run.xml
%doc %{_texmfdistdir}/doc/latex/logreq/examples/03-biblatex+bibtex8.tex
%doc %{_texmfdistdir}/doc/latex/logreq/examples/04-biblatex+bibtex+refsections.run.xml
%doc %{_texmfdistdir}/doc/latex/logreq/examples/04-biblatex+bibtex+refsections.tex
%doc %{_texmfdistdir}/doc/latex/logreq/examples/05-biblatex+biber.run.xml
%doc %{_texmfdistdir}/doc/latex/logreq/examples/05-biblatex+biber.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
