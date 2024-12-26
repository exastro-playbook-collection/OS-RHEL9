Ansible Role: OS-RHEL9/RH_systemd/OS_build
=======================================================
# Description
本ロールは、RHEL9に関するサービス管理設定についての情報の設定を行います。

# Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL8）
  * Ansible バージョン 2.11 以上 (動作確認バージョン [core 2.11.12])
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
OS-RHEL9/RH_systemd/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_RH_systemd` | | 
| `- file` | コピー元ファイルsystem.confの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/systemd/system.conf | 
| &nbsp;&nbsp;&nbsp;&nbsp;`value` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- section` | セクション名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`properties` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`プロパティ名：設定値`| プロパティ名<br>設定値 | 
| `- file` | コピー元ファイルuser.confの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/systemd/user.conf |
| &nbsp;&nbsp;&nbsp;&nbsp;`value` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- section` | セクション名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`properties` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`プロパティ名：設定値`| プロパティ名<br>設定値 | 
| `- file` | コピー元ファイル/etc/systemd/system/配下の*.serviceと*.socketファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/systemd/system/配下の*.serviceと*.socketファイル | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/sudoers.d/配下の*.serviceと*.socketファイルの内容 | 

### Example
~~~
VAR_RH_systemd:
- file: ''
  path: /etc/systemd/system.conf
  value:
  - properties:
      JoinControllers: cpu,cpuacct net_cls,net_prio
      LogColor: 'yes'
      LogLevel: info
      LogLocation: 'no'
      LogTarget: journal-or-kmsg
    section: Manager
- file: user.conf
  path: /etc/systemd/user.conf
  value:
  - properties:
      LogColor: 'yes'
      LogLevel: info
      LogLocation: 'no'
      LogTarget: console
    section: Manager
- file: ''
  path: /etc/systemd/system/application@.service
  text:
  - '[Unit]'
  - Description=chargen-dgrm service
  - ''
  - '[Service]'
  - Type=UNLISTED
　・・・
- file: ''
  path: /etc/systemd/system/application.socket
  text:
  - '[Unit]'
  - Description=Application Socket
  - ''
  - '[Socket]'
　・・・
~~~

~~~
user.confファイルの内容：
This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.
#
# You can override the directives in this file by creating files in
# /etc/systemd/user.conf.d/*.conf.
#
# See systemd-user.conf(5) for details

[Manager]
#LogLevel=info
#LogTarget=console
#LogColor=yes
#LogLocation=no
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
    │         └── RH_systemd/
    │              └── OS_build/
    │                   │── files/
    │                   │      user.conf
    │                   │      ・・・
    │                   │── tasks/
    │                   │      main.yml
    │                   │      build_property_section.yml
    │                   │      modify_property_section.yml
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
    - role: OS-RHEL9/RH_systemd/OS_build
      VAR_RH_systemd:
      - file: ''
        path: /etc/systemd/system.conf
        value:
        - properties:
            JoinControllers: cpu,cpuacct net_cls,net_prio
            LogColor: 'yes'
            LogLevel: info
            LogLocation: 'no'
            LogTarget: journal-or-kmsg
          section: Manager
      - file: user.conf
        path: /etc/systemd/user.conf
        value:
        - properties:
            LogColor: 'yes'
            LogLevel: info
            LogLocation: 'no'
            LogTarget: console
          section: Manager
      - file: ''
        path: /etc/systemd/system/application@.service
        text:
        - '[Unit]'
        - Description=chargen-dgrm service
        - ''
        - '[Service]'
        - Type=UNLISTED
      　・・・
      - file: ''
        path: /etc/systemd/system/application.socket
        text:
        - '[Unit]'
        - Description=Application Socket
        - ''
        - '[Socket]'
      　・・・
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
    - role: OS-RHEL9/RH_systemd/OS_build
      VAR_RH_systemd:
      - file: ''
        path: /etc/systemd/system.conf
        value:
        - properties:
            JoinControllers: cpu,cpuacct net_cls,net_prio
            LogColor: 'yes'
            LogLevel: info
            LogLocation: 'no'
            LogTarget: journal-or-kmsg
          section: Manager
      - file: user.conf
        path: /etc/systemd/user.conf
        value:
        - properties:
            LogColor: 'yes'
            LogLevel: info
            LogLocation: 'no'
            LogTarget: console
          section: Manager
      - file: ''
        path: /etc/systemd/system/application@.service
        text:
        - '[Unit]'
        - Description=chargen-dgrm service
        - ''
        - '[Service]'
        - Type=UNLISTED
      　・・・
      - file: ''
        path: /etc/systemd/system/application.socket
        text:
        - '[Unit]'
        - Description=Application Socket
        - ''
        - '[Socket]'
      　・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_systemd/OS_gathering
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
    │              └── RH_systemd/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_systemd.yml
~~~

# Remarks
-------
パラメータfileが下記のいずれかを満たす場合、設定したpropertiesまたは設定したtextの内容を利用して構築ロールを実行します。
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
