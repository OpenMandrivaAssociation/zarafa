%define	major 0
%define	libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

%define beta_or_rc 0
%define actual_release 2
%define svnrevision 18984
%define with_ldap 1
%define with_xmlto 1

Summary:	Zarafa Outlook Sharing and Open Source Collaboration
Name:		zarafa
Version:	6.30.12
%if %{beta_or_rc}
Release:	%mkrel 0.%{actual_release}.svn%{svnrevision}
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
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.ini
Patch0:		zarafa-6.30.4-package.patch
# Patch 1, 2 and 3 were sent to upstream
Patch1:		zarafa-6.30.4-perl.patch
Patch2:		zarafa-6.30.10-undefined-symbol.patch
Patch3:		zarafa-6.30.10-chmod.patch
# Patch 4 and 5 are backports from upstream
Patch4:		zarafa-6.30.10-fortify.patch
Patch5:		zarafa-6.30.10-long-ulong.patch
# http://www.brodowski.org/zarafa/php-mapi/6.30.10.18495/18495_patch.diff
Patch10:	zarafa-6.30.4-brodowski.patch
Patch11:	zarafa-6.30.10-linkage_fix.diff
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	curl-devel
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	libical-devel >= 0.42
BuildRequires:	libuuid-devel
BuildRequires:	libvmime07-devel
BuildRequires:	libxml2-devel
BuildRequires:	mysql-devel >= 4.1
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	perl-devel
BuildRequires:	php-devel >= 3:5.2.0
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

%package -n perl-libmapi
Summary:	Perl Mapi extension libraries by Zarafa
Group:		Development/Perl
Requires:	perl

%description -n perl-libmapi
Perl MAPI extension libraries by Zarafa.

%package -n php-mapi
Summary:	A PHP Mapi client by Zarafa
Group:		Development/PHP
# Bug: Without mod_ssl, reloading httpd causes core dump
Requires:	apache-mod_ssl
Requires:	apache-mod_php >= 5.2

%description -n php-mapi
PHP MAPI extension by Zarafa to enable MAPI communication in PHP.

%prep
%setup -q
%patch0 -p1 -b .package
%patch1 -p1 -b .perl
%patch2 -p1 -b .symbol
%patch3 -p1 -b .chmod
%patch4 -p1 -b .fortify
%patch5 -p1 -b .long-ulong
#%%patch10 -p5 -b .brodowski
%patch11 -p0

%build
# Needed to get rid of rpath
libtoolize --force
autoreconf --force --install

CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -g -ggdb"
export CFLAGS
%configure2_5x \
    --with-userscript-prefix=%{_sysconfdir}/%{name}/userscripts \
    --with-quotatemplate-prefix=%{_sysconfdir}/%{name}/quotamail \
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
    install

# Nuke all overlefts from licensed, managed or other proprietary items
rm -rf %{buildroot}%{_sysconfdir}/%{name}/report-ca
rm -f %{buildroot}%{_mandir}/man?/zarafa-{backup,restore,ldapms.cfg,licensed{,.cfg}}.*

# Move all the initscripts to their appropriate place and
# ensure that all services are off by default at boot time
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d/
for service in server spooler dagent gateway monitor ical; do
    if [ -f %{buildroot}%{_datadir}/doc/%{name}/%{name}-$service.init.fc ]; then
        sed -e 's@345@-@' %{buildroot}%{_datadir}/doc/%{name}/%{name}-$service.init.fc > \
            %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}-$service
        chmod 755 %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}-$service
        touch -c -r %{buildroot}{%{_datadir}/doc/%{name}/%{name}-$service.init.fc,%{_sysconfdir}/rc.d/init.d/%{name}-$service}
    fi
done

# Move the configuration files to their correct place and handle
# /usr/lib vs. /usr/lib64 for all architectures correct and set
# run_as_user, run_as_group and local_admin_users values correct
for config in %{buildroot}%{_datadir}/doc/%{name}/*.cfg; do
    config=$(basename $config)
    if [ -f %{buildroot}%{_datadir}/doc/%{name}/$config ]; then
        sed -e 's@\(run_as_\(user\|group\)[[:space:]]*=\).*@\1 %{name}@' -e 's@/usr/lib/zarafa@%{_libdir}/%{name}@' \
            -e 's@\(local_admin_users[[:space:]]*=[[:space:]]*root.*\)@\1 %{name}@' \
                %{buildroot}%{_datadir}/doc/%{name}/$config > %{buildroot}%{_sysconfdir}/%{name}/$config
        chmod 640 %{buildroot}%{_sysconfdir}/%{name}/$config
        touch -c -r %{buildroot}%{_datadir}/doc/%{name}/$config %{buildroot}%{_sysconfdir}/%{name}/$config
    fi
done

# Move the logrotate configuration file to it's correct place
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
sed -e 's@\(}\)@        create 0644 %{name} %{name}\n\1@' -e '1,6d' \
  %{buildroot}%{_datadir}/doc/%{name}/%{name}.logrotate > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
touch -c -r %{buildroot}%{_datadir}/doc/%{name}/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install the PHP module configuration file appropriate
mkdir -p %{buildroot}%{_sysconfdir}/php.d/
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/php.d/%{name}.ini

# Create missing userscript directories for packaging them
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/userscripts/{create,delete}{user,group,company}.d/

# Move the userscripts to their correct place and symlink them
mkdir -p %{buildroot}%{_datadir}/%{name}/userscripts/
for userscript in companies_common.sh groups_common.sh users_common.sh \
            createcompany creategroup createuser deletecompany deletegroup deleteuser; do
    mv -f %{buildroot}{%{_sysconfdir},%{_datadir}}/%{name}/userscripts/$userscript
    ln -sf ../../..%{_datadir}/%{name}/userscripts/$userscript %{buildroot}%{_sysconfdir}/%{name}/userscripts/$userscript
done

# Create the data directory and install some files into
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -p -m 755 installer/linux/db-{calc-storesize,convert-attachments-to-files} %{buildroot}%{_datadir}/%{name}/
install -p -m 755 installer/linux/ssl-certificates.sh %{buildroot}%{_datadir}/%{name}/

# Create the default log and lib directory for packaging
mkdir -p %{buildroot}%{_localstatedir}/{log,lib}/%{name}/

# Remove all libtool .la files to avoid packaging of them
rm -f %{buildroot}%{_libdir}/{,php/extensions,%{name}}/*.la

# Remove files that are anyway in %doc or %{_datadir}/%{name}/
rm -rf %{buildroot}%{_datadir}/doc/%{name}/

# nuke files that belongs to a licensed release
rm -f %{buildroot}%{_mandir}/man1/zarafa-report.1*

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
%doc installer/licenseagreement/AGPL-3 doc/performance-tuning.txt
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
%{_sysconfdir}/rc.d/init.d/%{name}-dagent
%{_mandir}/man1/%{name}-dagent.1*
%{_mandir}/man5/%{name}-dagent.cfg.5*

%files -n %{develname}
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_libdir}/libicalmapi.so
%{_libdir}/libinetmapi.so
%{_libdir}/libmapi.so
%{_libdir}/libperlmapi.so
%{_libdir}/libcommon_mapi.a
%{_libdir}/libcommon_ssl.a
%{_libdir}/libcommon_util.a
%{_libdir}/libfreebusy.a
%{_includedir}/icalmapi/
%{_includedir}/inetmapi/
%{_includedir}/mapi4linux/
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
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/ldap.active-directory.cfg
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/ldap.openldap.cfg
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
%{_bindir}/%{name}-fsck
%{_bindir}/%{name}-passwd
%{_bindir}/%{name}-stats
%{_datadir}/%{name}/db-calc-storesize
%{_datadir}/%{name}/db-convert-attachments-to-files
%{_datadir}/%{name}/ssl-certificates.sh
%{_mandir}/man1/%{name}-admin.1*
%{_mandir}/man1/%{name}-fsck.1*
%{_mandir}/man1/%{name}-passwd.1*
%{_mandir}/man1/%{name}-stats.1*

%files -n %{libname}
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_libdir}/libicalmapi.so.*
%{_libdir}/libinetmapi.so.*
%{_libdir}/libmapi.so.*

%files -n perl-libmapi
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%{_libdir}/libperlmapi.so.*

%files -n php-mapi
%defattr(-,root,root,-)
%doc installer/licenseagreement/AGPL-3
%config(noreplace) %{_sysconfdir}/php.d/%{name}.ini
%{_datadir}/php/mapi/
%{_libdir}/php/extensions/mapi.so

