%define		module	pisa
Summary:	HTML/XML/CSS to PDF converter using the reportlab toolkit
Name:		python-%{module}
Version:	3.0.10
Release:	1
License:	QPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/spirito-pisa/%{module}-%{version}.tar.gz
# Source0-md5:	4c29768070f3a0f3a2f86a35f9ab22d7
URL:		http://pisa.spirito.de/index.html
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-html5lib
%pyrequires_eq	python
Requires:	python-html5lib
Requires:	python-PIL
Requires:	python-ReportLab >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML/XML/CSS to PDF converter using the reportlab toolkit

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

%py_postclean $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt README.txt
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{py_sitescriptdir}/sx
