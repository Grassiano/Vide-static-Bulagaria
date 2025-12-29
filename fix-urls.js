const fs = require('fs');
const path = require('path');

const directory = './public';

function fixFiles(dir) {
    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            fixFiles(filePath);
        } else if (file.endsWith('.html')) {
            let content = fs.readFileSync(filePath, 'utf8');

            // Fix protocol-relative URLs
            content = content.replace(/srcset="\/\//g, 'srcset="https://');
            content = content.replace(/src="\/\//g, 'src="https://');
            content = content.replace(/href="\/\//g, 'href="https://');

            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`Fixed URLs in: ${filePath}`);
        }
    });
}

fixFiles(directory);
console.log('Done fixing URLs.');
