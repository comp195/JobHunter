import React, { useEffect, useState } from "react";
import { Container, Box } from "@material-ui/core/";
import SlideOutMenu from "./components/SlideOutMenu";
import JobCard from "./components/JobCard";
import Typography from "@material-ui/core/Typography";
import * as d3 from "d3";
import monsterFile from "./csv/monster.csv";
import indeedFile from "./csv/indeed.csv";
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
  const [type, setType] = useState("");

  useEffect(() => {
    if (type === "Indeed") {
      d3.csv(indeedFile).then(setData);
    } else if (type === "Monster") {
      d3.csv(monsterFile).then(setData);
    } else {
      d3.csv(allFile).then(setData);
    }
  }, [type]);

  return (
    <Box>
      <SlideOutMenu />
      <Box>
        <Typography gutterBottom variant="h1" align="center" color="inherit">
          Job Finder
        </Typography>
      </Box>
      <Box justifyContent="center">
        <Router>
          <Box justifyContent="center">
            <nav>
              <ul>
                <li>
                  <Link to="/" onClick={() => setType("All")}>
                    Home
                  </Link>
                </li>
                <li>
                  <Link to="/Indeed" onClick={() => setType("Indeed")}>
                    Indeed
                  </Link>
                </li>
                <li>
                  <Link to="/Monster" onClick={() => setType("Monster")}>
                    Monster
                  </Link>
                </li>
              </ul>
            </nav>
            <Switch>
              <Route path="/Indeed">{/* <JobCard jobData={data} /> */}</Route>
              <Route path="/Monster">{/* <JobCard jobData={data} /> */}</Route>
              <Route path="/">
                <JobCard jobData={data} />
              </Route>
            </Switch>
          </Box>
        </Router>
      </Box>
    </Box>
  );
}

export default App;
