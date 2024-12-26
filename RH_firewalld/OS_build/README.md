Ansible Role: OS-RHEL9/RH_firewalld/OS_build
=======================================================
# Description
本ロールは、RHEL9に関するfirewalld設定についての情報の設定を行います。

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
OS-RHEL9/RH_firewalld/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_RH_firewalld` | | 
| `- file` | コピー元ファイル/etc/firewalld/配下のXMLファイルの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/firewalld/配下の*.xml | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | /etc/firewalld/配下のXMLファイル内容 | 
| `- file` | コピー元ファイルfirewalld.confの情報（ファイル名前またはパス付けファイル名前） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`path` | ファイルパス /etc/firewalld/firewalld.conf | 
| &nbsp;&nbsp;&nbsp;&nbsp;`text` | firewalld.confファイルの内容 | 

### Example
~~~
VAR_RH_firewalld:
- file: public.xml
  path: /etc/firewalld/zones/public.xml
  text:
  - <?xml version="1.0" encoding="utf-8"?>
  - <zone>
  - '  <short>Public</short>'
  - '  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>'
  - '  <service name="ssh"/>'
  ・・・
・・・
~~~

~~~
public.xmlファイルの内容：
<?xml version="1.0" encoding="utf-8"?>
<zone>
  <short>Public</short>
  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>
  <service name="ssh"/>
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
    │         └── RH_firewalld/
    │              └── OS_build/
    │                   │── files/
    │                   │      public.xml
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
    - role: OS-RHEL9/RH_firewalld/OS_build
      VAR_RH_firewalld:
      - file: public.xml
        path: /etc/firewalld/zones/public.xml
        text:
        - <?xml version="1.0" encoding="utf-8"?>
        - <zone>
        - '  <short>Public</short>'
        - '  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>'
        - '  <service name="ssh"/>'
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
    - role: OS-RHEL9/RH_firewalld/OS_build
      VAR_RH_firewalld:
      - file: public.xml
        path: /etc/firewalld/zones/public.xml
        text:
        - <?xml version="1.0" encoding="utf-8"?>
        - <zone>
        - '  <short>Public</short>'
        - '  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>'
        - '  <service name="ssh"/>'
        ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_firewalld/OS_gathering
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
    │              └── RH_firewalld/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        RH_firewalld.yml
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
