%define _disable_ld_as_needed 1
%define _disable_ld_no_undefined 1
%define	major 0
%define	libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

%define beta_or_rc 1
%define actual_release 1
%define svnrevision 25584

%define with_clucene 1
%define with_ldap 1
%define with_xmlto 1

%define _requires_exceptions pear(

Summary:	Zarafa Outlook Sharing and Open Source Collaboration
Name:		zarafa
Version:	6.40.6
%if %{beta_or_rc}
Release:	%mkrel 0.%{actual_release}.svn%{svnrevision}.0
%else
Release:	%mkrel %{actual_release}
%endif
# Red Hat Legal has been advised by email from Zarafa that no license is
# required in order to use the letter string "zarafa" (combined with other
# words) in the package naming, to refer to the software as "Zarafa" to
# indicate its intended purpose, and to modify packages with bug fixes and
# enhancements.
License:	AGPLv3 with exceptions
Group:		System/Servers
URL:		http://www.zarafa.com/
# http://www.zarafa.com/download-community -> "Zarafa Source Package"
#Source0:	%{name}-%{version}.tar.gz
Source0:	http://download.zarafa.com/community/final/6.40/6.40.6-%{svnrevision}/sourcecode/zcp-%{version}.tar.gz
Source1:	%{name}.ini
Source2:	%{name}.logrotate
Source3:	%{name}-webaccess.conf
Patch0:		zarafa-6.40.0-package.patch
# mandriva patches
Patch100:	zarafa-6.30.10-linkage_fix.diff
Patch101:	zarafa-6.40.5-pthread.patch
Patch103:	zarafa-6.40.5-uuid.patch
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	curl-devel
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	libical-devel >= 0.42
%if %mdkversion >= 201000
BuildRequires:	libuuid-devel
%endif
%if %mdkversion == 200900
BuildRequires:	e2fsprogs-devel
%endif
BuildRequires:	libvmime07-devel
BuildRequires:	libxml2-devel
BuildRequires:	mysql-devel >= 4.1
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	perl-devel
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	swig
BuildRequires:	python-devel
BuildRequires:	boost-devel
%if %{with_clucene}
BuildRequires:	clucene-devel >= 0.9.20
%endif
%if %{with_ldap}
BuildRequires:	openldap-devel
%endif
%if %{with_xmlto}
BuildRequires:	xmlto
%endif
# The normal zarafa package pulls in all of zarafa
Requires:	zarafa-ical >= %{version}-%{release}
Requires:	zarafa-dagent >= %{version}-%{release}
Requires:	zarafa-gateway >= %{version}-%{release}
Requires:	zarafa-monitor >= %{version}-%{release}
Requires:	zarafa-server >= %{version}-%{release}
Requires:	zarafa-spooler >= %{version}-%{release}
Requires:	zarafa-utils >= %{version}-%{release}
Requires:	zarafa-config >= %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Zarafa Outlook Sharing is a Microsoft Exchange replacement. The Open Source
Collaboration provides an integration with your existing Linux mail server,
native mobile phone support by ActiveSync compatibility and a webaccess with
'Look & Feel' similar to Outlook using Ajax. Including an IMAP4 and a POP3
gateway as well as an iCal/CalDAV gateway, Zarafa can combine the usability
with the stability and flexibility of a Linux server.

The proven Zarafa groupware solution is using MAPI objects, provides a MAPI
client library as well as programming interfaces for C++, PHP and Perl. The
other Zarafa related packages need to be installed to gain all the features
and benefits of Zarafa Outlook Sharing and Open Source Collaboration.

%package	client
Summary:	Zarafa Client Library
Group:		System/Servers
Requires:	zarafa-common >= %{version}-%{release}

%description	client
Zarafa client libraries for use with integrated MAPI clients.

%package	common
Summary:	Zarafa common files
Group:		System/Servers

%description	common
Common files and directories required by most Zarafa packages.

%package	dagent
Summary:	Zarafa Delivery Agent
Group:		System/Servers
Requires:	zarafa-client >= %{version}-%{release}
Requires:	zarafa-common >= %{version}-%{release}
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(preun):    /sbin/chkconfig
Requires(postun):   /sbin/service
Provides:	zarafa-dagent = %{version}-%{release}

%description	dagent
The delivery agent delivers e-mails into the Zarafa server.
It can be used to trigger the local mailer or act as the LMTP
server.

%package -n	%{develname}
Summary:	Development files for several Zarafa libraries
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}, pkgconfig
Requires:	zarafa-common = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
The zarafa-devel package includes header files and libraries necessary for
developing programs which use features from the Zarafa Outlook Sharing and
Open Source Collaboration. The proven Zarafa groupware solution is using
MAPI objects, provides a MAPI client library and programming interfaces for
C++, PHP and Perl.

%package	gateway
Summary:	Zarafa Gateway server (POP3/IMAP access)
Group:		System/Servers
Requires:	zarafa-client >= %{version}-%{release}
Requires:	zarafa-common >= %{version}-%{release}
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(preun):    /sbin/chkconfig
Requires(postun):   /sbin/service

%description	gateway
The gateway enables other e-mail clients to connect through
POP3 or IMAP to the Zarafa server to read their e-mail. With
IMAP, it is also possible to view the contents of shared
folders and subfolders. The gateway can be configured to
listen for POP3, POP3S, IMAP and/or IMAPS.

%package	ical
Summary:	The Zarafa iCal/CalDAV gateway
Group:		System/Servers
Requires:	zarafa-client >= %{version}-%{release}
Requires:	zarafa-common >= %{version}-%{release}
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(preun):    /sbin/chkconfig
Requires(postun):   /sbin/service
Provides:	zarafa-caldav = %{version}-%{release}

%description	ical
The iCal/CalDAV gateway enables users to retrieve their
calendar using iCalendar compliant clients. The iCal/CalDAV
gateway can be configured to listen for HTTP and HTTPS
requests.

%package	caldav
Summary:	The Zarafa iCal/CalDAV gateway
Group:		System/Servers
Requires:	zarafa-ical >= %{version}-%{release}

%description	caldav
The iCal/CalDAV gateway enables users to retrieve their
calendar using iCalendar compliant clients. The iCal/CalDAV
gateway can be configured to listen for HTTP and HTTPS
requests.

%package	monitor
Summary:	Zarafa Monitoring service
Group:		System/Servers
Requires:	zarafa-client >= %{version}-%{release}
Requires:	zarafa-common >= %{version}-%{release}
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(preun):    /sbin/chkconfig
Requires(postun):   /sbin/service

%description	monitor
The monitor checks user mailbox sizes. When a quotum is reached
the monitor sends a quota notification email.

%package	server
Summary:	Zarafa Backend Server
Group:		System/Servers
Requires:	zarafa-common >= %{version}-%{release}
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(preun):    /sbin/chkconfig
Requires(postun):   /sbin/service
Provides:	zarafa-config = %{version}-%{release}

%description	server
The Zarafa groupware backend server

%package	spooler
Summary:	Zarafa Spooler Service
Group:		System/Servers
Requires:	zarafa-client >= %{version}-%{release}
Requires:	zarafa-common >= %{version}-%{release}
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/service
Requires(preun):    /sbin/chkconfig
Requires(postun):   /sbin/service

%description	spooler
The spooler sends all pending Zarafa e-mail to the recipients,
from the Outbox of a user/all users.

%package	utils
Summary:	Zarafa Utilities
Group:		System/Servers
Requires:	zarafa-client >= %{version}-%{release}
Requires:	zarafa-common >= %{version}-%{release}

%description	utils
Administration utilities for the Zarafa Groupware environment
including reporting and password management.

%package -n	%{libname}
Summary:	Mapi libraries by Zarafa
Group:		System/Libraries
Requires:	zarafa-client >= %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n %{libname}
MAPI libraries by Zarafa.

%package -n	python-MAPI
Summary:	Python Mapi extension libraries by Zarafa
Group:		Development/Python
Requires:	python

%description -n	python-MAPI
Python MAPI extension libraries by Zarafa.

%package -n	php-mapi
Summary:	A PHP Mapi client by Zarafa
Group:		Development/PHP
# Bug: Without mod_ssl, reloading httpd causes core dump
Requires:	apache-mod_ssl
Requires:	apache-mod_php >= 5.2

%description -n php-mapi
PHP MAPI extension by Zarafa to enable MAPI communication in PHP.

%if %{with_clucene}
%package	indexer
Summary:	The Zarafa Indexing service
Group:		System/Servers
Requires:	zarafa-common >= %{version}-%{release}
Requires:	catdoc
Requires:	xsltproc
Requires:	lynx
Requires:	unzip
Requires:	poppler
Requires:	file
Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/service
Requires(preun):  /sbin/chkconfig
Requires(postun): /sbin/service

%description	indexer
The zarafa-indexer package includes the Zarafa Indexing service for fast
and full-text searching. Using CLucene search engine, this service makes
an index per user of messages and attachments for the Zarafa server. At
search queries, the server will use this index to quickly find messages,
items and even in contents of attached documents.
%endif

%package	webaccess
Summary:	Zarafa Webaccess featuring a 'Look & Feel' similar to Outlook
Group:		Development/PHP
Requires:	apache-mod_php >= 5.2
Requires:	php-mapi >= %{version}-%{release}
%if %mdkversion >= 201010
BuildArch:	noarch
%endif

%description	webaccess
Zarafa Webaccess features the familiar Outlook 'Look & Feel' interface
and you can keep using the features in Outlook that have always allowed
you to work efficiently. View your e-mail, calendar and contacts via a
web browser. And opening your colleagues calendar or sending a meeting
request is only a piece of cake. The Zarafa Webaccess is using the ajax
technology to give a more interactive feeling to the users.

%package	archiver
Summary:	Manages zarafa archives and performs the archive operation
Group:		System/Servers
Requires:	zarafa-client >= %{version}-%{release}
Requires:	zarafa-common >= %{version}-%{release}
Requires:	zarafa-utils >= %{version}-%{release}

%description	archiver
This tool is used to attach or detach archives to a users store. An archive is
defined as a special non-active store or a folder inside such a store.

On top of managing archives, this tool is used to perform the actual archive
operation. Using the -u option, the archiver can be instructed to archive a
single store or all stores.

%package	msr
Summary:	Relocates mailboxes from one node to another
Group:		System/Servers
Requires:	zarafa-client >= %{version}-%{release}
Requires:	zarafa-common >= %{version}-%{release}
Requires:	zarafa-utils >= %{version}-%{release}
Requires:	python-MAPI >= %{version}-%{release}
Requires:	python-threadpool

%description	msr
In order to move mailboxes between multi-server nodes, the mailbox storage
relocator is available. The zarafa-msr tool should be used to relocate
mailboxes to other multi-server nodes.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1 -b .package

# mandriva patches
%patch100 -p1 -b .linkage
%patch101 -p1 -b .pthread
%patch103 -p1 -b .uuid

%build
# Needed to get rid of rpath
libtoolize --copy --force
autoreconf --force --install

CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -g -ggdb"
export CFLAGS
%configure2_5x \
    --with-userscript-prefix=%{_sysconfdir}/%{name}/userscripts \
    --with-quotatemplate-prefix=%{_sysconfdir}/%{name}/quotamail \
    --with-indexerscripts-prefix=%{_datadir}/%{name}/indexerscripts \
%if %{with_clucene}
    --with-clucene-lib-prefix=%{_libdir} \
    --with-clucene-include-prefix=%{_includedir} \
%else
    --with-clucene-lib-prefix= \
%endif
    --enable-release \
    --disable-static \
    --disable-testtools \
    --enable-perl

%make

%install
rm -rf %{buildroot}

make \
    docdir=%{_datadir}/doc/%{name}/ \
    datarootdir=%{_datadir} \
    DESTDIR=%{buildroot} \
    INSTALL='install -p' \
    BUILT_SOURCES='' \
    install \
    install-ajax-webaccess

# Nuke all overlefts from licensed, managed or other proprietary items
rm -rf %{buildroot}%{_sysconfdir}/%{name}/{license,licensed.cfg,report-ca}
rm -f %{buildroot}%{_mandir}/man?/zarafa-{backup,restore,report,ldapms.cfg,licensed{,.cfg}}.*

# Move all the initscripts to their appropriate place and
# ensure that all services are off by default at boot time
rm -rf %{buildroot}%{_sysconfdir}/init.d/
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d/
for service in dagent gateway ical indexer monitor server spooler; do
    if [ -f installer/linux/%{name}-$service.init.rhel ]; then
        sed -e 's@345@-@' installer/linux/%{name}-$service.init.rhel > \
            %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}-$service
        chmod 755 %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}-$service
        touch -c -r installer/linux/%{name}-$service.init.rhel %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}-$service
    fi
done

# Move the configuration files to their correct place and handle
# /usr/lib vs. /usr/lib64 for all architectures correct and set
# run_as_user, run_as_group and local_admin_users values correct
for config in %{buildroot}%{_datadir}/doc/%{name}/example-config/*.cfg; do
    config=$(basename $config)
    if [ -f %{buildroot}%{_datadir}/doc/%{name}/example-config/$config ]; then
        sed -e 's@\(run_as_\(user\|group\)[[:space:]]*=\).*@\1 %{name}@' -e 's@/usr/lib/zarafa@%{_libdir}/%{name}@' \
            -e 's@\(local_admin_users[[:space:]]*=[[:space:]]*root.*\)@\1 %{name}@' \
                %{buildroot}%{_datadir}/doc/%{name}/example-config/$config > %{buildroot}%{_sysconfdir}/%{name}/$config
        chmod 640 %{buildroot}%{_sysconfdir}/%{name}/$config
        touch -c -r %{buildroot}%{_datadir}/doc/%{name}/example-config/$config %{buildroot}%{_sysconfdir}/%{name}/$config
    fi
done

# Move the logrotate configuration file to its correct place
rm -f %{buildroot}%{_sysconfdir}/logrotate.d/*
for service in dagent gateway ical indexer licensed monitor server spooler; do
    sed -e "s@SERVICE@$service@" %{SOURCE2} >> %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
done
touch -c -r %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Move the userscripts to their correct place and symlink them
mkdir -p %{buildroot}%{_datadir}/%{name}/userscripts/
for userscript in companies_common.sh groups_common.sh users_common.sh \
            createcompany creategroup createuser deletecompany deletegroup deleteuser; do
    mv -f %{buildroot}{%{_sysconfdir},%{_datadir}}/%{name}/userscripts/$userscript
    ln -sf ../../..%{_datadir}/%{name}/userscripts/$userscript %{buildroot}%{_sysconfdir}/%{name}/userscripts/$userscript
done

# Create the data directory and install some files into
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -p -m 644 installer/linux/db-{calc-storesize,convert-attachments-to-files} %{buildroot}%{_datadir}/%{name}/
install -p -m 644 installer/linux/ssl-certificates.sh %{buildroot}%{_datadir}/%{name}/
%if %{with_ldap}
install -p -m 644 installer/linux/{db-upgrade-objectsid-to-objectguid,ldap-switch-sendas}.pl %{buildroot}%{_datadir}/%{name}/
install -p -m 644 installer/ldap/%{name}.schema %{buildroot}%{_datadir}/%{name}/
%else
rm -f %{buildroot}%{_sysconfdir}/%{name}/ldap.{active-directory,openldap,propmap}.cfg
rm -f %{buildroot}%{_mandir}/man5/%{name}-ldap.cfg.5*
%endif

# Create the default log and lib directory for packaging
mkdir -p %{buildroot}%{_localstatedir}/{log,lib}/%{name}/

# Remove all libtool .la files to avoid packaging of them
rm -f %{buildroot}{%{_libdir}/{,php/modules,php4,%{name}},%{perl_vendorarch}/auto/MAPI}/*.la

# Remove files that are anyway in %doc or %{_datadir}/%{name}/
rm -rf %{buildroot}%{_datadir}/doc/%{name}{,-indexer}/

# Remove unwanted/unused files that shouldn't exist anyway...
rm -f %{buildroot}%{_sysconfdir}/sysconfig/%{name}-indexer

# Move Indexer/CLucene related files to its correct places
%if %{with_clucene}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/indexerscripts/
mv -f %{buildroot}{%{_datadir},%{_sysconfdir}}/%{name}/indexerscripts/attachments_parser.db
for helper in attachments_parser xmltotext.xslt zmktemp; do
    ln -s ../../..%{_datadir}/%{name}/indexerscripts/$helper %{buildroot}%{_sysconfdir}/%{name}/indexerscripts/$helper
done
%else
rm -f %{buildroot}{%{_sysconfdir}/{rc.d/init.d,sysconfig},%{_mandir}/man?}/%{name}-indexer*
rm -rf %{buildroot}{%{_sysconfdir}/%{name}/indexer.cfg,%{_datadir}/%{name}/indexerscripts/}
%endif

# Move the webaccess configuration file to its correct place
mv -f %{buildroot}%{_sysconfdir}/%{name}/webaccess{-ajax,}
rm -f %{buildroot}%{_datadir}/%{name}-webaccess/config.php
ln -sf ../../..%{_sysconfdir}/%{name}/webaccess/config.php %{buildroot}%{_datadir}/%{name}-webaccess/config.php

# Install the apache configuration file for webaccess
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}-webaccess.conf

# Move the webaccess plugins directory to its correct place
rm -rf %{buildroot}{%{_datadir},%{_localstatedir}/lib}/%{name}-webaccess/plugins
mkdir -p %{buildroot}%{_datadir}/%{name}-webaccess/plugins/

# Remove unwanted language connectors and webaccess files
rm -f %{buildroot}%{_datadir}/%{name}-webaccess/client/widgets/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.{cfm,pl}
rm -f %{buildroot}%{_datadir}/%{name}-webaccess/{.htaccess,%{name}-webaccess.conf}
rm -f %{buildroot}%{_libdir}/php/extensions/mapi.*a

# bork
install -m0644 doc/zarafa.1 %{buildroot}%{_mandir}/man1/
install -m0644 installer/linux/ldap.active-directory.cfg %{buildroot}%{_sysconfdir}/%{name}/
install -m0644 installer/linux/ldap.openldap.cfg %{buildroot}%{_sysconfdir}/%{name}/
install -m0644 installer/linux/archiver.cfg %{buildroot}%{_sysconfdir}/%{name}/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%pre common
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "Zarafa Service Account" %{name}
exit 0

%post dagent
[ $1 -eq 1 ] && /sbin/chkconfig --add %{name}-dagent
# Ensure correct log file ownership after upgrade from official packages
chown %{name}:%{name} %{_localstatedir}/log/%{name}/dagent.* > /dev/null 2>&1 || :

%post ical
[ $1 -eq 1 ] && /sbin/chkconfig --add %{name}-ical
# Ensure correct log file ownership after upgrade from official packages
chown %{name}:%{name} %{_localstatedir}/log/%{name}/ical.* > /dev/null 2>&1 || :

%post gateway
[ $1 -eq 1 ] && /sbin/chkconfig --add %{name}-gateway
# Ensure correct log file ownership after upgrade from official packages
chown %{name}:%{name} %{_localstatedir}/log/%{name}/gateway.* > /dev/null 2>&1 || :

%post monitor
[ $1 -eq 1 ] && /sbin/chkconfig --add %{name}-monitor
# Ensure correct log file ownership after upgrade from official packages
chown %{name}:%{name} %{_localstatedir}/log/%{name}/monitor.* > /dev/null 2>&1 || :

%post server
[ $1 -eq 1 ] && /sbin/chkconfig --add %{name}-server
# Ensure correct log file ownership after upgrade from official packages
chown %{name}:%{name} %{_localstatedir}/log/%{name}/server.* > /dev/null 2>&1 || :

%post spooler
[ $1 -eq 1 ] && /sbin/chkconfig --add %{name}-spooler
# Ensure correct log file ownership after upgrade from official packages
chown %{name}:%{name} %{_localstatedir}/log/%{name}/spooler.* > /dev/null 2>&1 || :

%preun dagent
if [ $1 -eq 0 ]; then
    /sbin/service %{name}-dagent stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}-dagent
fi

%preun ical
if [ $1 -eq 0 ]; then
    /sbin/service %{name}-ical stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}-ical
fi

%preun gateway
if [ $1 -eq 0 ]; then
    /sbin/service %{name}-gateway stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}-gateway
fi

%preun monitor
if [ $1 -eq 0 ]; then
    /sbin/service %{name}-monitor stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}-monitor
fi

%preun server
if [ $1 -eq 0 ]; then
    /sbin/service %{name}-server stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}-server
fi

%preun spooler
if [ $1 -eq 0 ]; then
    /sbin/service %{name}-spooler stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}-spooler
fi

%postun dagent
if [ $1 -ne 0 ]; then
    /sbin/service %{name}-dagent condrestart > /dev/null 2>&1 || :
fi

%postun ical
if [ $1 -ne 0 ]; then
    /sbin/service %{name}-ical condrestart > /dev/null 2>&1 || :
fi

%postun gateway
if [ $1 -ne 0 ]; then
    /sbin/service %{name}-gateway condrestart > /dev/null 2>&1 || :
fi

%postun monitor
if [ $1 -ne 0 ]; then
    /sbin/service %{name}-monitor condrestart > /dev/null 2>&1 || :
fi

%postun server
if [ $1 -ne 0 ]; then
    /sbin/service %{name}-server condrestart > /dev/null 2>&1 || :
fi

%postun spooler
if [ $1 -ne 0 ]; then
    /sbin/service %{name}-spooler condrestart > /dev/null 2>&1 || :
fi

%post -n php-mapi
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun -n php-mapi
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3

%files caldav
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3

%files client
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_libdir}/libzarafaclient.so

%files common
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}/
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/log/%{name}/

%files dagent
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3 installer/linux/createuser.dotforward
%{_bindir}/%{name}-autorespond
%{_bindir}/%{name}-dagent
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/dagent.cfg
%config(noreplace) %{_sysconfdir}/%{name}/autorespond
%{_sysconfdir}/rc.d/init.d/%{name}-dagent
%{_mandir}/man1/%{name}-dagent.1*
%{_mandir}/man5/%{name}-dagent.cfg.5*

%files -n %{develname}
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_libdir}/libarchiver.so
%{_libdir}/libicalmapi.so
%{_libdir}/libinetmapi.so
%{_libdir}/libmapi.so
%{_libdir}/libcommon_mapi.a
%{_libdir}/libcommon_ssl.a
%{_libdir}/libcommon_util.a
%{_libdir}/libfreebusy.a
%{_libdir}/libzarafasync.a
%{_includedir}/icalmapi/
%{_includedir}/inetmapi/
%{_includedir}/mapi4linux/
%{_includedir}/libfreebusy/
%{_includedir}/libzarafasync
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files gateway
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_bindir}/%{name}-gateway
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/gateway.cfg
%{_sysconfdir}/rc.d/init.d/%{name}-gateway
%{_mandir}/man1/%{name}-gateway.1*
%{_mandir}/man5/%{name}-gateway.cfg.5*

%files ical
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_bindir}/%{name}-ical
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/ical.cfg
%{_sysconfdir}/rc.d/init.d/%{name}-ical
%{_mandir}/man1/%{name}-ical.1*
%{_mandir}/man5/%{name}-ical.cfg.5*

%files monitor
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_bindir}/%{name}-monitor
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/monitor.cfg
%dir %{_sysconfdir}/%{name}/quotamail/
%config(noreplace) %{_sysconfdir}/%{name}/quotamail/companyhard.mail
%config(noreplace) %{_sysconfdir}/%{name}/quotamail/companysoft.mail
%config(noreplace) %{_sysconfdir}/%{name}/quotamail/companywarning.mail
%config(noreplace) %{_sysconfdir}/%{name}/quotamail/userhard.mail
%config(noreplace) %{_sysconfdir}/%{name}/quotamail/usersoft.mail
%config(noreplace) %{_sysconfdir}/%{name}/quotamail/userwarning.mail
%{_sysconfdir}/rc.d/init.d/%{name}-monitor
%{_mandir}/man1/%{name}-monitor.1*
%{_mandir}/man5/%{name}-monitor.cfg.5*

%files server -f %{name}.lang
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_bindir}/%{name}-server
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/server.cfg
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/unix.cfg
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/zarafa
%{_sysconfdir}/rc.d/init.d/%{name}-server
%dir %{_sysconfdir}/%{name}/userscripts/
%{_sysconfdir}/%{name}/userscripts/createuser
%{_sysconfdir}/%{name}/userscripts/creategroup
%{_sysconfdir}/%{name}/userscripts/createcompany
%{_sysconfdir}/%{name}/userscripts/deleteuser
%{_sysconfdir}/%{name}/userscripts/deletegroup
%{_sysconfdir}/%{name}/userscripts/deletecompany
%{_sysconfdir}/%{name}/userscripts/*common.sh
%dir %{_sysconfdir}/%{name}/userscripts/createuser.d/
%dir %{_sysconfdir}/%{name}/userscripts/creategroup.d/
%dir %{_sysconfdir}/%{name}/userscripts/createcompany.d/
%dir %{_sysconfdir}/%{name}/userscripts/deleteuser.d/
%dir %{_sysconfdir}/%{name}/userscripts/deletegroup.d/
%dir %{_sysconfdir}/%{name}/userscripts/deletecompany.d/
%config(noreplace) %{_sysconfdir}/%{name}/userscripts/createcompany.d/00createpublic
%config(noreplace) %{_sysconfdir}/%{name}/userscripts/createuser.d/00createstore
%{_datadir}/%{name}/userscripts/
%{_libdir}/%{name}/dbplugin.so
%{_libdir}/%{name}/unixplugin.so
%{_mandir}/man1/%{name}-server.1*
%{_mandir}/man5/%{name}-server.cfg.5*
%{_mandir}/man5/%{name}-unix.cfg.5*
%if %{with_ldap}
%doc installer/ldap/%{name}.schema
%{_datadir}/%{name}/%{name}.schema
%{_datadir}/%{name}/db-upgrade-objectsid-to-objectguid.pl
%{_datadir}/%{name}/ldap-switch-sendas.pl
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/ldap.active-directory.cfg
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/ldap.openldap.cfg
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/ldap.propmap.cfg
%{_libdir}/%{name}/ldapplugin.so
%{_mandir}/man5/%{name}-ldap.cfg.5*
%endif

%files spooler
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_bindir}/%{name}-spooler
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/spooler.cfg
%{_sysconfdir}/rc.d/init.d/%{name}-spooler
%{_mandir}/man1/%{name}-spooler.1*
%{_mandir}/man5/%{name}-spooler.cfg.5*

%files utils
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_bindir}/%{name}-admin
%{_bindir}/%{name}-cfgchecker
%{_bindir}/%{name}-fsck
%{_bindir}/%{name}-passwd
%{_bindir}/%{name}-stats
%{_datadir}/%{name}/db-calc-storesize
%{_datadir}/%{name}/db-convert-attachments-to-files
%{_datadir}/%{name}/ssl-certificates.sh
%{_mandir}/man1/%{name}-admin.1*
%{_mandir}/man1/%{name}-cfgchecker.1*
%{_mandir}/man1/%{name}-fsck.1*
%{_mandir}/man1/%{name}-passwd.1*
%{_mandir}/man1/%{name}-stats.1*

%files -n %{libname}
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_libdir}/libarchiver.so.*
%{_libdir}/libicalmapi.so.*
%{_libdir}/libinetmapi.so.*
%{_libdir}/libmapi.so.*

%files -n php-mapi
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%config(noreplace) %{_sysconfdir}/php.d/%{name}.ini
%{_datadir}/php/mapi/
%{_libdir}/php/extensions/mapi.so

%if %{with_clucene}
%files indexer
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_bindir}/%{name}-indexer
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/indexer.cfg
%{_sysconfdir}/rc.d/init.d/%{name}-indexer
%dir %{_sysconfdir}/%{name}/indexerscripts/
%config(noreplace) %{_sysconfdir}/%{name}/indexerscripts/attachments_parser.db
%{_sysconfdir}/%{name}/indexerscripts/attachments_parser
%{_sysconfdir}/%{name}/indexerscripts/xmltotext.xslt
%{_sysconfdir}/%{name}/indexerscripts/zmktemp
%dir %{_datadir}/%{name}/indexerscripts/
%{_datadir}/%{name}/indexerscripts/attachments_parser
%{_datadir}/%{name}/indexerscripts/xmltotext.xslt
%{_datadir}/%{name}/indexerscripts/zmktemp
%{_mandir}/man1/%{name}-indexer.1*
%{_mandir}/man5/%{name}-indexer.cfg.5*
%endif

%files webaccess
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}-webaccess.conf
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/webaccess/
%config(noreplace) %{_sysconfdir}/%{name}/webaccess/config.php
%{_datadir}/%{name}-webaccess/
%dir %{_localstatedir}/lib/%{name}-webaccess/
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}-webaccess/tmp/

%files -n python-MAPI
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{py_platsitedir}/*MAPI*
%{py_platsitedir}/icalmapi*
%{py_platsitedir}/inetmapi*
%{py_platsitedir}/_icalmapi*
%{py_platsitedir}/_inetmapi*

%files archiver
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/archiver.cfg
%{_bindir}/%{name}-archiver
%{_mandir}/man1/%{name}-archiver.1*
%{_mandir}/man5/%{name}-archiver.cfg.5*

%files msr
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_bindir}/%{name}-msr
%{_mandir}/man1/%{name}-msr.1*
%{_mandir}/man5/%{name}-msr.cfg.5*
