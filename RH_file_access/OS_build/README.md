Ansible Role: OS-RHEL9/RH_file_access/OS_build
=======================================================
# Description
本ロールは、RHEL9に関するファイル設定についての情報の設定を行います。

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
OS-RHEL9/RH_file_access/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  ◎：キーのため変更不可の変数（更新、削除の場合）<br>
  〇：値が変更できる変数<br>

| Name     |  値変更可能 | Description | 
| -------- | :-----------: | ----------- |
| `VAR_RH_file_access` | 
| `- file_path` |     ◎     | ファイルパス | 
| &nbsp;&nbsp;&nbsp;&nbsp;`owner` |     〇     | Owner | 
| &nbsp;&nbsp;&nbsp;&nbsp;`group` |     〇     | Group | 
| &nbsp;&nbsp;&nbsp;&nbsp;`mode` |     〇     | Mode | 
| &nbsp;&nbsp;&nbsp;&nbsp;`symbolic_link` |     〇     | シンボリックリンク | 
| &nbsp;&nbsp;&nbsp;&nbsp;`action` |     〇     | 構築時の設定<br>file: ファイル更新<br>link: シンボリックリンク作成<br>absent: ファイル、シンボリックリンク削除 | 

### Example
~~~
VAR_RH_file_access:
- action: file
  file_path: /home/testuser/new/testupdate.sh
  group: testgroup
  mode: u=rwx,g=rwx,o=rwx
  owner: testuser
- action: link
  file_path: /home/test-user/new/test.sh
  symbolic_link: /home/test-user2/filetest/fileaccess_link
- action: absent
  file_path: /home/test-user/test2.sh
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
    │         └── RH_file_access/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      check_parameter.yml
    │                   │      check.yml
    │                   │      main.yml
    │                   │      modify_file.yml
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
    - role: OS-RHEL9/RH_file_access/OS_build
      VAR_RH_file_access:
      - action: file
        file_path: /home/test-user/new/testupdate.sh
        group: testgroup
        mode: u=rwx,g=rwx,o=rwx
        owner: testuser
      - action: link
        file_path: /home/test-user/new/test.sh
        symbolic_link: /home/test-user2/filetest/fileaccess_link
      - action: absent
        file_path: /home/test-user/test2.sh
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
    - role: OS-RHEL9/RH_file_access/OS_build
      VAR_RH_file_access:
      - action: file
        file_path: /home/test-user/new/testupdate.sh
        group: testgroup
        mode: u=rwx,g=rwx,o=rwx
        owner: testuser
      - action: link
        file_path: /home/test-user/new/test.sh
        symbolic_link: /home/test-user2/filetest/fileaccess_link
      - action: absent
        file_path: /home/test-user/test2.sh
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_file_access/OS_gathering
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
    │              └── RH_file_access/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_file_access.yml
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
