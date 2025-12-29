const fs = require('fs');
const path = require('path');

const publicDir = './public';
const siteDir = path.join(publicDir, 'videprints.com');

// 1. Flatten Structure: Move everything from public/videprints.com to public/
function moveFiles(src, dest) {
    if (!fs.existsSync(src)) return;
    const items = fs.readdirSync(src);
    items.forEach(item => {
        const srcPath = path.join(src, item);
        const destPath = path.join(dest, item);
        // If destination exists and is a directory, merge? For now just move.
        fs.renameSync(srcPath, destPath);
    });
    // Clean up empty dir
    fs.rmdirSync(src);
}

// 2. Fix URLs and Content
function fixContent(dir) {
    if (!fs.existsSync(dir)) return;
    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            fixContent(filePath);
        } else if (file.endsWith('.html')) {
            let content = fs.readFileSync(filePath, 'utf8');

            // Fix protocol-relative URLs
            content = content.replace(/srcset="\/\//g, 'srcset="https://');
            content = content.replace(/src="\/\//g, 'src="https://');
            content = content.replace(/href="\/\//g, 'href="https://');

            // Update WhatsApp link
            // Capture any generic wa.me or api.whatsapp link and replace
            // Old: api.whatsapp.com/message/KCJVQNJ7NGTYO1...
            // New: wa.me/972546492267
            const waRegex = /Data-WhatsApp="[^"]*"/g; // If used in data attributes
            const waLinkRegex = /href="https:\/\/api\.whatsapp\.com\/[^"]*"/g;

            content = content.replace(waLinkRegex, 'href="https://wa.me/972546492267"');

            // Also look for just the number if it's in text or other attributes?
            // User said: "דברו איתנו בווטאספ צריך להוביל לשיחה למספר +972546492267"

            // Update Email
            // Old: info@videprints.com (maybe?)
            // New: support@videprints.com
            content = content.replace(/mailto:[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+/g, 'mailto:support@videprints.com');

            fs.writeFileSync(filePath, content, 'utf8');
        }
    });
}

// Wait for scrape to finish (manual run)
if (fs.existsSync(siteDir)) {
    console.log('Flattening directory structure...');
    moveFiles(siteDir, publicDir);
}

console.log('Fixing URLs and Contact Info...');
fixContent(publicDir);
console.log('Done.');
