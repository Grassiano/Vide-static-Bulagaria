const scrape = require('website-scraper');

const options = {
    urls: [
        'https://videprints.com/',
        'https://videprints.com/pages/events',
        'https://videprints.com/pages/about-us',
        'https://videprints.com/pages/contact',
        'https://videprints.com/pages/events-form',
        'https://videprints.com/policies/terms-of-service',
        'https://videprints.com/policies/privacy-policy',
        'https://videprints.com/pages/%D7%A9%D7%90%D7%9C%D7%95%D7%AA-%D7%AA%D7%A9%D7%95%D7%91%D7%95%D7%AA', // FAQ
        'https://videprints.com/pages/%D7%AA%D7%A7%D7%A0%D7%95%D7%9F-%D7%94%D7%92%D7%A8%D7%9C%D7%94' // Raffle
    ],
    directory: './public',
    sources: [
        { selector: 'img', attr: 'src' },
        { selector: 'img', attr: 'srcset' },
        { selector: 'link[rel="stylesheet"]', attr: 'href' },
        { selector: 'script', attr: 'src' },
        { selector: 'video', attr: 'src' },
        { selector: 'source', attr: 'src' }
    ],
    recursive: true,
    maxDepth: 3,
    prettifyUrls: true,
    filenameGenerator: 'bySiteStructure',
    request: {
        headers: {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    }
};

console.log('Starting FINAL scrape of videprints.com...');
scrape(options).then((result) => {
    console.log('Website successfully downloaded to ./public');
}).catch((err) => {
    console.error('Error downloading website:', err);
});
