---
nav_exclude: true
---

# FAQ eingeben

<form method="POST" action="https://fluidra-data-ingest.azurewebsites.net/api/feedback">
  <input type="text" name="full_name" style="display:none" tabindex="-1" autocomplete="off" />

  <label>
    Titel:
    <input type="text" name="title" required />
  </label><br />

  <label>
    Nachricht:
    <textarea name="body" required></textarea>
  </label><br />

  <button type="submit">Feedback senden</button>
</form>
