%global             source_name floorp
%global             application_name floorp
%global             full_name floorp-web-brawser
%global             internal_name floorp-ablaze

Name:               floorp
Version:            v11.3.3
Release:            2%{?dist}
Summary:            Floorp Web browser

License:            MPLv1.1 or GPLv2+ or LGPLv2+
URL:                https://github.com/Floorp-Projects/Floorp
Source0:            https://download-installer.cdn.mozilla.net/pub/devedition/releases/%{version}/linux-x86_64/en-US/firefox-%{version}.tar.bz2
Source0:            https://github.com/Floorp-Projects/Floorp/releases/download/%{version}/floorp-%{version}.linux-x86_64.tar.bz2
Source1:            %{internal_name}.desktop
Source2:            policies.json
Source3:            %{internal_name}

ExclusiveArch:      x86_64

Requires(post):     gtk-update-icon-cache

%description
This is a release of the Floorp web browser. Floorp is a fork of Firefox ESR
with additional features aimed to make the overall Firefox Browser experince
better than vanilla Firefox.

Bugs related to Floorp should be reported directly to the Floorp GitHub repo: 
<https://https://github.com/Floorp-Projects/Floorp/issues/>

Bugs related to this package should be reported at this GitHub project:
<https://github.com/LovecraftianGodsKiller/floorp/issues/>

%prep
%setup -q -n %{source_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/%{application_name},%{_bindir},%{_datadir}/applications,%{_datadir}/icons/hicolor/128x128/apps,%{_datadir}/icons/hicolor/64x64/apps,%{_datadir}/icons/hicolor/48x48/apps,%{_datadir}/icons/hicolor/32x32/apps,%{_datadir}/icons/hicolor/16x16/apps}

%__cp -r * %{buildroot}/opt/%{application_name}

%__install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

%__install -D -m 0444 %{SOURCE2} -t %{buildroot}/opt/%{application_name}/distribution

%__install -D -m 0755 %{SOURCE3} -t %{buildroot}%{_bindir}

%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png

%post
gtk-update-icon-cache -f -t %{_datadir}/icons/hicolor

%files
%{_datadir}/applications/%{internal_name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png
%{_bindir}/%{internal_name}
/opt/%{application_name}

%changelog
* Tue Sep 12 2023 Namelesswonder <Namelesswonder@users.noreply.github.com> - 118.0b7-2
- firefox-developer-edition.spec: Trim changelog to resolve date warnings and bump release
