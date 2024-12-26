Ansible Role: OS-RHEL9/RH_sudo/OS_build
=======================================================
# Description
本ロールは、RHEL9に関するsudo設定についての情報の設定を行います。

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
OS-RHEL9/RH_sudo/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_RH_sudo` | | 
| `- file` | コピー元ファイルsudo.confの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/sudo.conf | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | sudo.confファイルの内容 | 
| `- file` | コピー元ファイルsudoersの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/sudoers | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | sudoersファイルの内容 | 
| `- file` | コピー元ファイル/etc/sudoers.d/配下のファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/sudoers.d/配下 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/sudoers.d/配下のファイルの内容 | 

### Example
~~~
VAR_RH_sudo:
- file: sudo.conf
  path: /etc/sudo.conf
  text:
  - '#'
  - '# Default /etc/sudo.conf file'
  - '#'
  - '# Format:'
  - '#   Plugin plugin_name plugin_path plugin_options ...'
  ・・・
- file: ''
  path: /etc/sudoers
  text:
  - '## Sudoers allows particular users to run various commands as'
  - '## the root user, without needing the root password.'
  - '##'
  - '## Examples are provided at the bottom of the file for collections'
  - '## of related commands, which can then be delegated out to particular'
  ・・・
- file: etc/sudoers.d/swadmin
  path: /etc/sudoers.d/swadmin
  text:
  - '#########Start/Stop Service###############'
  - Cmnd_Alias SWADMIN_START_SERVICES = /etc/rc.d/init.d/*
  - swadmin ALL=(ALL)NOPASSWD:SWADMIN_START_SERVICES
  ・・・
~~~

~~~
sudo.confファイルの内容：
#
# Default /etc/sudo.conf file
#
# Format:
#   Plugin plugin_name plugin_path plugin_options ...
・・・
~~~

~~~
etc/sudoers.d/swadminファイルの内容：
#########Start/Stop Service###############
Cmnd_Alias SWADMIN_START_SERVICES = /etc/rc.d/init.d/*
swadmin ALL=(ALL)NOPASSWD:SWADMIN_START_SERVICES
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
    │         └── RH_sudo/
    │              └── OS_build/
    │                   │── files/
    │                   │      sudo.conf
    │                   │      ・・・
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
    - role: OS-RHEL9/RH_sudo/OS_build
      VAR_RH_sudo:
      - file: sudo.conf
        path: /etc/sudo.conf
        text:
        - '#'
        - '# Default /etc/sudo.conf file'
        - '#'
        - '# Format:'
        - '#   Plugin plugin_name plugin_path plugin_options ...'
        ・・・
      - file: ''
        path: /etc/sudoers
        text:
        - '## Sudoers allows particular users to run various commands as'
        - '## the root user, without needing the root password.'
        - '##'
        - '## Examples are provided at the bottom of the file for collections'
        - '## of related commands, which can then be delegated out to particular'
        ・・・
      - file: etc/sudoers.d/swadmin
        path: /etc/sudoers.d/swadmin
        text:
        - '#########Start/Stop Service###############'
        - Cmnd_Alias SWADMIN_START_SERVICES = /etc/rc.d/init.d/*
        - swadmin ALL=(ALL)NOPASSWD:SWADMIN_START_SERVICES
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
    - role: OS-RHEL9/RH_sudo/OS_build
      VAR_RH_sudo:
      - file: sudo.conf
        path: /etc/sudo.conf
        text:
        - '#'
        - '# Default /etc/sudo.conf file'
        - '#'
        - '# Format:'
        - '#   Plugin plugin_name plugin_path plugin_options ...'
        ・・・
      - file: ''
        path: /etc/sudoers
        text:
        - '## Sudoers allows particular users to run various commands as'
        - '## the root user, without needing the root password.'
        - '##'
        - '## Examples are provided at the bottom of the file for collections'
        - '## of related commands, which can then be delegated out to particular'
        ・・・
      - file: etc/sudoers.d/swadmin
        path: /etc/sudoers.d/swadmin
        text:
        - '#########Start/Stop Service###############'
        - Cmnd_Alias SWADMIN_START_SERVICES = /etc/rc.d/init.d/*
        - swadmin ALL=(ALL)NOPASSWD:SWADMIN_START_SERVICES
        ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_sudo/OS_gathering
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
    │              └── RH_sudo/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_sudo.yml
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
