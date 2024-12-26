Ansible Role: OS-RHEL9/RH_cronconf/OS_gathering
=======================================================
# Description
本ロールは、RHEL9に関する定期自動ジョブスケジュール設定についての情報の取得を行います。

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

本ロールでは、以下のロール、共通部品を利用しています。

- gathering ロール
- パラメータ生成共通部品(parameter_generate)

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description | 
| ---- | ------------- | ----------- | 
| `VAR_OS_gathering_dest` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス | 
| `VAR_OS_extracting_dest` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス | 
| `VAR_OS_python_cmd` | 'python3' | Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド | 

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/RH_cronconf/`

本ロールを既定値で利用した場合、以下のように設定情報を格納します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _gathered_data/
         └── 管理対象マシンホスト名 or IPアドレス/
              └── OS/  # OS設定ロール向け専用のフォルダ
                   └── RH_cronconf/  # 収集データ
                        └── file/  ※1
                               ・・・
~~~

※1 フォルダ配下に格納される収集ファイルは以下となります。

| Path | Description | 
| ---- | ----------- | 
| `/etc/cron.allow` | /etc/cron.allowファイル | 
| `/etc/cron.deny` | /etc/cron.denyファイル | 
| `/etc/cron.daily/` | /etc/cron.daily/配下のファイル | 
| `/etc/cron.hourly/` | /etc/cron.hourly/配下のファイル | 
| `/etc/cron.weekly/` | /etc/cron.weekly/配下のファイル | 
| `/etc/cron.monthly/` | /etc/cron.monthly/配下のファイル | 

## 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/RH_cronconf.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        RH_cronconf.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_RH_cronconf` | | 
| `- file` | コピー元ファイルcron.allowの情報（ファイル名前またはパス付けファイル名前）、収集不可ので常に''(空値)である | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.allow | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | cron.allowファイルの内容 | 
| `- file` | コピー元ファイルcron.denyの情報（ファイル名前またはパス付けファイル名前）、収集不可ので常に''(空値)である | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.deny |
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | cron.denyファイルの内容 | 
| `- file` | コピー元ファイル/etc/cron.daily/配下のファイルの情報（ファイル名前またはパス付けファイル名前）、収集不可ので常に''(空値)である | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.daily/配下 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/cron.daily/配下のファイル内容 | 
| `- file` | コピー元ファイル/etc/cron.hourly/配下のファイルの情報（ファイル名前またはパス付けファイル名前）、収集不可ので常に''(空値)である | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.hourly/配下 |
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/cron.hourly/配下のファイル内容 | 
| `- file` | コピー元ファイル/etc/cron.weekly/配下のファイルの情報（ファイル名前またはパス付けファイル名前）、収集不可ので常に''(空値)である | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.weekly/配下 |
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/cron.weekly/配下のファイル内容 | 
| `- file` | コピー元ファイル/etc/cron.monthly/配下のファイルの情報（ファイル名前またはパス付けファイル名前）、収集不可ので常に''(空値)である | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/cron.monthly/配下 |
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/cron.monthly/配下のファイル内容 | 

### Example
~~~
VAR_RH_cronconf:
- file: ''
  path: /etc/cron.deny
  text: []
- file: ''
  path: /etc/cron.hourly/0anacron
  text:
  - '#!/bin/sh'
  - '# Check whether 0anacron was run today already'
  - if test -r /var/spool/anacron/cron.daily; then
  - '    day=`cat /var/spool/anacron/cron.daily`'
  - fi
  ・・・
- file: ''
  path: /etc/cron.daily/logrotate
  text:
  - '#!/bin/sh'
  - ''
  - /usr/sbin/logrotate -s /var/lib/logrotate/logrotate.status /etc/logrotate.conf
  - EXITVALUE=$?
  - if [ $EXITVALUE != 0 ]; then
  ・・・
- file: ''
  path: /etc/cron.daily/rhsmd
  text:
  - '#!/bin/sh'
  - '# nightly run of rhsmd to log entitlement expiration/validity errors to syslog'
  - '# this is a cron job because it doesn''t need to ''phone home''. should that'
  - '# change, look into calling the dbus interface from rhsmcertd instead.'
  - /usr/libexec/rhsmd -s
- file: ''
  path: /etc/cron.daily/man-db.cron
  text:
  - '#!/bin/bash'
  - ''
  - if [ -e /etc/sysconfig/man-db ]; then
  - '    . /etc/sysconfig/man-db'
  - fi
  ・・・
~~~

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-RHEL9
    │         └── RH_cronconf/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
    │                   │── tasks/
    │                   │      check.yml
    │                   │      gathering.yml
    │                   │      generate.yml
    │                   │      main.yml
    │                   │── vars/
    │                   │      gathering_definition.yml
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
    - role: OS-RHEL9/RH_cronconf/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── RH_cronconf/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        RH_cronconf.yml  # パラメータ
~~~

## パラメータ再利用

以下の例では、生成したパラメータを使用してOSの設定を変更します。

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_cronconf/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        RH_cronconf.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
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
