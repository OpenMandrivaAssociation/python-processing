Name:		python-processing
Version:	0.52
Release:	%mkrel 2
Group:		Sciences/Other
License:	BSD
Summary:	Python processing
Source:		http://prdownload.berlios.de/pyprocessing/processing-%{version}.zip
URL:		http://pyprocessing.berlios.de
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	python-devel

%description
processing is a package for the Python language which supports the spawning
of processes using the API of the standard library's threading module. It
runs on both Unix and Windows.

Features:

    * Objects can be transferred between processes using pipes or
      multi-producer/multi-consumer queues.
    * Objects can be shared between processes using a server process or
      (for simple data) shared memory.
    * Equivalents of all the synchronization primitives in threading are
      available.
    * A Pool class makes it easy to submit tasks to a pool of worker
      processes.

%prep
%setup -q -q -n processing-%{version}

%build

%install
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
