%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-husky-base
Version:        0.4.2
Release:        1%{?dist}
Summary:        ROS husky_base package

License:        BSD
URL:            http://ros.org/wiki/husky_base
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-controller-manager
Requires:       ros-melodic-diagnostic-aggregator
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-diff-drive-controller
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-hardware-interface
Requires:       ros-melodic-husky-control
Requires:       ros-melodic-husky-description
Requires:       ros-melodic-husky-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-topic-tools
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-controller-manager
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-hardware-interface
BuildRequires:  ros-melodic-husky-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslaunch
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-sensor-msgs

%description
Clearpath Husky robot driver

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Wed Dec 11 2019 Paul Bovbel <paul@bovbel.com> - 0.4.2-1
- Autogenerated by Bloom

* Mon Sep 30 2019 Paul Bovbel <paul@bovbel.com> - 0.4.1-1
- Autogenerated by Bloom

* Mon Aug 05 2019 Paul Bovbel <paul@bovbel.com> - 0.4.0-1
- Autogenerated by Bloom

