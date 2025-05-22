#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests

%define 	module	stevedore
Summary:	Manage dynamic plugins for Python applications
Summary(pl.UTF-8):	Zarządzanie dynamicznymi wtyczkami dla aplikacji Pythona
Name:		python-%{module}
# keep 1.x here for python2 support
Version:	1.32.0
Release:	4
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/stevedore/
Source0:	https://files.pythonhosted.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
# Source0-md5:	f854d6ed0f6fcaf93a32c755d706ce19
URL:		https://pypi.org/project/stevedore/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-pbr >= 2.0.0
%if %{with tests}
BuildRequires:  python-coverage >= 4.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-stestr >= 2.0.0
BuildRequires:	sphinx-pdg-2 >= 1.7.0
%endif
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.11.0
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	sphinx-pdg-2 >= 1.7.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manage dynamic plugins for Python applications.

%description -l pl.UTF-8
Zarządzanie dynamicznymi wtyczkami dla aplikacji Pythona.

%package apidocs
Summary:	API documentation for Python stevedore module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona stevedore
Group:		Documentation

%description apidocs
API documentation for Python stevedore module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona stevedore.

%prep
%setup -q -n stevedore-%{version}

%build
%py_build %{?with_tests:test}

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/stevedore/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/stevedore/example

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst announce.rst
%{py_sitescriptdir}/stevedore
%{py_sitescriptdir}/stevedore-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_images,_static,install,reference,user,*.html,*.js}
%endif
