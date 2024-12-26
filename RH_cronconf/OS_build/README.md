Ansible Role: OS-RHEL9/RH_cronconf/OS_build
=======================================================
# Description
本ロールは、RHEL9に関する定期自動ジョブスケジュール設定についての情報の設定を行います。

# Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL8）
  * Ansible バージョン 2.11.0 以上 (動作確認バージョン [core 2.11.12])
  * Python バージョン 3.x  (動作確認バージョン 3.6.8)
- 管理対象マシン
  * RHEL9

# Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへssh接続できる必要があります。
- 管理対象マシン
  * RHEL9

# Dependencies

本ロールでは、他のロールは必要ありません。
ただし、本READMEに書かれている「エビデンスを取得する場合」の手順を行う場合は、
OS-RHEL9/RH_cronconf/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_RH_cronconf` | | 
| `- file` | コピー元ファイルcron.allowの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.allow | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | cron.allowファイルの内容 | 
| `- file` | コピー元ファイルcron.denyの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.deny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | cron.denyファイルの内容 | 
| `- file` | コピー元ファイル/etc/cron.daily/配下のファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.daily/配下 |
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/cron.daily/配下のファイル内容 | 
| `- file` | コピー元ファイル/etc/cron.hourly/配下のファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.hourly/配下 |
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/cron.hourly/配下のファイル内容 | 
| `- file` | コピー元ファイル/etc/cron.weekly/配下のファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.weekly/配下 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/cron.weekly/配下のファイル内容 | 
| `- file` | コピー元ファイル/etc/cron.monthly/配下のファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.monthly/配下 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/cron.monthly/配下のファイル内容 |  

### Example
~~~
VAR_RH_cronconf:
- file: ''
  path: /etc/cron.deny
  text: []
- file: 0anacron
  path: /etc/cron.hourly/0anacron
  text:
  - '#!/bin/sh'
  - '# Check whether 0anacron was run today already'
  - if test -r /var/spool/anacron/cron.daily; then
  - '    day=`cat /var/spool/anacron/cron.daily`'
  - fi
  ・・・
- file: etc/cron.daily/logrotate
  path: /etc/cron.daily/logrotate
  text:
  - '#!/bin/sh'
  - ''
  - /usr/sbin/logrotate -s /var/lib/logrotate/logrotate.status /etc/logrotate.conf
  - EXITVALUE=$?
  - if [ $EXITVALUE != 0 ]; then
  ・・・
- file: rhsmd
  path: /etc/cron.daily/rhsmd
  text:
  - '#!/bin/sh'
  - '# nightly run of rhsmd to log entitlement expiration/validity errors to syslog'
  - '# this is a cron job because it doesn''t need to ''phone home''. should that'
  - '# change, look into calling the dbus interface from rhsmcertd instead.'
  - /usr/libexec/rhsmd -s
- file: man-db.cron
  path: /etc/cron.daily/man-db.cron
~~~

~~~
0anacronファイルの内容：
#!/bin/sh
# Check whether 0anacron was run today already
if test -r /var/spool/anacron/cron.daily; then
    day=`cat /var/spool/anacron/cron.daily`
fi
・・・
~~~

~~~
logrotateファイルの内容：
#!/bin/sh

/usr/sbin/logrotate -s /var/lib/logrotate/logrotate.status /etc/logrotate.conf
EXITVALUE=$?
if [ $EXITVALUE != 0 ]; then
・・・
~~~

~~~
rhsmdファイルの内容：
#!/bin/sh
# nightly run of rhsmd to log entitlement expiration/validity errors to syslog
# this is a cron job because it doesn't need to 'phone home'. should that
# change, look into calling the dbus interface from rhsmcertd instead.
/usr/libexec/rhsmd -s
~~~

~~~
man-db.cronファイルの内容：
#!/bin/bash

if [ -e /etc/sysconfig/man-db ]; then
    . /etc/sysconfig/man-db
fi
・・・
~~~


## Optional Variables

特にありません。

# Usage

1. 本ロールを用いたPlaybookを作成します。
2. 変数を必要に応じて設定します。
3. Playbookを実行します。

# Example Playbook

## ■エビデンスを取得しない場合の呼び出す方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-RHEL9
    │         └── RH_cronconf/
    │              └── OS_build/
    │                   │── files/
    │                   │   │── etc/
    │                   │   │   └─ cron.daily/
    │                   │   │      └─ logrotate
    │                   │   │── man-db.cron
    │                   │   │── rhsmd
    │                   │   │── 0anacron
    │                   │   └── ・・・
    │                   │── tasks/
    │                   │      build_flat.yml
    │                   │      main.yml
    │                   │── templates/
    │                   │      flat_template
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
    - role: OS-RHEL9/RH_cronconf/OS_build
      VAR_RH_cronconf:
      - file: ''
        path: /etc/cron.deny
        text: []
      - file: 0anacron
        path: /etc/cron.hourly/0anacron
        text:
        - '#!/bin/sh'
        - '# Check whether 0anacron was run today already'
        - if test -r /var/spool/anacron/cron.daily; then
        - '    day=`cat /var/spool/anacron/cron.daily`'
        - fi
        ・・・
      - file: etc/cron.daily/logrotate
        path: /etc/cron.daily/logrotate
        text:
        - '#!/bin/sh'
        - ''
        - /usr/sbin/logrotate -s /var/lib/logrotate/logrotate.status /etc/logrotate.conf
        - EXITVALUE=$?
        - if [ $EXITVALUE != 0 ]; then
        ・・・
      - file: rhsmd
        path: /etc/cron.daily/rhsmd
        text:
        - '#!/bin/sh'
        - '# nightly run of rhsmd to log entitlement expiration/validity errors to syslog'
        - '# this is a cron job because it doesn''t need to ''phone home''. should that'
        - '# change, look into calling the dbus interface from rhsmcertd instead.'
        - /usr/libexec/rhsmd -s
      - file: man-db.cron
        path: /etc/cron.daily/man-db.cron
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

## ■エビデンスを取得する場合の呼び出す方法

エビデンスを収集する場合、以下のようなエビデンス収集用のPlaybookを作成してください。  

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_cronconf/OS_build
      VAR_RH_cronconf:
      - file: ''
        path: /etc/cron.deny
        text: []
      - file: 0anacron
        path: /etc/cron.hourly/0anacron
        text:
        - '#!/bin/sh'
        - '# Check whether 0anacron was run today already'
        - if test -r /var/spool/anacron/cron.daily; then
        - '    day=`cat /var/spool/anacron/cron.daily`'
        - fi
        ・・・
      - file: etc/cron.daily/logrotate
        path: /etc/cron.daily/logrotate
        text:
        - '#!/bin/sh'
        - ''
        - /usr/sbin/logrotate -s /var/lib/logrotate/logrotate.status /etc/logrotate.conf
        - EXITVALUE=$?
        - if [ $EXITVALUE != 0 ]; then
        ・・・
      - file: rhsmd
        path: /etc/cron.daily/rhsmd
        text:
        - '#!/bin/sh'
        - '# nightly run of rhsmd to log entitlement expiration/validity errors to syslog'
        - '# this is a cron job because it doesn''t need to ''phone home''. should that'
        - '# change, look into calling the dbus interface from rhsmcertd instead.'
        - /usr/libexec/rhsmd -s
      - file: man-db.cron
        path: /etc/cron.daily/man-db.cron
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_cronconf/OS_gathering
  strategy: free
~~~

- エビデンス収集結果一覧

エビデンス収集結果は、以下のように格納されます。
エビデンス収集結果の詳細は、OS_gatheringロールを確認してください。

~~~
#エビデンス構成
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── RH_cronconf/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_cronconf.yml
~~~

# Remarks
-------
パラメータfileが下記のいずれかを満たす場合、設定したtextの内容を書き換えます。
- 定義されていません
- 値に何も設定しません
- 設定値が""（空値)です。

上記以外の場合、パラメータfileに有効な値(※指定した内容の有効性はユーザーが保証する必要)であれば、下記の通りに処理します。
- fileに指定した内容がファイル名前または相対パス付けのファイル名前であるとき、filesの配下に対応するファイルを指定されるパスにコピーします。
- fileに指定した内容が絶対パス付けのファイル名前であるとき、指定したファイルを指定されるパスにコピーします。

# License
-------

# Copyright
---------
Copyright (c) 2024 NEC Corporation

# Author Information
------------------
NEC Corporation
