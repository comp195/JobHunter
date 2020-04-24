import React, { useEffect, useState } from "react";
import { Container, Box } from "@material-ui/core/";
import SlideOutMenu from "./components/SlideOutMenu";
import JobCard from "./components/JobCard";
import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import * as d3 from "d3";
import jobFile from "./jobs.csv";

const useStyles = makeStyles((theme) => ({
  background: {
    // backgroundColor: ""
  },
  bar: {
    // backgroundColor: "#e6e6fa"
  },
}));

function App() {
  const styles = useStyles();
  const [data, setData] = useState([]);

  useEffect(() => {
    d3.csv(jobFile).then(setData);
  }, []);

  console.log(data);
  console.log("1");

  return (
    <Box className={styles.background}>
      <Box className={styles.bar}>
        <SlideOutMenu />
      </Box>
      <Box>
        <Typography gutterBottom variant="h1" align="center" color="inherit">
          Job Finder
        </Typography>
        <Container>
          <JobCard jobData={data} />
        </Container>
      </Box>
    </Box>
  );
}

export default App;
