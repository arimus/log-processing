%define debug_package %{nil}

Name:           logstash
Version:        1.1.0
Release:        3%{?dist}
Summary:        logstash is a tool for managing events and logs.

Group:          System Environment/Daemons
License:        Apache 2.0
URL:            http://logstash.net
Source0:        %{name}-%{version}.tar.gz
Source1:        etc-rc.d-init.d-logstash
Source2:        etc-logstash-logstash.conf
Source3:        etc-logstash-log4j.properties
Source4:        etc-sysconfig-logstash
Source5:        usr-sbin-logstash
# cheat because ant 1.7 packages cannot be found for RHEL5
Source6:        apache-ant-1.7.1-bin.tar.gz

Patch0:         logstash_amqp09_queuefix.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:	git
BuildRequires:	wget
BuildRequires:	ruby

Requires:       grok
Requires:       java
Requires:       daemonize

Requires:       chkconfig initscripts

# disable jar repackaging
%define __os_install_post %{nil}

%description
logstash is a tool for managing events and logs. You can use it to collect logs, parse them, and store them for later use (like, for searching).

%prep
rm -rf "${RPM_BUILD_ROOT}"
mkdir -p "${RPM_BUILD_ROOT}/usr/share/logstash/"
cp -p %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 .
find . -type f -print0 | xargs -0 --no-run-if-empty -- sed -i -e 's/@@@version@@@/%{version}/g'

%build
# prepare the bundled ant 1.7
tar -zxvf %SOURCE6
export ANT_HOME=`pwd`/apache-ant-1.7.1
export PATH=$ANT_HOME/bin:$PATH
chmod +x $ANT_HOME/bin/ant

# logstash build
tar -zxvf %SOURCE0
cd %{name}-%{version}
patch -p1 < %PATCH0
echo `which ant`
make

%install
install -D -m 644 -t "${RPM_BUILD_ROOT}/usr/share/logstash/" %{name}-%{version}/build/%{name}-%{version}-monolithic.jar
install -D -m 655 etc-rc.d-init.d-logstash          "${RPM_BUILD_ROOT}/etc/rc.d/init.d/logstash"
install -D -m 644 etc-logstash-logstash.conf        "${RPM_BUILD_ROOT}/etc/logstash/logstash.conf"
install -D -m 644 etc-logstash-log4j.properties     "${RPM_BUILD_ROOT}/etc/logstash/log4j.properties"
install -D -m 644 etc-sysconfig-logstash            "${RPM_BUILD_ROOT}/etc/sysconfig/logstash"
install -D -m 755 usr-sbin-logstash                 "${RPM_BUILD_ROOT}/usr/sbin/logstash"
mkdir -p "${RPM_BUILD_ROOT}/var/lib/logstash"
mkdir -p "${RPM_BUILD_ROOT}/var/log/logstash"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/
/var/
/etc/rc.d/init.d/logstash
%config(noreplace) /etc/logstash
%config(noreplace) /etc/sysconfig

%changelog
* Thu Apr 11 2012 David Castro arimus@gmail.com 1.1.0-3
- New init script that isn't busted
- Sysconfig for settings and used by enhanced sbin
- Logging to /var/log/logstash

* Thu Apr 05 2012 David Castro arimus@gmail.com 1.1.0-1
- Initial spec that works for CentOS 5/6 and patches the issue with the
  elasticsearch_river
- sets the default amqp version to 0.9
- updates elasticsearch version to 0.19.2
