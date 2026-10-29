---
description: What Obsidian, sync tooling and network services exist on the living's hosts is needed, for placing a vault or sync server. It ages; check the date.
---

Witnessed 2026-10-29 on host `ouranos` by flow 2c8b6a; source /home/li/primary/flows/2c8b6a/research/hosts.md (commands recorded there). Cluster nodes other than ouranos are known from cluster data only.

Obsidian on ouranos:
- `which obsidian` finds nothing; it is not in `/run/current-system/sw/bin`, `~/.nix-profile/bin` or the system closure; no flatpak.
- `/nix/store` has no obsidian, syncthing or couchdb entries.
- No vault: `find /home/li -maxdepth 4 -name .obsidian` returned nothing.
- `/home/li/.password-store/Obsidian/ligoldragon.gpg` exists, not decrypted.

Services on ouranos (`systemctl list-units`, `ss -tlnp`):
- Running: headscale (`*:8443`, `*:50443`; server_url `https://ouranos.goldragon.criome:8443`), tailscaled, yggdrasil, strongswan, sshd (port 22), kea-dhcp4, avahi, cups, nix-daemon, lojix, repository-ledger, mpd (127.0.0.1:6600), dolt (127.0.0.1).
- Not present as units: syncthing, couchdb, forgejo, gitea, soft-serve, caddy, nginx, traefik, wireguard.
- Gitolite: user `gitolite` and `/var/lib/gitolite` exist; no daemon, it works over sshd. `repos/CriomOS/modules/nixos/repository-receive.nix:14,190` enables `services.gitolite` for nodes with `GitoliteServer`; ouranos has it.
- No reverse proxy. The only non-loopback listeners are sshd, Headscale (8443, 50443), DNS and mDNS. Reachability from the internet was not tested.

Tailnet (`tailscale status`): ouranos 100.64.0.2, prometheus-1 100.64.0.3, prometheus 100.64.0.1 (offline 230 days). The Headscale controller runs on ouranos, a laptop.

Cluster `goldragon` (`/home/li/primary/repos/goldragon/cluster-definition.datom`): ouranos, prometheus (GMKtec, 128 GB), tiger, zeus, balboa (rock64), VMs mirror-alpha, mirror-beta, vm-testing. A search of the cluster data found no Syncthing, CouchDB, Forgejo, Gitea, soft-serve, Caddy, nginx or WireGuard role.

Phone: Android, from his own words (`flows/01a04e75/vision/listenerWisprFlow.md:3-5`). It is not in the cluster data and not a tailnet node. Model, Android version, and whether an Obsidian mobile app or account is in use are unknown.
