import React, { useEffect, useState } from "react";
import { Box } from "@material-ui/core/";
import SlideOutMenu from "./components/SlideOutMenu";
import JobCard from "./components/JobCard";
import Typography from "@material-ui/core/Typography";
import * as d3 from "d3";
import monsterFile from "./csv/monster_jobs.csv";
import indeedFile from "./csv/indeed_jobs.csv";
import allFile from "./csv/allJobs.csv";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

// function Home() {
//   return <h2>Home</h2>;
// }

// function About() {
//   return <h2>About</h2>;
// }

// function Users() {
//   return <h2>Users</h2>;
// }

function App() {
  // const styles = useStyles();
  const [data, setData] = useState([]);
  const [indeed, setIndeed] = useState([]);
  const [monster, setMonster] = useState([]);
  const [type, setType] = useState("");

  useEffect(() => {
    // d3.csv(indeedFile).then(setData);
    // d3.csv(monsterFile).then(setData);
    // d3.csv(allFile).then(setData);
    Promise.all([d3.csv(allFile), d3.csv(monsterFile), d3.csv(indeedFile)])
      .then(function (files) {
        setData(files[0]);
        setMonster(files[1]);
        setIndeed(files[2]);
      })
      .catch(function (err) {
        // handle error here
      });
  }, []);

  return (
    <Box>
      <Box>
        <Router>
          <Box>
            <SlideOutMenu />
            <Typography
              gutterBottom
              variant="h1"
              align="center"
              color="inherit"
            >
              Job Finder
            </Typography>
            <Switch>
              <Route path="/Indeed">
                <JobCard jobData={indeed} />
              </Route>
              <Route path="/Monster">
                <JobCard jobData={monster} />
              </Route>
              <Route path="/">
                <JobCard jobData={data} />
              </Route>
            </Switch>
          </Box>
        </Router>
      </Box>
      <Box></Box>
    </Box>
  );
}

export default App;
