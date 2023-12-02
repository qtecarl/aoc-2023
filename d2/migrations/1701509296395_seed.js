/* eslint-disable camelcase */

const fs = require("fs");
const path = require("path");

exports.shorthands = undefined;

exports.up = (pgm) => {
  const seed = fs.readFileSync("./input.txt", "utf8");
  const rows = seed.split("\n");

  const db_rows = [];

  for (const row of rows) {
    const id = row.match(/((?<=Game )[0-9]+)/g)[0];
    for (const e of row.split(": ")[1].split("; ")) {
      const red = e.match(/([0-9]+(?= red))/g);
      const green = e.match(/([0-9]+(?= green))/g);
      const blue = e.match(/([0-9]+(?= blue))/g);

      db_rows.push(
        "(" +
          id +
          "," +
          (red ? red[0] : 0) +
          "," +
          (green ? green[0] : 0) +
          "," +
          (blue ? blue[0] : 0) +
          ")"
      );
    }
  }

  pgm.sql(`
    INSERT INTO hand (id, r, g, b) VALUES
    ${db_rows.join(",")}
  `);
};

exports.down = (pgm) => {
  pgm.sql(`
        DELETE FROM hand;
    `);
};
