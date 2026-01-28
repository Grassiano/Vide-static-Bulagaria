const express = require('express');
const path = require('path');
const app = express();

const port = process.env.PORT || 3000;

// #region agent log - DEBUG VERSION IDENTIFIER
const DEPLOY_VERSION = "BULGARIA-v2-2026-01-28 20:06:06";
console.log("=== SERVER STARTING ===");
console.log("DEPLOY_VERSION:", DEPLOY_VERSION);
console.log("LANGUAGE: BULGARIAN");
// #endregion

// Debug endpoint to check which version is deployed
app.get('/debug-version', (req, res) => {
    res.json({
        version: DEPLOY_VERSION,
        language: "BULGARIAN",
        timestamp: "2026-01-28 20:06:06",
        message: "This is the CORRECT Bulgaria deployment"
    });
});

// Serve static files from the 'public/videprints.com' directory
const siteRoot = path.join(__dirname, 'public/videprints.com');

app.use(express.static(siteRoot));

// Fallback to index.html for root
app.get('/', (req, res) => {
    console.log("Serving index.html for /");
    res.sendFile(path.join(siteRoot, 'index.html'));
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
    console.log(`Serving static files from: ${siteRoot}`);
    console.log(`DEPLOY_VERSION: ${DEPLOY_VERSION}`);
});
