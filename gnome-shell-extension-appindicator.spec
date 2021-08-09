%global uuid appindicatorsupport@rgcjonas.gmail.com

Name: gnome-shell-extension-appindicator
Version: 40
Release: 1%{?dist}
Summary: AppIndicator/KStatusNotifierItem support for GNOME Shell
BuildArch: noarch

License: GPLv2
URL: https://github.com/ubuntu/gnome-shell-extension-appindicator
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make glib2 gettext

Requires: gnome-shell >= 3.14.0
Requires: libappindicator-gtk3

# gnome-shell-extension-appindicator version >= 40 now also includes
# support for legacy X11 tray icons and the topicons(-plus) extensions
# are no longer maintained upstream
Provides:  gnome-shell-extension-topicons-plus = %{version}-%{release}
Obsoletes: gnome-shell-extension-topicons-plus <= 27-9

%description
This extension integrates Ubuntu AppIndicators and KStatusNotifierItems (KDE's
blessed successor of the systray) into GNOME Shell.

You can use gnome-tweaks (additional package) or run in terminal:

  gnome-extensions enable %uuid


%prep
%autosetup -p1


%build
%make_build


%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -axv --parents *.js metadata.json interfaces-xml locale/*/LC_MESSAGES/*.mo \
                  schemas/*.xml schemas/gschemas.compiled                     \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/


%files
%license LICENSE
%doc README.md AUTHORS.md
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Mon Aug  9 2021 Hans de Goede <hdegoede@redhat.com> - 40-1
- Update to latest upstream release: v40 (rhbz#1971135)
- This includes legacy X11 tray-icon support, make
  gnome-shell-extension-appindicator obsolete and provide
  gnome-shell-extension-topicons-plus

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 37-1
- build(update): 37

* Tue Apr 27 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 35-2
- build(add dep): libappindicator-gtk3

* Fri Mar 19 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 35-1
- build(update): 35

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 34-1
- Update to 34

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 33-1
- Update to 33

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 30-7
- Initial package
