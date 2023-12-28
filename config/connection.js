const mysql = require("mysql2");

//creates connection to the database
const db = mysql.createConnection(
  {
    //Apple M1 chip host
    host: "127.0.0.1",
    user: "root",
    password: "",
    database: "travel_db",
  },
  console.log("Connected to the database.")
);

module.exports = db;
