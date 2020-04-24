const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const port = process.env.PORT || 5000;

const csv = require("csv-parser");
const fs = require("fs");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => res.send("Hello World!"));

app.listen(port, () =>
  console.log(`Example app listening at http://localhost:${port}`)
);

app.listen(port, () => console.log(`Listening on port ${port}`));

var count = 0;

fs.createReadStream("../../scrapers/monster_com/jobs.csv")
  .pipe(csv())
  .on("data", (row) => {
    console.log(count, row);
    count = count + 1;
  })
  .on("end", () => {
    console.log("CSV file successfully processed");
  });
