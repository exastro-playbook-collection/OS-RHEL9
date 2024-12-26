Ansible Role: OS-RHEL9/RH_ALL/OS_gathering
=======================================================
# Description
本ロールは、RHEL9に関する情報の取得を一括で行います。

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

本ロールでは、<VAR_OS_target_rolename>で定義したパラメータ生成対象のOS_gatheringロールを利用します。
また、パラメータ生成対象のOS_gatheringロールでは、以下のロール、共通部品を利用しています。

- gathering ロール
- パラメータ生成共通部品(parameter_generate)

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に必ず指定しなければならない変数値は、<VAR_OS_target_rolename>の定義によって変動します。
<VAR_OS_target_rolename>で定義したパラメータ生成対象のOS_gatheringロールを確認してください。

## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description |
| ---- | ------------- | ----------- |
| `VAR_OS_gathering_dest_all` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス |
| `VAR_OS_extracting_dest_all` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス |
| `VAR_OS_python_cmd_all` | 'python3' |  Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド |
| `VAR_OS_target_rolename` | (*1) | パラメータ生成対象 |

(*1) 本変数値は収集・パラメータ生成対象とするロールを定義します。
     運用に合わせて対象の追加/削除を行ってください。

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest_all>/<ホスト名/IP>/OS/<VAR_OS_target_rolename>/`

本ロールを既定値で利用した場合、以下のように設定情報を格納します。
格納される情報の詳細は、各パラメータ生成対象のOS_gatheringロールを確認してください。

- 構成は以下のとおり

~~~
 - playbook/
    └── _gathered_data/
         └── 管理対象マシンホスト名 or IPアドレス/
              └── OS/  # OS設定ロール向け専用のフォルダ
                   └── パラメータ生成対象/  # 収集データ
                        │── command/
                        │      ・・・
                        └── file/
                               ・・・
~~~

## 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- `<VAR_extracting_dest_all>/<ホスト名/IP>/OS/<VAR_OS_target_rolename>.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。
格納される情報の詳細は、各パラメータ生成対象のOS_gatheringロールを確認してください。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        パラメータ生成対象.yml  # パラメータ
~~~

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

以下の例では既定値で設定情報収集およびパラメータ生成を行います。

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-RHEL9/RH_ALL/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、各パラメータ生成対象のOS_gatheringロールを確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── パラメータ生成対象/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        パラメータ生成対象.yml  # パラメータ
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
    - role: OS-RHEL9/RH_ALL/OS_build
      VAR_OS_reboot: true
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        パラメータ生成対象.yml  # パラメータ
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
