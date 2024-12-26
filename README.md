OS-RHEL9
===============================
# Trademarks
-----------
* Linuxは、Linus Torvalds氏の米国およびその他の国における登録商標または商標です。
* RedHat、RHEL、CentOSは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* Windows、PowerShell、IIS、.NET Frameworkは、Microsoft Corporation の米国およびその他の国における登録商標または商標です。
* Ansibleは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* pythonは、Python Software Foundationの登録商標または商標です。
* NECは、日本電気株式会社の登録商標または商標です。
* その他、本ロールのコード、ファイルに記載されている会社名および製品名は、各社の登録商標または商標です。

# Description
-----------
RHEL9に関する情報の収集および設定を行うためのロールを提供します。
情報の収集は、OS_gatheringロールを使って収集を行います。情報の設定は、OS_buildロールを使って設定を行います。
OS_gatheringで収集結果情報として出力されるyamlファイルのパラメタを編集し、OS_buildロールの設定情報として利用できます。
ソフトウェア製品向けロールと異なり、利用者が設定時に必要となるロールを適宜選択して設定を行ってください。
またOS全ての情報設定を行う事ができるわけではありませんので、設定に必要となるロールが提供されていない場合は、自作することをご検討ください。

-------------

## 注意
OS関連のロール利用は、パラメータ内容を十分に確認し、事前評価を行ってからご利用ください。パラメータ値が誤っていると、ターゲットマシンへのアクセスができなくなるなど、トラブルが発生する可能性があります。

-------------

# Specification

## Ansibleサーバ

* Ansible バージョン 2.11 以上 (動作確認バージョン [core 2.11.12])
* Python バージョン 3.x  (動作確認バージョン 3.6.8)

# OS用ロールを使うまでの前準備
OS用ロールを利用する前に、ターゲットマシン(管理対象サーバ)へ事前に実施してください。

RHELサーバは、OSのインストール後、以下の設定を実施してください。（sshはデフォルトで動作している前提です）

* Ansible サーバと接続するネットワークの設定
* Ansibleがアクセスする、管理者権限のあるユーザーアカウントの作成


# 提供ロール一覧
## 情報取得ロール一覧
情報の取得に使用する以下のロールを提供します。

| ロール名 | Description | 
| ------- | ----------- | 
| [RH_ALL/OS_gathering](RH_ALL/OS_gathering) | OS情報一括取得 | 
| [RH_chrony/OS_gathering](RH_chrony/OS_gathering) | 時刻同期設定 | 
| [RH_cron/OS_gathering](RH_cron/OS_gathering) | 定期自動ジョブ基本設定 | 
| [RH_cronconf/OS_gathering](RH_cronconf/OS_gathering) | 定期自動ジョブスケジュール設定 | 
| [RH_default_target/OS_gathering](RH_default_target/OS_gathering) | デフォルトターゲットの設定 | 
| [RH_directory/OS_gathering](RH_directory/OS_gathering) | ディレクトリ設定 | 
| [RH_file_access/OS_gathering](RH_file_access/OS_gathering) | ファイル設定 | 
| [RH_firewalld/OS_gathering](RH_firewalld/OS_gathering) | firewalld設定 | 
| [RH_fstab/OS_gathering](RH_fstab/OS_gathering) | ファイルシステム マウント設定 | 
| [RH_group/OS_gathering](RH_group/OS_gathering) | グループ設定 | 
| [RH_grub2/OS_gathering](RH_grub2/OS_gathering) | ブートローダー設定 | 
| [RH_hostname/OS_gathering](RH_hostname/OS_gathering) | ホスト名設定 | 
| [RH_hosts/OS_gathering](RH_hosts/OS_gathering) | hosts設定 | 
| [RH_hosts_allow_deny/OS_gathering](RH_hosts_allow_deny/OS_gathering) | アクセス制限(許可/拒否) | 
| [RH_init/OS_gathering](RH_init/OS_gathering) | ブートプロセスシステム表示機能設定 | 
| [RH_initfunc/OS_gathering](RH_initfunc/OS_gathering) | 起動スクリプト関数 | 
| [RH_inittab/OS_gathering](RH_inittab/OS_gathering) | 起動、LANレベル設定 | 
| [RH_kdump/OS_gathering](RH_kdump/OS_gathering) | カーネルダンプ設定 | 
| [RH_limits/OS_gathering](RH_limits/OS_gathering) | リソース制限設定 | 
| [RH_logrotate/OS_gathering](RH_logrotate/OS_gathering) | ログローテーション設定 | 
| [RH_logwatch/OS_gathering](RH_logwatch/OS_gathering) | ログ監視設定 | 
| [RH_mptcpd/OS_gathering](RH_mptcpd/OS_gathering) | mptcpd サービス設定 | 
| [RH_networkscripts/OS_gathering](RH_networkscripts/OS_gathering) | インタフェース設定 | 
| [RH_nftables/OS_gathering](RH_nftables/OS_gathering) | パケットフィルタルール | 
| [RH_nsswitch/OS_gathering](RH_nsswitch/OS_gathering) | ネームサービススイッチ設定 | 
| [RH_pam/OS_gathering](RH_pam/OS_gathering) | パスワード設定 | 
| [RH_postfix/OS_gathering](RH_postfix/OS_gathering) | postfix設定 | 
| [RH_profile/OS_gathering](RH_profile/OS_gathering) | ユーザー環境 bash、csh | 
| [RH_profile_all/OS_gathering](RH_profile_all/OS_gathering) | 全ユーザー共通設定(環境変数など) | 
| [RH_resolv/OS_gathering](RH_resolv/OS_gathering) | リゾルバ設定 | 
| [RH_rpm/OS_gathering](RH_rpm/OS_gathering) | パッケージインストール | 
| [RH_rsyslog/OS_gathering](RH_rsyslog/OS_gathering) | アプリケーション通知メッセージログ設定 | 
| [RH_securetty/OS_gathering](RH_securetty/OS_gathering) | rootログイン制御設定 | 
| [RH_selinux/OS_gathering](RH_selinux/OS_gathering) | SeLinux設定 | 
| [RH_services/OS_gathering](RH_services/OS_gathering) | インターネットネットワーク設定 | 
| [RH_sshd_config/OS_gathering](RH_sshd_config/OS_gathering) | sshデーモン接続設定 | 
| [RH_ssh_config/OS_gathering](RH_ssh_config/OS_gathering) | sshクライアント接続設定 | 
| [RH_sudo/OS_gathering](RH_sudo/OS_gathering) | sudo設定 | 
| [RH_sysctl/OS_gathering](RH_sysctl/OS_gathering) | カーネルパラメータ設定 | 
| [RH_systemctl/OS_gathering](RH_systemctl/OS_gathering) | システムサービス起動制御 | 
| [RH_systemd/OS_gathering](RH_systemd/OS_gathering) | サービス管理設定 | 
| [RH_udev_rules/OS_gathering](RH_udev_rules/OS_gathering) | デバイスルール設定 | 
| [RH_user/OS_gathering](RH_user/OS_gathering) | ユーザー設定 | 
| [RH_vsftpd/OS_gathering](RH_vsftpd/OS_gathering) | FTP設定 | 
| [RH_vsftpd_user/OS_gathering](RH_vsftpd_user/OS_gathering) | FTPユーザー設定 | 

## 情報取得ロールのマニュアル一覧
各ロールで情報取得可能なパラメータは、以下の各ロールのマニュアル内のResultセクションに記載されたものとなります。

| 情報取得ロールのマニュアル | 
| ------- |  
| [RH_chrony/OS_gathering マニュアル](RH_chrony/OS_gathering/README.md) |
| [RH_cron/OS_gathering マニュアル](RH_cron/OS_gathering/README.md) |
| [RH_cronconf/OS_gathering マニュアル](RH_cronconf/OS_gathering/README.md) |
| [RH_default_target/OS_gathering マニュアル](RH_default_target/OS_gathering/README.md) |
| [RH_directory/OS_gathering マニュアル](RH_directory/OS_gathering/README.md) |
| [RH_file_access/OS_gathering マニュアル](RH_file_access/OS_gathering/README.md) |
| [RH_firewalld/OS_gathering マニュアル](RH_firewalld/OS_gathering/README.md) |
| [RH_fstab/OS_gathering マニュアル](RH_fstab/OS_gathering/README.md) |
| [RH_group/OS_gathering マニュアル](RH_group/OS_gathering/README.md) |
| [RH_grub2/OS_gathering マニュアル](RH_grub2/OS_gathering/README.md) |
| [RH_hostname/OS_gathering マニュアル](RH_hostname/OS_gathering/README.md) |
| [RH_hosts/OS_gathering マニュアル](RH_hosts/OS_gathering/README.md) |
| [RH_hosts_allow_deny/OS_gathering マニュアル](RH_hosts_allow_deny/OS_gathering/README.md) |
| [RH_init/OS_gathering マニュアル](RH_init/OS_gathering/README.md) |
| [RH_initfunc/OS_gathering マニュアル](RH_initfunc/OS_gathering/README.md) |
| [RH_inittab/OS_gathering マニュアル](RH_inittab/OS_gathering/README.md) |
| [RH_kdump/OS_gathering マニュアル](RH_kdump/OS_gathering/README.md) |
| [RH_limits/OS_gathering マニュアル](RH_limits/OS_gathering/README.md) |
| [RH_logrotate/OS_gathering マニュアル](RH_logrotate/OS_gathering/README.md) |
| [RH_logwatch/OS_gathering マニュアル](RH_logwatch/OS_gathering/README.md) |
| [RH_mptcpd/OS_gathering マニュアル](RH_mptcpd/OS_gathering/README.md) |
| [RH_networkscripts/OS_gathering マニュアル](RH_networkscripts/OS_gathering/README.md) |
| [RH_nftables/OS_gathering マニュアル](RH_nftables/OS_gathering/README.md) |
| [RH_nsswitch/OS_gathering マニュアル](RH_nsswitch/OS_gathering/README.md) |
| [RH_pam/OS_gathering マニュアル](RH_pam/OS_gathering/README.md) |
| [RH_postfix/OS_gathering マニュアル](RH_postfix/OS_gathering/README.md) |
| [RH_profile/OS_gathering マニュアル](RH_profile/OS_gathering/README.md) |
| [RH_profile_all/OS_gathering マニュアル](RH_profile_all/OS_gathering/README.md) |
| [RH_resolv/OS_gathering マニュアル](RH_resolv/OS_gathering/README.md) |
| [RH_rpm/OS_gathering マニュアル](RH_rpm/OS_gathering/README.md) |
| [RH_rsyslog/OS_gathering マニュアル](RH_rsyslog/OS_gathering/README.md) |
| [RH_securetty/OS_gathering マニュアル](RH_securetty/OS_gathering/README.md) |
| [RH_selinux/OS_gathering マニュアル](RH_selinux/OS_gathering/README.md) |
| [RH_services/OS_gathering マニュアル](RH_services/OS_gathering/README.md) |
| [RH_sshd_config/OS_gathering マニュアル](RH_sshd_config/OS_gathering/README.md) |
| [RH_ssh_config/OS_gathering マニュアル](RH_ssh_config/OS_gathering/README.md) |
| [RH_sudo/OS_gathering マニュアル](RH_sudo/OS_gathering/README.md) |
| [RH_sysctl/OS_gathering マニュアル](RH_sysctl/OS_gathering/README.md) |
| [RH_systemctl/OS_gathering マニュアル](RH_systemctl/OS_gathering/README.md) |
| [RH_systemd/OS_gathering マニュアル](RH_systemd/OS_gathering/README.md) |
| [RH_udev_rules/OS_gathering マニュアル](RH_udev_rules/OS_gathering/README.md) |
| [RH_user/OS_gathering マニュアル](RH_user/OS_gathering/README.md) |
| [RH_vsftpd/OS_gathering マニュアル](RH_vsftpd/OS_gathering/README.md) |
| [RH_vsftpd_user/OS_gathering マニュアル](RH_vsftpd_user/OS_gathering/README.md) |


## RH_ALL/OS_gathering(OS情報一括取得)の情報取得ロール確認方法
RH_ALL/OS_gathering(OS情報一括取得)ロールで情報取得を行うデフォルトのロールは、下記ファイルのコメントされていないロールとなります。

| ファイル名                            |
| ----------------------------------- |
| [RH_ALL/OS_gathering/defaults/main.yml](RH_ALL/OS_gathering/defaults/main.yml) |

## 情報設定ロール一覧
情報の設定に使用する以下のロールを提供します。

| ロール名                            | Description                      | 
| ----------------------------------- | -------------------------------- | 
| [RH_ALL/OS_build](RH_ALL/OS_build) | OS情報一括設定 | 
| [RH_chrony/OS_build](RH_chrony/OS_build) | 時刻同期設定 | 
| [RH_cron/OS_build](RH_cron/OS_build) | 定期自動ジョブ基本設定 | 
| [RH_cronconf/OS_build](RH_cronconf/OS_build) | 定期自動ジョブスケジュール設定 | 
| [RH_default_target/OS_build](RH_default_target/OS_build) | デフォルトターゲットの設定 | 
| [RH_directory/OS_build](RH_directory/OS_build) | ディレクトリ設定 | 
| [RH_file_access/OS_build](RH_file_access/OS_build) | ファイル設定 | 
| [RH_firewalld/OS_build](RH_firewalld/OS_build) | firewalld設定 | 
| [RH_fstab/OS_build](RH_fstab/OS_build) | ファイルシステム マウント設定 | 
| [RH_group/OS_build](RH_group/OS_build) | グループ設定 | 
| [RH_grub2/OS_build](RH_grub2/OS_build) | ブートローダー設定 | 
| [RH_hostname/OS_build](RH_hostname/OS_build) | ホスト名設定 | 
| [RH_hosts/OS_build](RH_hosts/OS_build) | hosts設定 | 
| [RH_hosts_allow_deny/OS_build](RH_hosts_allow_deny/OS_build) | アクセス制限(許可/拒否) | 
| [RH_init/OS_build](RH_init/OS_build) | ブートプロセスシステム表示機能設定 | 
| [RH_initfunc/OS_build](RH_initfunc/OS_build) | 起動スクリプト関数 | 
| [RH_inittab/OS_build](RH_inittab/OS_build) | 起動、LANレベル設定 | 
| [RH_kdump/OS_build](RH_kdump/OS_build) | カーネルダンプ設定 | 
| [RH_limits/OS_build](RH_limits/OS_build) | リソース制限設定 | 
| [RH_logrotate/OS_build](RH_logrotate/OS_build) | ログローテーション設定 | 
| [RH_logwatch/OS_build](RH_logwatch/OS_build) | ログ監視設定 | 
| [RH_mptcpd/OS_build](RH_mptcpd/OS_build) | mptcpd サービス設定 | 
| [RH_networkscripts/OS_build](RH_networkscripts/OS_build) | インタフェース設定 | 
| [RH_nftables/OS_build](RH_nftables/OS_build) | パケットフィルタルール | 
| [RH_nsswitch/OS_build](RH_nsswitch/OS_build) | ネームサービススイッチ設定 | 
| [RH_pam/OS_build](RH_pam/OS_build) | パスワード設定 | 
| [RH_postfix/OS_build](RH_postfix/OS_build) | postfix設定 | 
| [RH_profile/OS_build](RH_profile/OS_build) | ユーザー環境 bash、csh | 
| [RH_profile_all/OS_build](RH_profile_all/OS_build) | 全ユーザー共通設定(環境変数など) | 
| [RH_reboot/OS_build](RH_reboot/OS_build) | OSの再起動、シャットダウン、サービスの再起動およびsysctl読み込むファイルの設定 | 
| [RH_resolv/OS_build](RH_resolv/OS_build) | リゾルバ設定 | 
| [RH_rpm/OS_build](RH_rpm/OS_build) | パッケージインストール | 
| [RH_rsyslog/OS_build](RH_rsyslog/OS_build) | アプリケーション通知メッセージログ設定 | 
| [RH_securetty/OS_build](RH_securetty/OS_build) | rootログイン制御設定 | 
| [RH_selinux/OS_build](RH_selinux/OS_build) | SeLinux設定 | 
| [RH_services/OS_build](RH_services/OS_build) | インターネットネットワーク設定 | 
| [RH_sshd_config/OS_build](RH_sshd_config/OS_build) | sshデーモン接続設定 | 
| [RH_ssh_config/OS_build](RH_ssh_config/OS_build) | sshクライアント接続設定 | 
| [RH_sudo/OS_build](RH_sudo/OS_build) | sudo設定 | 
| [RH_sysctl/OS_build](RH_sysctl/OS_build) | カーネルパラメータ設定 | 
| [RH_systemctl/OS_build](RH_systemctl/OS_build) | システムサービス起動制御 | 
| [RH_systemd/OS_build](RH_systemd/OS_build) | サービス管理設定 | 
| [RH_udev_rules/OS_build](RH_udev_rules/OS_build) | デバイスルール設定 | 
| [RH_user/OS_build](RH_user/OS_build) | ユーザー設定 | 
| [RH_vsftpd/OS_build](RH_vsftpd/OS_build) | FTP設定 | 
| [RH_vsftpd_user/OS_build](RH_vsftpd_user/OS_build) | FTPユーザー設定 | 

## 情報設定ロールのマニュアル一覧
各ロールで情報設定可能なパラメータは、以下の各ロールのマニュアル内のRole Variablesセクションに記載されたものとなります。

| 情報設定ロールのマニュアル | 
| ------- |  
| [RH_chrony/OS_build マニュアル](RH_chrony/OS_build/README.md) |
| [RH_cron/OS_build マニュアル](RH_cron/OS_build/README.md) |
| [RH_cronconf/OS_build マニュアル](RH_cronconf/OS_build/README.md) |
| [RH_default_target/OS_build マニュアル](RH_default_target/OS_build/README.md) |
| [RH_directory/OS_build マニュアル](RH_directory/OS_build/README.md) |
| [RH_file_access/OS_build マニュアル](RH_file_access/OS_build/README.md) |
| [RH_firewalld/OS_build マニュアル](RH_firewalld/OS_build/README.md) |
| [RH_fstab/OS_build マニュアル](RH_fstab/OS_build/README.md) |
| [RH_group/OS_build マニュアル](RH_group/OS_build/README.md) |
| [RH_grub2/OS_build マニュアル](RH_grub2/OS_build/README.md) |
| [RH_hostname/OS_build マニュアル](RH_hostname/OS_build/README.md) |
| [RH_hosts/OS_build マニュアル](RH_hosts/OS_build/README.md) |
| [RH_hosts_allow_deny/OS_build マニュアル](RH_hosts_allow_deny/OS_build/README.md) |
| [RH_init/OS_build マニュアル](RH_init/OS_build/README.md) |
| [RH_initfunc/OS_build マニュアル](RH_initfunc/OS_build/README.md) |
| [RH_inittab/OS_build マニュアル](RH_inittab/OS_build/README.md) |
| [RH_kdump/OS_build マニュアル](RH_kdump/OS_build/README.md) |
| [RH_limits/OS_build マニュアル](RH_limits/OS_build/README.md) |
| [RH_logrotate/OS_build マニュアル](RH_logrotate/OS_build/README.md) |
| [RH_logwatch/OS_build マニュアル](RH_logwatch/OS_build/README.md) |
| [RH_mptcpd/OS_build マニュアル](RH_mptcpd/OS_build/README.md) |
| [RH_networkscripts/OS_build マニュアル](RH_networkscripts/OS_build/README.md) |
| [RH_nftables/OS_build マニュアル](RH_nftables/OS_build/README.md) |
| [RH_nsswitch/OS_build マニュアル](RH_nsswitch/OS_build/README.md) |
| [RH_pam/OS_build マニュアル](RH_pam/OS_build/README.md) |
| [RH_postfix/OS_build マニュアル](RH_postfix/OS_build/README.md) |
| [RH_profile/OS_build マニュアル](RH_profile/OS_build/README.md) |
| [RH_profile_all/OS_build マニュアル](RH_profile_all/OS_build/README.md) |
| [RH_reboot/OS_build マニュアル](RH_reboot/OS_build/README.md) |
| [RH_resolv/OS_build マニュアル](RH_resolv/OS_build/README.md) |
| [RH_rpm/OS_build マニュアル](RH_rpm/OS_build/README.md) |
| [RH_rsyslog/OS_build マニュアル](RH_rsyslog/OS_build/README.md) |
| [RH_securetty/OS_build マニュアル](RH_securetty/OS_build/README.md) |
| [RH_selinux/OS_build マニュアル](RH_selinux/OS_build/README.md) |
| [RH_services/OS_build マニュアル](RH_services/OS_build/README.md) |
| [RH_sshd_config/OS_build マニュアル](RH_sshd_config/OS_build/README.md) |
| [RH_ssh_config/OS_build マニュアル](RH_ssh_config/OS_build/README.md) |
| [RH_sudo/OS_build マニュアル](RH_sudo/OS_build/README.md) |
| [RH_sysctl/OS_build マニュアル](RH_sysctl/OS_build/README.md) |
| [RH_systemctl/OS_build マニュアル](RH_systemctl/OS_build/README.md) |
| [RH_systemd/OS_build マニュアル](RH_systemd/OS_build/README.md) |
| [RH_udev_rules/OS_build マニュアル](RH_udev_rules/OS_build/README.md) |
| [RH_user/OS_build マニュアル](RH_user/OS_build/README.md) |
| [RH_vsftpd/OS_build マニュアル](RH_vsftpd/OS_build/README.md) |
| [RH_vsftpd_user/OS_build マニュアル](RH_vsftpd_user/OS_build/README.md) |

## RH_ALL/OS_build(OS情報一括設定)の情報設定ロール確認方法
RH_ALL/OS_build(OS情報一括設定)ロールで情報設定を行うデフォルトのロールは、下記ファイルのコメントされていないロールとなります。

| ファイル名                            |
| ----------------------------------- |
| [RH_ALL/OS_build/defaults/main.yml](RH_ALL/OS_build/defaults/main.yml) |

# Remarks
-------
OS仕様に依存する情報の設定ロールでは、実行は成功するが設定したパラメタが反映されない場合があります。

# License
-------

# Copyright
---------
Copyright (c) 2024 NEC Corporation

# Author Information
------------------
NEC Corporation
