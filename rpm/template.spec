Name:           ros-melodic-husky-navigation
Version:        0.4.1
Release:        1%{?dist}
Summary:        ROS husky_navigation package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/husky_navigation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-amcl
Requires:       ros-melodic-base-local-planner
Requires:       ros-melodic-dwa-local-planner
Requires:       ros-melodic-gmapping
Requires:       ros-melodic-map-server
Requires:       ros-melodic-move-base
Requires:       ros-melodic-navfn
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roslaunch

%description
Autonomous mapping and navigation demos for the Clearpath Husky

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
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

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Sep 30 2019 Paul Bovbel <paul@bovbel.com> - 0.4.1-1
- Autogenerated by Bloom

* Mon Aug 05 2019 Paul Bovbel <paul@bovbel.com> - 0.4.0-1
- Autogenerated by Bloom

