%define name radeon-rlc-firmware
%define version 1
%define release %mkrel 5

Summary: ATI R600/R700/Evergreen/Fusion RLC Firmware
Name:	 %{name}
Version: %{version}
Release: %{release}
# extracted from git://git.kernel.org/pub/scm/linux/kernel/git/dwmw2/linux-firmware.git
Source0: %{name}-%{version}.tar.xz
License: Proprietary
Group:	 System/Kernel and hardware
Url:	 http://ati.amd.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This is Ati Radeon R600/R700/Evergreen (HD5xxx)/Fusion RLC firmware needed
for IRQ handling. It's needed for R600/R700/Evergreen/Fusion KMS support
beginning with 2.6.33 series kernels.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware/radeon
install -m644 *.bin %{buildroot}/lib/firmware/radeon/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.*
/lib/firmware/radeon/*.bin
