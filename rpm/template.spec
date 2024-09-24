%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-rcl-yaml-param-parser
Version:        9.2.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rcl_yaml_param_parser package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       libyaml-devel
Requires:       ros-jazzy-libyaml-vendor
Requires:       ros-jazzy-rcutils
Requires:       ros-jazzy-rmw
Requires:       ros-jazzy-ros-workspace
BuildRequires:  libyaml-devel
BuildRequires:  ros-jazzy-ament-cmake-gen-version-h
BuildRequires:  ros-jazzy-ament-cmake-ros
BuildRequires:  ros-jazzy-libyaml-vendor
BuildRequires:  ros-jazzy-rcutils
BuildRequires:  ros-jazzy-rmw
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gtest
BuildRequires:  ros-jazzy-ament-lint-auto
BuildRequires:  ros-jazzy-ament-lint-common
BuildRequires:  ros-jazzy-mimick-vendor
BuildRequires:  ros-jazzy-osrf-testing-tools-cpp
BuildRequires:  ros-jazzy-performance-test-fixture
%endif

%description
Parse a YAML parameter file and populate the C data structure.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Tue Sep 24 2024 Audrow Nash <audrow@openrobotics.org> - 9.2.4-1
- Autogenerated by Bloom

* Thu Jun 13 2024 Audrow Nash <audrow@openrobotics.org> - 9.2.3-2
- Autogenerated by Bloom

* Mon May 13 2024 Audrow Nash <audrow@openrobotics.org> - 9.2.3-1
- Autogenerated by Bloom

* Wed Apr 24 2024 Audrow Nash <audrow@openrobotics.org> - 9.2.2-1
- Autogenerated by Bloom

* Fri Apr 19 2024 Audrow Nash <audrow@openrobotics.org> - 9.2.1-2
- Autogenerated by Bloom

* Tue Apr 16 2024 Audrow Nash <audrow@openrobotics.org> - 9.2.1-1
- Autogenerated by Bloom

* Thu Mar 28 2024 Audrow Nash <audrow@openrobotics.org> - 9.2.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Audrow Nash <audrow@openrobotics.org> - 9.1.0-2
- Autogenerated by Bloom

