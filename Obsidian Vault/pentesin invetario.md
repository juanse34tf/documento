Microsoft Windows [Versión 10.0.26100.2161]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\Users\juan sebastian>ssh  linage-admin@38.199.25.20
linage-admin@38.199.25.20's password:
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Fri Mar 13 04:47:36 AM UTC 2026

  System load:  0.0                Processes:              242
  Usage of /:   24.6% of 37.57GB   Users logged in:        1
  Memory usage: 5%                 IPv4 address for ens34: 38.199.25.20
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

6 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


Last login: Fri Mar 13 04:10:52 2026 from 190.242.107.21
linage-admin@inventarios:~$ neofetch
            .-/+oossssoo+/-.               linage-admin@inventarios.linageisp.com
        `:+ssssssssssssssssss+:`           --------------------------------------
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 24.04.4 LTS x86_64
    .ossssssssssssssssssdMMMNysssso.       Host: VMware20,1 None
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 6.8.0-101-generic
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 3 days, 8 hours, 20 mins
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 788 (dpkg)
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.2.21
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Resolution: 1280x800
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Terminal: /dev/pts/2
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: Intel Xeon Gold 5118 (8) @ 2.299GHz
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   GPU: 00:0f.0 VMware SVGA II Adapter
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Memory: 435MiB / 15991MiB
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.

linage-admin@inventarios:~$ sudo pro attach C12gBEbR9uPDxjSM1cP6QmVgLyvUj6
[sudo] password for linage-admin:
Enabling Ubuntu Pro: ESM Apps
Ubuntu Pro: ESM Apps enabled
Enabling Ubuntu Pro: ESM Infra
Ubuntu Pro: ESM Infra enabled
Enabling Livepatch
Livepatch enabled
This machine is now attached to 'Ubuntu Pro - free personal subscription'

SERVICE          ENTITLED  STATUS       DESCRIPTION
anbox-cloud      yes       disabled     Scalable Android in the cloud
esm-apps         yes       enabled      Expanded Security Maintenance for Applications
esm-infra        yes       enabled      Expanded Security Maintenance for Infrastructure
fips-updates     yes       disabled     FIPS compliant crypto packages with stable security updates
landscape        yes       disabled     Management and administration tool for Ubuntu
livepatch        yes       enabled      Canonical Livepatch service
realtime-kernel* yes       disabled     Ubuntu kernel with PREEMPT_RT patches integrated
usg              yes       disabled     Security compliance and audit tools

 * Service has variants

NOTICES
Operation in progress: pro attach

For a list of all Ubuntu Pro services and variants, run 'pro status --all'
Enable services with: pro enable <service>

     Account: juansebastianmunoz799@gmail.com
Subscription: Ubuntu Pro - free personal subscription
linage-admin@inventarios:~$