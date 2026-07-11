%global tl_name logreq
%global tl_revision 53003

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Support for automation of the LaTeX workflow
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/logreq
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logreq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logreq.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(etoolbox)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package helps to automate a typical LaTeX workflow that involves
running LaTeX several times, running tools such as BibTeX or makeindex,
and so on. It will log requests like "please rerun LaTeX" or "please run
BibTeX on file X" to an external XML file which lists all open tasks in
a machine-readable format. Compiler scripts and integrated LaTeX editing
environments may parse this file to determine the next steps in the
workflow in a way that is more efficient than parsing the main log file.
In sum, the package will do two things: enable package authors to use
LaTeX commands to issue requests, collect all requests from all packages
and write them to an external XML file at the end of the document.

