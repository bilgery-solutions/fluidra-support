---
nav_exclude: true
---

# FAQ eingeben

<form method="POST" action="https://fluidra-data-ingest.azurewebsites.net/api/feedback"
    style="max-width: 100%;padding: 1.5rem;border-radius: 10px;box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <input type="text" name="full_name" style="display:none" tabindex="-1" autocomplete="off" />
    <h2 style="margin-top: 0;">Titel<h2>
    <input type="text" name="title" required style="width:100%;border: 1px solid #ccc;border-radius:10px;"/>
    <br />
    <h2 style="margin-top: 0;">Inhalt<h2>
    <textarea name="body" rows="5" required style="width:100%;border: 1px solid #ccc;border-radius:10px;"></textarea>
    <br />
    <br />
    <button type="submit" style="display: inline-block;padding: 0.75rem 1.25rem;background-color: #001971;color: white;text-decoration: none;border-radius: 8px;font-weight: 600;">Senden</button>
</form>
