Ansible Role: OS-RHEL9/RH_networkscripts/OS_build
=======================================================
# Description
本ロールは、RHEL9に関するインタフェース設定についての情報の設定を行います。

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
OS-RHEL9/RH_networkscripts/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_RH_networkscripts` | | 
| `- file` | コピー元ファイル/etc/sysconfig/network-scripts/配下のifcfg-.*ファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/sysconfig/network-scripts/配下のifcfg-.* | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/sysconfig/network-scripts/配下のifcfg-.*ファイルの内容 | 
| `- file` | コピー元ファイル/etc/NetworkManager/system-connections/配下の*.nmconnectionファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/NetworkManager/system-connections/配下の*.nmconnection |
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/NetworkManager/system-connections/配下の*.nmconnectionファイルの内容 | 

### Example
~~~
VAR_RH_networkscripts:
- file: ''
  path: /etc/sysconfig/network-scripts/ifcfg-lo
  text:
  - DEVICE=lo
  - IPADDR=127.0.0.1
  - NETMASK=255.0.0.0
  - NETWORK=127.0.0.0
  - '# If you''re having problems with gated making 127.0.0.0/8 a martian,'
  ・・・
- file: ifcfg-eth0
  path: /etc/sysconfig/network-scripts/ifcfg-eth0
  text:
  - '# Created by cloud-init on instance boot automatically, do not edit.'
  - '#'
  - BOOTPROTO=dhcp
  - DEVICE=eth0
  - HWADDR=00:00:00:00:00:00
  ・・・
- file: ''
  path: /etc/NetworkManager/system-connections/ens192.nmconnection
  text:
  - '[connection]'
  - id=ens192
  - uuid=03286398-3d95-3875-9823-6ea203e69811
  - type=ethernet
  - autoconnect-priority=-999
  - interface-name=ens192
  ・・・
・・・
~~~

~~~
ifcfg-eth0ファイルの内容：
# Created by cloud-init on instance boot automatically, do not edit.
#
BOOTPROTO=dhcp
DEVICE=eth0
HWADDR=00:00:00:00:00:00
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
    │         └── RH_networkscripts/
    │              └── OS_build/
    │                   │── files/
    │                   │      ifcfg-eth0
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
    - role: OS-RHEL9/RH_networkscripts/OS_build
      VAR_RH_networkscripts:
      - file: ''
        path: /etc/sysconfig/network-scripts/ifcfg-lo
        text:
        - DEVICE=lo
        - IPADDR=127.0.0.1
        - NETMASK=255.0.0.0
        - NETWORK=127.0.0.0
        - '# If you''re having problems with gated making 127.0.0.0/8 a martian,'
        ・・・
      - file: ifcfg-eth0
        path: /etc/sysconfig/network-scripts/ifcfg-eth0
        text:
        - '# Created by cloud-init on instance boot automatically, do not edit.'
        - '#'
        - BOOTPROTO=dhcp
        - DEVICE=eth0
        - HWADDR=00:00:00:00:00:00
        ・・・
      - file: ''
        path: /etc/NetworkManager/system-connections/ens192.nmconnection
        text:
        - '[connection]'
        - id=ens192
        - uuid=03286398-3d95-3875-9823-6ea203e69811
        - type=ethernet
        - autoconnect-priority=-999
        - interface-name=ens192
        ・・・
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
    - role: OS-RHEL9/RH_networkscripts/OS_build
      VAR_RH_networkscripts:
      - file: ''
        path: /etc/sysconfig/network-scripts/ifcfg-lo
        text:
        - DEVICE=lo
        - IPADDR=127.0.0.1
        - NETMASK=255.0.0.0
        - NETWORK=127.0.0.0
        - '# If you''re having problems with gated making 127.0.0.0/8 a martian,'
        ・・・
      - file: ifcfg-eth0
        path: /etc/sysconfig/network-scripts/ifcfg-eth0
        text:
        - '# Created by cloud-init on instance boot automatically, do not edit.'
        - '#'
        - BOOTPROTO=dhcp
        - DEVICE=eth0
        - HWADDR=00:00:00:00:00:00
        ・・・
      - file: ''
        path: /etc/NetworkManager/system-connections/ens192.nmconnection
        text:
        - '[connection]'
        - id=ens192
        - uuid=03286398-3d95-3875-9823-6ea203e69811
        - type=ethernet
        - autoconnect-priority=-999
        - interface-name=ens192
        ・・・
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_networkscripts/OS_gathering
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
    │              └── RH_networkscripts/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_networkscripts.yml
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
