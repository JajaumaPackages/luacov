%define debug_package %{nil}

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           luacov
Version:        0.11.0
Release:        1%{?dist}
Summary:        Coverage analysis tool for Lua scripts

License:        MIT
URL:            http://keplerproject.github.io/luacov/
Source0:        https://github.com/keplerproject/luacov/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif

%description
LuaCov is a simple coverage analyzer for Lua scripts. When a Lua script is run
with the luacov module loaded, it generates a stats file with the number of
executions of each line of the script and its loaded modules. The luacov
command-line script then processes this file generating a report file which
allows one to visualize which code paths were not traversed, which is useful
for verifying the effectiveness of a test suite.


%prep
%setup -q


%build


%install
install -d %{buildroot}%{luapkgdir}
cp -ar src/luacov src/luacov.lua %{buildroot}%{luapkgdir}
install -p -m755 -D src/bin/luacov %{buildroot}%{_bindir}/luacov


%files
%doc README.md doc
%{_bindir}/luacov
%{luapkgdir}/luacov/
%{luapkgdir}/luacov.lua


%changelog
* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.11.0-1
- Public release
