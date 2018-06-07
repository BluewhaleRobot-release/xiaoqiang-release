Name:           ros-kinetic-xiaoqiang-freenect-camera
Version:        0.0.9
Release:        0%{?dist}
Summary:        ROS xiaoqiang_freenect_camera package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/xiaoqiang_freenect_camera
Source0:        %{name}-%{version}.tar.gz

Requires:       log4cxx-devel
Requires:       ros-kinetic-camera-info-manager
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-libfreenect
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  log4cxx-devel
BuildRequires:  ros-kinetic-camera-info-manager
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-libfreenect
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs

%description
A libfreenect-based ROS driver for the Microsoft Kinect. This is a port of the
OpenNI driver that uses libfreenect instead, because on some systems with some
devices it works better. Modified version of xiaoqiang_freenect_stack, add tilt
angle control support

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Jun 07 2018 Randoms <randoms@bwbot.org> - 0.0.9-0
- Autogenerated by Bloom

* Fri Jun 01 2018 Randoms <randoms@bwbot.org> - 0.0.7-0
- Autogenerated by Bloom

* Thu May 31 2018 Randoms <randoms@bwbot.org> - 0.0.6-0
- Autogenerated by Bloom

* Wed May 30 2018 Randoms <randoms@bwbot.org> - 0.0.5-0
- Autogenerated by Bloom

