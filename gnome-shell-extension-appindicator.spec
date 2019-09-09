%global uuid    appindicatorsupport@rgcjonas.gmail.com

Name:           gnome-shell-extension-appindicator
Version:        30
Release:        8%{?dist}
Summary:        AppIndicator/KStatusNotifierItem support for GNOME Shell

# No license files
# https://github.com/ubuntu/gnome-shell-extension-appindicator/pull/188
License:        GPLv2
URL:            https://github.com/ubuntu/gnome-shell-extension-appindicator
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix regression for GNOME 3.32 version
Patch0:         0001-Revert-cleanup-Don-t-use-actor-property-on-actors.patch

Requires:       gnome-shell >= 3.14.0
BuildArch:      noarch

%description
This extension integrates Ubuntu AppIndicators and KStatusNotifierItems
(KDE's blessed successor of the systray) into GNOME Shell.

You can use gnome-tweaks (additional package) or run in terminal:

  gnome-shell-extension-tool -e %uuid

%prep
%autosetup

%install
mkdir -p                                    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -axv *.js metadata.json interfaces-xml   %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%doc README.md AUTHORS.md
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
* Mon Sep 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 30-8
- Fix regression for GNOME 3.32 version

* Sun Sep 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 30-7
- Initial package

