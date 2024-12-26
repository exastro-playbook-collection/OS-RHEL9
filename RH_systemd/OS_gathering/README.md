Ansible Role: OS-RHEL9/RH_systemd/OS_gathering
=======================================================
# Description
本ロールは、RHEL9に関するサービス管理設定についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/RH_systemd/`

本ロールを既定値で利用した場合、以下のように設定情報を格納します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _gathered_data/
         └── 管理対象マシンホスト名 or IPアドレス/
              └── OS/  # OS設定ロール向け専用のフォルダ
                   └── RH_systemd/  # 収集データ
                        └── file/  ※1
                               ・・・
~~~

※1 フォルダ配下に格納される収集ファイルは以下となります。

| Path | Description | 
| ---- | ----------- | 
| `/etc/systemd/system.conf` | /etc/systemd/system.confファイル | 
| `/etc/systemd/user.conf` | /etc/systemd/user.confファイル | 
| `/etc/systemd/system/*.service` | /etc/systemd/system/配下の*.serviceファイル | 
| `/etc/systemd/system/*.socket` | /etc/systemd/system/配下の*.socketファイル | 

## 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/RH_systemd.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        RH_systemd.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`プロパティ名：設定値` | プロパティ名<br>設定値 | 
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
- file: ''
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

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-RHEL9
    │         └── RH_systemd/
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
    - role: OS-RHEL9/RH_systemd/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── RH_systemd/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        RH_systemd.yml  # パラメータ
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
    - role: OS-RHEL9/RH_systemd/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        RH_systemd.yml  # パラメータ
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
