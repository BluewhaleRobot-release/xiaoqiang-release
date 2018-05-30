Name:           ros-kinetic-xiaoqiang-server
Version:        0.0.5
Release:        0%{?dist}
Summary:        ROS xiaoqiang_server package

Group:          Development/Libraries
License:        MIT
URL:            http://www.bwbot.org/content/xiaoqiang
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-xiaoqiang-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-xiaoqiang-msgs

%description
xiaoqiang remote control server

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
* Wed May 30 2018 Randoms <randoms@bwbot.org> - 0.0.5-0
- Autogenerated by Bloom

