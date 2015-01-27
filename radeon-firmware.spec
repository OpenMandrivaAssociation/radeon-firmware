%define name radeon-firmware
%define version 20110310
%define release 2

Summary: ATI R600/R700/Evergreen/Fusion Firmware
Name:	 %{name}
Version: obsoleted by kernel-firmware
Release: %{release}
# extracted from git://git.kernel.org/pub/scm/linux/kernel/git/dwmw2/linux-firmware.git
# all files in radeon/ dir excluding the files in kernel-firmware
Source0: %{name}-%{version}.tar.xz
License: Proprietary
Group:	 System/Kernel and hardware
Url:	 http://ati.amd.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Obsoletes: radeon-rlc-firmware
Conflicts: kernel-firmware-extra < 20110310-1

%description
This is Ati Radeon R600/R700/Evergreen (HD5xxx)/Fusion firmware needed
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
