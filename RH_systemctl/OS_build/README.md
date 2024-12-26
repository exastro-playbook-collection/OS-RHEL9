Ansible Role: OS-RHEL9/RH_systemctl/OS_build
=======================================================
# Description
本ロールは、RHEL9に関するシステムサービス起動制御についての情報の設定を行います。

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
OS-RHEL9/RH_systemctl/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  ◎：キーのため変更不可の変数<br>
  〇：値が変更できる変数<br>

| Name     |  値変更可能 | Description | 
| -------- | :-----------: | ----------- | 
| `VAR_RH_systemctl` | 
| `- name` |     ◎     | システムサービス名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`status` |     〇     | enabled: ユニットファイルを有効化<br>disabled: ユニットファイルを無効化<br>masked: ユニットファイルを完全無効化<br>masked_off: 完全無効化されているユニットファイルの解除 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`dopreset` |     〇     | ユニットファイルのプリセットの設定<br>true: 設定を行う<br>false: 設定を行わない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`action` |     〇     | 構築時の設定<br>true: 設定を行う<br>false: 設定を行わない | 

### Example
~~~
VAR_RH_systemctl:
- action: 'true'
  name: httpd.service
  dopreset: 'true'
  status: disabled
- action: 'false'
  name: kdump.service
  dopreset: 'false'
  status: enabled
- action: 'false'
  name: sssd.service
  dopreset: 'false'
  status: masked
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
    │         └── RH_systemctl/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      check_parameter.yml
    │                   │      check.yml
    │                   │      main.yml
    │                   │      modify_exe.yml
    │                   │      modify_systemctl.yml
    │                   │      modify.yml
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
    - role: OS-RHEL9/RH_systemctl/OS_build
      VAR_RH_systemctl:
      - action: 'true'
        name: httpd.service
        dopreset: 'true'
        status: disabled
      - action: 'false'
        name: kdump.service
        dopreset: 'false'
        status: enabled
      - action: 'false'
        name: sssd.service
        dopreset: 'false'
        status: masked
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
    - role: OS-RHEL9/RH_systemctl/OS_build
      VAR_RH_systemctl:
      - action: 'true'
        name: httpd.service
        dopreset: 'true'
        status: disabled
      - action: 'false'
        name: kdump.service
        dopreset: 'false'
        status: enabled
      - action: 'false'
        name: sssd.service
        dopreset: 'false'
        status: masked
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_systemctl/OS_gathering
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
    │              └── RH_systemctl/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_systemctl.yml
~~~

# Remarks
-------
完全無効化されているユニットファイルの解除は、ユニットファイルが完全無効化されている場合のみ実施されます。
ユニットファイルをプリセットすると、ユニットファイルの状態はプリセットの値に設定します。

# License
-------

# Copyright
---------
Copyright (c) 2024 NEC Corporation

# Author Information
------------------
NEC Corporation
