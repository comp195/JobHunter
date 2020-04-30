import React, { useEffect, useState } from "react";
import { Container, Box } from "@material-ui/core/";
import SlideOutMenu from "./components/SlideOutMenu";
import JobCard from "./components/JobCard";
import Typography from "@material-ui/core/Typography";
import * as d3 from "d3";
import monsterFile from "./csv/monster.csv";
import indeedFile from "./csv/indeed.csv";
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
  const [indeed, setIndeed] = useState(true);

  useEffect(() => {
    if (indeed) {
      d3.csv(indeedFile).then(setData);
    } else {
      d3.csv(monsterFile).then(setData);
    }
  }, [indeed]);

  return (
    <Box>
      <SlideOutMenu />
      <Box>
        <Typography gutterBottom variant="h1" align="center" color="inherit">
          Job Finder
        </Typography>
        {/* <Container>
          <JobCard jobData={data} />
        </Container> */}
      </Box>
      <Box>
        <Router>
          <div>
            <nav>
              <ul>
                <li>
                  <Link to="/">Home</Link>
                </li>
                <li>
                  <Link to="/Indeed" onClick={() => setIndeed(true)}>
                    Indeed
                  </Link>
                </li>
                <li>
                  <Link to="/Monster" onClick={() => setIndeed(false)}>
                    Monster
                  </Link>
                </li>
              </ul>
            </nav>
            {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
            <Switch>
              <Route path="/Indeed">
                <JobCard jobData={data} />
              </Route>
              <Route path="/Monster">
                <JobCard jobData={data} />
              </Route>
              <Route path="/"></Route>
            </Switch>
          </div>
        </Router>
      </Box>
    </Box>
  );
}

export default App;
