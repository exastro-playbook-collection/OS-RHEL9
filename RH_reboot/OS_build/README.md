Ansible Role: OS-RHEL9/RH_reboot/OS_build 
=======================================================

## Description
本ロールは、RHEL9に関するOSの再起動、シャットダウン、サービスの再起動およびsysctl読み込むファイルの設定についての情報の設定を行います。
以下の用途で使用することができます。
* 単独で行いたい場合
* 複数のロールを呼び出し、それぞれで再起動またはシャットダウンが必要になる可能性があるが、再起動またはシャットダウンは最後に一度だけ行えば良い場合

## Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL8）
  * Ansible バージョン 2.11 以上 (動作確認バージョン [core 2.11.12])
  * Python バージョン 3.x  (動作確認バージョン 3.6.8)
- 管理対象マシン
  * RHEL9

## Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへssh接続できる必要があります。
- 管理対象マシン
  * RHEL9

# Dependencies

本ロールでは、他のロールは必要ありません。

## Role Variables
本ロールで指定できる変数値について説明します。

### Mandatory variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_RH_reboot` | | 
| &nbsp;&nbsp;&nbsp;&nbsp;`reboot_requires` | OSを再起動するフラグ<br>true: OSを再起動する<br>false: OSを再起動しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`daemonReexec_requires` | systemd マネージャーがマネージャーの状態をシリアル化する<br>true: シリアル化する<br>false: シリアル化しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`daemonReload_requires` | systemd が変更を読み取る<br>true: 読み取る<br>false: 読み取しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`nmcli_restart` | nmcliコマンドでNetworkManagerサービスの再起動<br>true: 再起動する<br>false: 再起動しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`restarted_services` | 指定されたサービスを再起動する。systemdコマンドでサポートできるサービス以外、下記のサービス名も指定できます。<br>udev:udevルール再ロード | 
| &nbsp;&nbsp;&nbsp;&nbsp;`shutdown_requires` | OSをシャットダウンするフラグ<br>true: OSをシャットダウンする<br>false: OSをシャットダウンしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`sysctlfile` | sysctl読み込むファイルを指定する | 

### Example
~~~
VAR_RH_reboot:
  sysctlfile: /etc/sysctl.conf
  daemonReexec_requires: false
  daemonReload_requires: false
  nmcli_restart: false
  restarted_services:
    - httpd
    - vsftpd
  reboot_requires: true
  shutdown_requires: false

~~~
### Optional variables

特にありません。

# Usage

1. 本ロールを用いたPlaybookを作成します。
2. 変数を必要に応じて設定します。
3. Playbookを実行します。

# Example Playbook

### ■単独で再起動を行う方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成
~~~
 - playbook/
    │── roles/
    │    └── OS-RHEL9
    │         └── RH_reboot/
    │              └── OS_build/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── handlers/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      main.yml
    │                   └─ README.md
    └─ master_playbook.yml
~~~

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_reboot/OS_build
      VAR_RH_reboot:
        sysctlfile: /etc/sysctl.conf
        daemonReexec_requires: false
        daemonReload_requires: false
        nmcli_restart: false
        restarted_services:
          - httpd
          - vsftpd
        reboot_requires: true
        shutdown_requires: false
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

### ■複数ロール間で再起動を制御する方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成（2つの設定ロール`RH_grub2`/`RH_kdump`とともに使用する例）
~~~
 - playbook/
    │── roles/
    │    └── OS-RHEL9
    │         └── RH_grub2/
    │         │    └── OS_build/
    │         │         │── tasks/
    │         │         │      main.yml
    │         │         │      modify_property.yml
    │         │         └─ README.md
    │         └── RH_kdump/
    │         │    └── OS_build/
    │         │         │── files/
    │         │         │      kdump.conf
    │         │         │── tasks/
    │         │         │      build_flat.yml
    │         │         │      main.yml
    │         │         │── templates/
    │         │         │      flat_template
    │         │         └─ README.md
    │         └──RH_reboot/
    │              └── OS_build/
    │                   │── defaults/
    │                   │       main.yml
    │                   │── handlers/
    │                   │       main.yml
    │                   │── tasks/
    │                   │       main.yml
    │                   └─ README.md
    └─ master_playbook.yml
~~~

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_grub2/OS_build
      VAR_RH_grub2:
      - path: /etc/default/grub
        properties:
          GRUB_CMDLINE_LINUX: '"console=ttyS0,115200n8 console=tty0 net.ifnames=0 rd.blacklist=nouveau crashkernel=auto"'
          GRUB_DEFAULT: saved
          GRUB_DISABLE_RECOVERY: '"true"'
          GRUB_DISABLE_SUBMENU: 'true'
          GRUB_DISTRIBUTOR: '"$(sed ''s, release .*$,,g'' /etc/system-release)"'
          ・・・
    - role: OS-RHEL9/RH_kdump/OS_build
      VAR_RH_kdump:
      - file: kdump.conf
        path: /etc/kdump.conf
        text:
        - '# This file contains a series of commands to perform (in order) in the kdump'
        - '# kernel after a kernel crash in the crash kernel(1st kernel) has happened.'
        - '#'
        - '# Directives in this file are only applicable to the kdump initramfs, and have'
        - '# no effect once the root filesystem is mounted and the normal init scripts are'
        ・・・
    - role: OS-RHEL9/RH_reboot/OS_build
      VAR_RH_reboot:
        daemonReexec_requires: false
        daemonReload_requires: false
        nmcli_restart: false
        restarted_services:
          - kdump
        reboot_requires: true
        shutdown_requires: false
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

# Remarks
-------

# License
-------

# Copyright
---------
Copyright (c) 2024 NEC Corporation

# Author Information
------------------
NEC Corporation
