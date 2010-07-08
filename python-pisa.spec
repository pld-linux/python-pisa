%define		module	pisa
Summary:	HTML/XML/CSS to PDF converter using the ReportLab toolkit
Summary(pl.UTF-8):	Konwerter formatów HTML/XML/CSS do PDF korzystający z narzędzi ReportLab
Name:		python-%{module}
Version:	3.0.33
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pisa/%{module}-%{version}.tar.gz
# Source0-md5:	e2040b12211303d065bc4ae2470d2700
URL:		http://www.xhtml2pdf.com/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-html5lib
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
%pyrequires_eq	python
Requires:	python-html5lib
Requires:	python-PIL
Requires:	python-ReportLab >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML/XML/CSS to PDF converter using the ReportLab toolkit.

%description -l pl.UTF-8
Konwerter formatów HTML/XML/CSS do PDF korzystający z narzędzi
ReportLab.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

install -d $RPM_BUILD_ROOT%{_bindir}
install pisa.py $RPM_BUILD_ROOT%{_bindir}
sed -i 's@/usr/local/bin/python.*$@/usr/bin/python@' $RPM_BUILD_ROOT%{_bindir}/pisa.py

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
