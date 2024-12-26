Ansible Role: OS-RHEL9/RH_vsftpd/OS_build
=======================================================
# Description
本ロールは、RHEL9に関するFTP設定についての情報の設定を行います。

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
OS-RHEL9/RH_vsftpd/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_RH_vsftpd` | | 
| `- file` | コピー元ファイルvsftpd.confの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/vsftpd/vsftpd.conf | 
| &nbsp;&nbsp;&nbsp;&nbsp;`properties` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`プロパティ名：設定値` | プロパティ名<br>設定値 |  

※ FTP設定の情報を設定、変更した場合、ftpデーモンが再起動されます。

### Example
~~~
VAR_RH_vsftpd:
- file: vsftpd.conf
  path: /etc/vsftpd/vsftpd.conf
  properties:
    anonymous_enable: 'NO'
    connect_from_port_20: 'YES'
    dirmessage_enable: 'YES'
    listen: 'NO'
    listen_ipv6: 'YES'
    ・・・
~~~

~~~
vsftpd.confファイルの内容：
# Example config file /etc/vsftpd/vsftpd.conf
#
# The default compiled in settings are fairly paranoid. This sample file
# loosens things up a bit, to make the ftp daemon more usable.
# Please see vsftpd.conf.5 for all compiled in defaults.
#
# READ THIS: This example file is NOT an exhaustive list of vsftpd options.
# Please read the vsftpd.conf.5 manual page to get a full idea of vsftpd's
# capabilities.
#
# Allow anonymous FTP? (Beware - allowed by default if you comment this out).
anonymous_enable=NO
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
    │         └── RH_vsftpd/
    │              └── OS_build/
    │                   │── files/
    │                   │      vsftpd.conf
    │                   │── tasks/
    │                   │      main.yml
    │                   │      modify_property.yml
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
    - role: OS-RHEL9/RH_vsftpd/OS_build
      VAR_RH_vsftpd:
      - file: vsftpd.conf
        path: /etc/vsftpd/vsftpd.conf
        properties:
          anonymous_enable: 'NO'
          connect_from_port_20: 'YES'
          dirmessage_enable: 'YES'
          listen: 'NO'
          listen_ipv6: 'YES'
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
    - role: OS-RHEL9/RH_vsftpd/OS_build
      VAR_RH_vsftpd:
      - file: vsftpd.conf
        path: /etc/vsftpd/vsftpd.conf
        properties:
          anonymous_enable: 'NO'
          connect_from_port_20: 'YES'
          dirmessage_enable: 'YES'
          listen: 'NO'
          listen_ipv6: 'YES'
          ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_vsftpd/OS_gathering
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
    │              └── RH_vsftpd/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_vsftpd.yml
~~~

# Remarks
-------
パラメータfileが下記のいずれかを満たす場合、設定したpropertiesを利用して構築ロールを実行します。さらに、収集データから変更不要な設定値を削除して構築ロールを実行することが必要です。
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
