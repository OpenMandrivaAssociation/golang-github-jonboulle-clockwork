# http://github.com/jonboulle/clockwork

%global goipath         github.com/jonboulle/clockwork
%global commit          2eee05ed794112d45db504eb05aa693efd2b8b09


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.16%{?dist}
Summary:        A fake clock for golang
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# /usr/bin/ld: cannot find /usr/lib64/libpthread_nonshared.a
#%%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.git2eee05e
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.20160615git2eee05e
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git2eee05e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git2eee05e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git2eee05e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git2eee05e
- Bump to upstream 2eee05ed794112d45db504eb05aa693efd2b8b09
  related: #1250489

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitfad208d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.gitfad208d
- Bump to upstream fad208dd89dbc316a149043e332a192477f0e2a2
  related: #1250489

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git3f831b6
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git3f831b6
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git3f831b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git3f831b6
- Update to spec-2.1
  related: #1250489

* Thu Aug 06 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.git3f831b6
- Update spec file to spec-2.0
  resolves: #1250489

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git3f831b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 18 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.git3f831b6
- First package for Fedora
  resolves: #1175771

