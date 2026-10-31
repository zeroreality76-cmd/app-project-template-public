# Baslinje för branchregler

Verifiera stöd och behörighet i målrepositoryt innan någon regel aktiveras.

| Regel | Rekommenderad standard | Undantag |
|---|---|---|
| Direktpush till skyddad branch | Blockera | Dokumenterat incidentförfarande |
| Pull request | Krävs för ändringar | Endast uttryckligt ägarbeslut |
| Oberoende granskning | Krävs vid kod/säkerhetsgräns | Låg-risk dokumentation enligt policy |
| Statuskontroller | Endast verifierade relevanta kontroller | Teknikval saknas eller kontroll trasig |
| Administratörsbypass | Begränsa och logga | Incident med eftergranskning |
