# Publishing the Farm Tracker as an installable app

The app is a PWA: once it is on an https web address, anyone can open the link and click **Install**.
Files that must be published together (keep this structure):

```
index.html
manifest.webmanifest
sw.js
icons/icon-192.png  icons/icon-512.png  icons/icon.svg
```

## Option A – Netlify Drop (no account setup, ~2 minutes)
1. Put the files above in one folder on your computer.
2. Go to https://app.netlify.com/drop and drag the folder onto the page.
3. You get a link like `https://something.netlify.app`. Send it to your client.

## Option B – GitHub Pages (use a NEW, separate repository)
1. Create a new repository (for example `farm-tracker-app`) and upload the files to its root.
2. Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
3. After a minute the app is at `https://<your-username>.github.io/farm-tracker-app/`.
   (Do not publish from the hospital `lcrh-erp` repository.)

## How your client installs it
- **Windows / Mac (Chrome or Edge):** open the link, click **Install app** (top right of the page) or the install icon in the address bar.
- **Android (Chrome):** open the link, tap **Install app**, or menu (⋮) > **Install app**.
- **iPhone (Safari):** open the link, tap Share > **Add to Home Screen**.

## Publishing an update later
Change `VERSION` at the top of `sw.js` (for example `farm-tracker-v2`) and re-upload all files. Clients get the new version the next time they open the app online. Their saved data is not affected.

## Remember
Each user's data is stored on their own device. Tell clients to use **Backup & Settings > Export backup** regularly.
