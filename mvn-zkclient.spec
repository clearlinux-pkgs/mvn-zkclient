#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-zkclient
Version  : 0.10
Release  : 2
URL      : https://github.com/sgroschupf/zkclient/archive/0.10.tar.gz
Source0  : https://github.com/sgroschupf/zkclient/archive/0.10.tar.gz
Source1  : https://repo1.maven.org/maven2/com/101tec/zkclient/0.10/zkclient-0.10.jar
Source2  : https://repo1.maven.org/maven2/com/101tec/zkclient/0.10/zkclient-0.10.pom
Source3  : https://repo1.maven.org/maven2/com/101tec/zkclient/0.3/zkclient-0.3.jar
Source4  : https://repo1.maven.org/maven2/com/101tec/zkclient/0.3/zkclient-0.3.pom
Source5  : https://repo1.maven.org/maven2/com/101tec/zkclient/0.7/zkclient-0.7.jar
Source6  : https://repo1.maven.org/maven2/com/101tec/zkclient/0.7/zkclient-0.7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-zkclient-data = %{version}-%{release}
Requires: mvn-zkclient-license = %{version}-%{release}

%description
ZkClient: a zookeeper client, that makes life a little easier.
=====
+ Website: 			https://github.com/sgroschupf/zkclient
+ Apache 2.0 License

%package data
Summary: data components for the mvn-zkclient package.
Group: Data

%description data
data components for the mvn-zkclient package.


%package license
Summary: license components for the mvn-zkclient package.
Group: Default

%description license
license components for the mvn-zkclient package.


%prep
%setup -q -n zkclient-0.10

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-zkclient
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-zkclient/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.10/zkclient-0.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.10/zkclient-0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.3/zkclient-0.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.3/zkclient-0.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.7
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.7/zkclient-0.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.7
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/101tec/zkclient/0.7/zkclient-0.7.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/101tec/zkclient/0.10/zkclient-0.10.jar
/usr/share/java/.m2/repository/com/101tec/zkclient/0.10/zkclient-0.10.pom
/usr/share/java/.m2/repository/com/101tec/zkclient/0.3/zkclient-0.3.jar
/usr/share/java/.m2/repository/com/101tec/zkclient/0.3/zkclient-0.3.pom
/usr/share/java/.m2/repository/com/101tec/zkclient/0.7/zkclient-0.7.jar
/usr/share/java/.m2/repository/com/101tec/zkclient/0.7/zkclient-0.7.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-zkclient/LICENSE
