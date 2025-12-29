const express = require('express');
const path = require('path');
const app = express();

const port = process.env.PORT || 3000;

// Serve static files from the 'public/videprints.com' directory
// This is because the scraper created a domain folder inside public
const siteRoot = path.join(__dirname, 'public/videprints.com');

app.use(express.static(siteRoot));

// Fallback to index.html for root
app.get('/', (req, res) => {
    res.sendFile(path.join(siteRoot, 'index.html'));
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
    console.log(`Serving static files from: ${siteRoot}`);
});
