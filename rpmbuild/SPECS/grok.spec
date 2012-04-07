%define _sharedir /usr/share/grok

Summary: A powerful pattern matching system for parsing and processing text
Name: grok
Version: 1.20110708.1
Release: 1
Group: System Environment/Utilities
License: BSD
Source0: http://semicomplete.googlecode.com/files/%{name}-%{version}.tar.gz
URL: http://www.semicomplete.com/projects/grok/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: libevent
Requires: pcre >= 7.6
Requires: tokyocabinet >= 1.4.9
BuildRequires: libevent-devel gperf tokyocabinet-devel pcre-devel

# no longer needed -- modern jls-grok gem uses libffi
Obsoletes: grok-ruby

%description
A powerful pattern matching system for parsing and processing text data such
as log files.

%package devel
Group: Development Tools
Summary: Grok development headers

%description devel
Headers required for grok development.

%prep
%setup -q

%build
make

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_includedir}
%{__mkdir_p} %{buildroot}%{_sharedir}/patterns
install -c grok %{buildroot}/%{_bindir}
install -c libgrok.so %{buildroot}/%{_libdir}
install -c patterns/base %{buildroot}%{_sharedir}/patterns/base
for header in grok.h grok_pattern.h grok_capture.h grok_capture_xdr.h grok_match.h grok_logging.h grok_discover.h grok_version.h; do
 install -c $header %{buildroot}/%{_includedir}
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/grok
%{_libdir}/libgrok.so
%dir %{_sharedir}
%dir %{_sharedir}/patterns
%{_sharedir}/patterns/base

%files devel
%{_includedir}

%post
/sbin/ldconfig

%changelog
* Fri Apr  6 2012 David Castro <arimus@gmail.com> 1.20110708.1
* Tue Mar  8 2011 Jordan Sissel <jls@semicomplete.com> 1.20110308.1-1
* Mon Oct 19 2009 Pete Fritchman <petef@databits.net> 20090928-1
- Initial packaging.
