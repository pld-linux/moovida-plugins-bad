%define		module_name	elisa
Summary:	"Bad" plugins for Moovida
Summary(pl.UTF-8):	"Złe" wtyczki dla Moovidy
Name:		moovida-plugins-bad
Version:	1.0.7
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://www.moovida.com/media/public/%{name}-%{version}.tar.gz
# Source0-md5:	7a63e77549468b45ce9337f5c7acd9ac
URL:		http://www.moovida.com/
BuildRequires:	moovida = %{version}
Requires:	python-simplejson
Provides:	moovida-plugins = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Bad" plugins for Moovida

%description -l pl.UTF-8
"Złe" wtyczki dla Moovidy

%prep
%setup -q -n elisa-plugins-bad-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

#py_postclean

#install moovida/plugins/amp/slave.py $RPM_BUILD_ROOT%{py_sitescriptdir}/moovida/plugins/amp/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/%{module_name}/plugins/*
