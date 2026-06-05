const fs = require("fs");

function logger(req, res, next) {
    const log = `${new Date().toISOString()} | ${req.method} | ${req.url}\n`;

    fs.appendFile("logs.txt", log, (err) => {
        if (err) {
            console.error("Logging Error:", err);
        }
    });

    next();
}

module.exports = logger;