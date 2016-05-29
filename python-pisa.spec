%define		module	pisa
Summary:	HTML/XML/CSS to PDF converter using the ReportLab toolkit
Summary(pl.UTF-8):	Konwerter formatów HTML/XML/CSS do PDF korzystający z narzędzi ReportLab
Name:		python-%{module}
Version:	3.0.33
Release:	5
License:	Apache v2.0
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pisa/%{module}-%{version}.tar.gz
# Source0-md5:	e2040b12211303d065bc4ae2470d2700
Patch0:		reportlab3.patch
URL:		http://www.xhtml2pdf.com/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-html5lib
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	sed >= 4.0
Requires:	python
Requires:	python-PIL
Requires:	python-ReportLab >= 2.2
Requires:	python-html5lib
Requires:	python-pyPdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML/XML/CSS to PDF converter using the ReportLab toolkit.

%description -l pl.UTF-8
Konwerter formatów HTML/XML/CSS do PDF korzystający z narzędzi
ReportLab.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

install -d $RPM_BUILD_ROOT%{_bindir}
cp -p pisa.py $RPM_BUILD_ROOT%{_bindir}
sed -i 's@%{_prefix}/local/bin/python.*$@%{_bindir}/python@' $RPM_BUILD_ROOT%{_bindir}/pisa.py

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt README.txt
%attr(755,root,root) %{_bindir}/pisa
%attr(755,root,root) %{_bindir}/pisa.py
%attr(755,root,root) %{_bindir}/xhtml2pdf
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{py_sitescriptdir}/ho
%{py_sitescriptdir}/sx
