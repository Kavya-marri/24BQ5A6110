const express = require("express");
const logger = require("./logger");

const app = express();

app.use(logger);

app.get("/", (req, res) => {
    res.send("Logging Middleware Working");
});

const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});