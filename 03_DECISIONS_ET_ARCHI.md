# [03] DÉCISIONS TECHNIQUES ET ARCHITECTURE

## 1. Le Pont API (Ecriture Mémoire)
- **Fichier** : memory_api.py (Port 8081).
- **Fonctionnement** : Écoute sur 0.0.0.0. Reçoit des requêtes POST avec le token `KALEL_SECRET_2026`. Écrit dans `memory.md`.
- **Accès iPhone** : Via Tailscale (http://100.123.61.123:8081/save_memory) car Cloudflare bloquait les requêtes HTTP (erreurs TLS).

## 2. Les Tunnels (Cloudflare vs Tailscale)
- **Cloudflare** : Utilisé pour le site Taxi et l'API publique. Instable pour les tunnels éphémères (trycloudflare).
- **Tailscale** : Réseau privé. Très fiable pour connecter l'iPhone au serveur Kali. Utilisé pour le raccourci mémoire.

## 3. Validation de la V7.0
- Le patch C7 (lecture des personal_items) est actif.
- La faille de sécurité (Redaction JSON) a été bouchée et validée par OX5 (Maker-Checker).
