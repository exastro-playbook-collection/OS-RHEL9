Ansible Role: OS-RHEL9/RH_user/OS_build
=======================================================
# Description
本ロールは、RHEL9に関するユーザー設定についての情報の設定を行います。

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
OS-RHEL9/RH_user/OS_gatheringロールを利用します。

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
| `VAR_RH_user` | 
| `- user_name` |     ◎     | ユーザー名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`user_id` |     〇     | ユーザーID | 
| &nbsp;&nbsp;&nbsp;&nbsp;`group_id` |     〇     | グループID | 
| &nbsp;&nbsp;&nbsp;&nbsp;`comment` |     〇     | コメント | 
| &nbsp;&nbsp;&nbsp;&nbsp;`home_dir` |     〇     | ホームディレクトリ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`login_shell` |     〇     | ログインシェル名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`password` |     〇     | パスワード | 
| &nbsp;&nbsp;&nbsp;&nbsp;`password_apply` |     〇     | 構築時のパスワード設定の有無<br>true: パスワードの設定を行う<br>false: パスワードの設定を行わない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`action` |     〇     | 構築時の設定<br>present: 作成/更新<br>absent: 削除 | 

### Example
~~~
VAR_RH_user:
- action: present
  comment: create testuser
  group_id: '1100'
  home_dir: /home/testuser
  login_shell: /bin/bash
  password: p@ssw0rd123
  password_apply: true
  user_id: '1100'
  user_name: testuser
- action: present
  comment: update testuser2
  group_id: '1101'
  home_dir: /home/testuser2
  login_shell: /bin/bash
  password_apply: false
  user_id: '1102'
  user_name: testuser2
- action: absent
  user_name: testuser99
  password_apply: false
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
    │         └── RH_user/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      check_parameter.yml
    │                   │      check.yml
    │                   │      main.yml
    │                   │      modify_user.yml
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
    - role: OS-RHEL9/RH_user/OS_build
      VAR_RH_user:
      - action: present
        comment: create testuser
        group_id: '1100'
        home_dir: /home/testuser
        login_shell: /bin/bash
        password: p@ssw0rd123
        password_apply: true
        user_id: '1100'
        user_name: testuser
      - action: present
        comment: update testuser2
        group_id: '1102'
        home_dir: /home/testuser2
        login_shell: /bin/bash
        password_apply: false
        user_id: '1102'
        user_name: testuser2
      - action: absent
        user_name: testuser99
        password_apply: false
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
    - role: OS-RHEL9/RH_user/OS_build
      VAR_RH_user:
      - action: present
        comment: create testuser
        group_id: '1100'
        home_dir: /home/testuser
        login_shell: /bin/bash
        password: p@ssw0rd123
        password_apply: true
        user_id: '1100'
        user_name: testuser
      - action: present
        comment: update testuser2
        group_id: '1102'
        home_dir: /home/testuser2
        login_shell: /bin/bash
        password_apply: false
        user_id: '1102'
        user_name: testuser2
      - action: absent
        user_name: testuser99
        password_apply: false
      ・・・

  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_user/OS_gathering
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
    │              └── RH_user/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_user.yml
~~~

# Remarks
-------
ユーザーを削除する場合、password_apply変数を設定の値に係わらず指定する必要です。

# License
-------

# Copyright
---------
Copyright (c) 2024 NEC Corporation

# Author Information
------------------
NEC Corporation
