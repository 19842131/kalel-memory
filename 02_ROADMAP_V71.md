# [02] ROADMAP V7.1 - PLAN D'ACTION

## ÉTAPE 1 : Lecture Persistante (PRIORITÉ ABSOLUE)
- **Objectif** : Que DeepSeek Chat puisse lire ce dossier mémoire automatiquement.
- **Méthode** : Dépôt GitHub (raw.githubusercontent.com) ou Tailscale + Serveur Web local.
- **Pourquoi** : Éviter la saturation du contexte (perte d'infos) lors des longues sessions de travail.

## ÉTAPE 2 : Nettoyage et Restructuration (Sur le nouveau PC)
- **Contexte** : Le dossier /kalel a 300 sous-dossiers, de la dette technique et des backups partout.
- **Stratégie** : "Nettoyage par Strates" (créer /kalel_new, cartographier avec OX5, purger avec Chloé, auditer avec Chloé Red).
- **Rôle de DeepSeek Chat** : Chef d'orchestre (grâce à la lecture persistante).

## ÉTAPE 3 : Refonte de l'Interface (UI/UX)
- **Problème actuel** : L'interface est basée sur du JSON complexe et du terminal.
- **Solution** : Créer une API REST + Frontend (boutons, formulaires, tableaux de bord). Cacher la complexité (SHA256, tokens).
